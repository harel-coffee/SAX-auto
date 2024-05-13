from enum import Enum
import json
import streamlit as st
import pandas as pd
import numpy as np
import os
import openai
import pandas as pd
from collections import Counter
from io import StringIO
import re
import requests

# Set the environment variable


openai.api_key = os.getenv("OPENAI_API_KEY")
docker_domain = os.getenv("ML_DOCKER_DOMAIN")
mode = os.getenv("ML_OPERATION_MODE")
iterations_string = os.getenv("LLM_ITERATIONS")
models_string = os.getenv("MODELS")

print('Environment: ', mode, docker_domain,iterations_string,models_string, models_string)

if (openai.api_key is None or docker_domain is None or iterations_string is None or models_string is None or mode is None) :
    raise Exception("Missing configuration parameters , check that the openAI key, URL prefix for ML API, model runtime mode, number of iterations and relevant models are specified")
iterations = int(iterations_string)
models = json.loads(models_string)


def create_word_frequency_dictionary(df,column_name):
    word_frequency = Counter()
    
    for value in df[column_name]:
        if pd.notna(value):
            # Split the string into words using ', ' as the separator
            words = [word.strip() for word in value.split(',')]
            
            # Update the word frequency counter
            word_frequency.update(words)
    
    return dict(word_frequency)

def filter_keywords(dict,iterations, threshold):
    calc_threshold = iterations*threshold
    filtered_words = {word: count for word, count in dict.items() if count > calc_threshold}

    # Get the list of words with counts > threshold
    filtered_word_list = list(filtered_words.keys())
    result_string = ", ".join(filtered_word_list)  # Join the list elements with a comma and space
    
    return result_string

def score_to_label(score):
    if score >= 0.9:
        return "Extremely Positive"
    elif score >= 0.7:
        return "Very Positive"
    elif score >= 0.5:
        return "Moderately Positive"
    elif score >= 0.3:
        return "Mildly Positive"
    elif score >= 0.1:
        return "Slightly Positive"
    elif score <= -0.9:
        return "Extremely Negative"
    elif score <= -0.7:
        return "Very Negative"
    elif score <= -0.5:
        return "Moderately Negative"
    elif score <= -0.3:
        return "Mildly Negative"
    elif score <= -0.1:
        return "Slightly Negative"
    else:
        return "Neutral"

def getModelSentiment(mname, narrative):
  sentiment = None
  if (mname == "VADER"):
    from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
    analyzer = SentimentIntensityAnalyzer()
    vls = analyzer.polarity_scores(narrative)
    # TODO: currently translating the compound score into a simple sentiment term. Will need to check if vader has something better already implemented.
    compound_score = vls['compound']
    
    sentiment = score_to_label(compound_score)
        
  else:
    raise Exception("Cannot run the model",mname," in a local mode")

  return sentiment

def runLocalModel(model, narrative) -> str:
    result = getModelSentiment(model,narrative)
    return result

def invokeModel(model, narrative) ->str:
    url="http://"+docker_domain+"/"+model+"/"+"infer"
    print("Invoking url:",url)
    params = {"sentence": narrative}    
    try:
        # Send a GET request to the URL with the query parameters
        response = requests.get(url, params=params)

        # Check if the request was successful (status code 200)
        if response.status_code == 200:
            # Parse the JSON response
            result = response.json()
            print("the parsed invocation result is: ", result)
            
            polarity_value = None

            for element_name, value in result.items():
                if 'polarity' in element_name:
                    polarity_value = value
                    break

            if polarity_value is not None:
                print(f'The polarity value returned by the model is: {polarity_value}')
            else:
                raise Exception('Polarity value not found in the model API result:',result)
            # extract the score from the result
            
            return float(polarity_value)
        else:
            print("Request to ML API failed with status code:", response.status_code)
            raise Exception("Request to ML API failed with status code:", response.status_code)

    except requests.exceptions.RequestException as e:
        print("Request error:", e)
        raise Exception("Request to ML API failed" ,e)


def runRemoteModel(model, narrative) -> str:
    result = invokeModel(model,narrative)
    sentiment = score_to_label(result)
    return sentiment

def runModel(model, narrative) ->str:
    print("In runModel:",model,", narrative: ",narrative, "mode:",mode)
    if mode  == "local":
        return runLocalModel(model, narrative)
    elif  mode == "remote":
        return runRemoteModel(model,narrative)
    else:
        raise Exception("Unknown invocation mode:",mode," ,configure either 'local' or 'remote'")

    
def run_chatgpt(narrative, sentiment,iterations,model) -> pd.DataFrame:
    f_prompt = "Please outline which terms in the following text support a {sentiment} sentiment . Here is the text: {text}" 
    f_sub_prompt = "{text},  {sentiment}"

    prompt = f_prompt.format(sentiment=sentiment, text=narrative)
    sub_prompt = f_sub_prompt.format(text=narrative, sentiment=sentiment)
    print(prompt)        

    df = pd.DataFrame()
    try:
        for i in range(iterations): 
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                {
                    "role": "system",
                    "content": "You are a helpful assistant very experienced in understanding subtleties in text. Given each textual narrative you can determine which words or terms in the text affect the overall sentiment of the text as being positive/negative or neutral.  You always return the list of those words in the text as a simple list, nothing else, like this :\"word1, word2, word3\". If no words support such a sentiment, return an empty list, nothing else, like this: \"\""
                },
                {
                    "role": "user",
                    "content": prompt
                },
                    
                
                ],
                temperature=0.7,
                max_tokens=256,
                top_p=1,
                frequency_penalty=0,
                presence_penalty=0
            )

            print(response)
            finish_reason = response['choices'][0]['finish_reason']
            response_txt = response['choices'][0]['message']['content']
                
            #print(finish_reason) 
            print(response_txt)
            new_sentiment = runModel(model,response_txt)
            print(new_sentiment)
            if new_sentiment == sentiment:
                new_row = {      
                    'prompt':prompt, 
                    'sub_prompt':sub_prompt, 
                    'response_txt':response_txt, 
                    'finish_reason':finish_reason}
                new_row = pd.DataFrame([new_row])
                df = pd.concat([df, new_row], axis=0, ignore_index=True)
    except Exception as e:
        print("Request error:", e)
        raise Exception("Request to LLM failed" ,e)
    
    return df


###### UI code
st.title('Model-independent explainer for textual narratives')

#Get the narrative
st.subheader('Add narrative for analysis:')
left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
narrative = left_column.text_area('Write text',placeholder = "Input your narrative here...")

with right_column:
    uploaded_file = st.file_uploader("Choose an narrative file:")
    if uploaded_file is not None:        
      stringio = StringIO(uploaded_file.getvalue().decode("utf-8"))
      #st.write(stringio)

      # To read file as string:
      narrative = stringio.read()

st.write("Current narrative:",narrative)

if 'narrative' in locals() and narrative is not None and narrative != "":   
    ####List to choose the model    
    model = st.selectbox(
        'Select the model',
        models
    )
    if model is not None:
        'You selected: ', model
    
    sentiment = "negative"
    key_words = []
    if st.button('Run model'):
        sentiment = runModel(model,narrative)
        st.write('Sentiment: %s' % sentiment)
        text = 'Analyzing key words for ' +sentiment+' sentiment...'
        data_load_state = st.text(text)
        column_name = 'response_txt'
        if iterations is None:
            iterations = 1        
        df = run_chatgpt(narrative,sentiment,iterations,model)
        word_frequency_dict = create_word_frequency_dictionary(df,column_name)
        st.table(word_frequency_dict)
        data_load_state.text("Done!")

        st.subheader("The strongest keywords:")
        key_words = filter_keywords(word_frequency_dict,len(df),0.7)
        st.write(key_words)
        #st.write('Sentiment:',runModel(model,key_words))

        st.subheader("The explanation:")
        words_to_highlight = key_words.split(",")
        
        highlighted_text = narrative
        
        for word in words_to_highlight:        
            pattern = re.compile(re.escape(word), re.IGNORECASE)
            highlighted_text = pattern.sub(
                f'<span style="background-color: yellow; padding: 3px; border-radius: 3px; font-weight: bold;">{word}</span>',
                highlighted_text
            )
        
        st.markdown(highlighted_text, unsafe_allow_html=True)



    

    




