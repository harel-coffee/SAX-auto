# P1: Question instantiation prompts
## P1.1: Instantiation of a process-reasoning question
**INPUT:**

**Phrase:** A, B, and C are activities in some process.
C occurs before A. A occurs before B.

**Question:** Does C occur before B?

**Instruction:** Considering the above question, choose any relevant concrete
activities A, B, and C in the domain of ≪transportation≫ that retain the truth of
the phrase statements. Using these terms, instantiate corresponding phrase
statements and a question statement in a form that matches the above statements
and question.

**OUTPUT (example):**

**Concrete Activities:**
A: Boarding the plane B: Takeoff of the plane C: Check-in at the airport

**Instantiated Phrase Statements:** Check-in at the airport occurs before boarding
the plane. Boarding the plane occurs before takeoff of the plane.

**Instantiated Question Statement:** Does check-in at the airport occur before
takeoff of the plane?

## P1.2: Instantiation of a causal-reasoning question

**INPUT:**

**Phrase:** A, B, and C are activities in some process. 
C causes the execution of A. C causes the execution of B. 

**Question:** Does A cause the execution of C?

**Instruction:** Considering the above question, choose any relevant concrete activities A, B, and C in the domain of <<transportation>> that retain the truth of the phrase statements. Using these terms, instantiate corresponding phrase statements and a question statement in a form that matches the above statements and question.

## P1.3: Instantiation of a combined-reasoning question

**INPUT:**

**Phrase:** A, B, and C are activities in some process. 
C occurs before A. A occurs before B. 
C causes the execution of A. C causes the execution of B.

**Question:** Does A cause the execution of B?

**Instruction:** Considering the above question, choose any relevant concrete activities A, B, and C in the domain of <<transportation>> that retain the truth of the phrase statements. Using these terms, instantiate corresponding phrase statements and a question statement in a form that matches the above statements and question.

# P2: LLM as a judge for faithfulness assessment

**INPUT:**

**Template question:** If we shorten C, will B be shortened?

**Instantiated question:** If we shorten Damage assessment team inspects the damage and estimates the cost of repair in duration, will Insurance policyholder receives the payout be shortened?

**Instruction:** Considering the instantiated question above a concrete version of the template question where the letters are replaced with process activity descriptions, when replacing these descriptions with their corresponding letters in the template, how would you rate the similarity between the revised instantiated question and the template question (where a 1 rate means they are identical and 0 they are completely different)? In your output, print only the rate value on a 0-1 scale.

**OUTPUT (Mixtral):**
0.9 or 90% similarity.

# P3: Reasoning prompts with seed questions

## P3.1: Process reasoning – seed questions

**Phrase:** A, B, and C are activities in some process.
C occurs before A. A occurs before B.

**Instruction:** Considering the above phrase about activities in a process, answer
the following question. Your answer should be limited to either Yes or No and
nothing else.

**Question:**
Does C occur before B?

## P3.2: Causal reasoning – seed questions

**Phrase:** A, B, and C are activities in some process.
C causes the execution of A. C causes the execution of B.

**Instruction:** Considering the above phrase about activities in a process, answer
the following question. Your answer should be limited to either Yes or No and
nothing else.

**Question:**
Does A cause the execution of C?

## P3.3: Combined reasoning – seed questions

**Phrase:** A, B, and C are activities in some process.
C occurs before A. A occurs before B.
C causes the execution of A. C causes the execution of B.

**Instruction:** Considering the above phrase about activities in a process, answer
the following question. Your answer should be limited to either Yes or No and
nothing else.

**Question:**
Does A cause the execution of B?

# P4: Reasoning prompts with instantiated questions (examples)

## P4.1: Process reasoning – instantiated questions

**Phrase:**
Issuing a financial report occurs before completing a financial audit. Completing a financial audit occurs before analyzing the financial data.

**Instruction:**
Considering the above phrase about activities in a process, answer the following question. Your answer should be limited to either Yes or No and nothing else.

**Question:**
Does issuing a financial report occur before analyzing the financial data?

## P4.2: Causal reasoning – instantiated questions

**Phrase:**
An Increase in Inflation causes the implementation of an Interest Rate Hike. An Increase in Inflation causes a Decrease in Investment.

**Instruction:**
Considering the above phrase about activities in a process, answer the following question. Your answer should be limited to either Yes or No and nothing else.

**Question:**
Does an Interest Rate Hike cause an Increase in Inflation?

## P4.3: Combined reasoning – instantiated questions

**Phrase:**
Vehicle maintenance team checking and maintaining the truck occurs before Truck driver starting the engine. Truck driver starting the engine occurs before Truck driver beginning the journey. Vehicle maintenance team checking and maintaining the truck causes the execution of Truck driver starting the engine. Vehicle maintenance team checking and maintaining the truck causes the execution of Truck driver beginning the journey.

**Instruction:**
Considering the above phrase about activities in a process, answer the following question. Your answer should be limited to either Yes or No and nothing else.

**Question:**
Does Truck driver starting the engine cause the execution of Truck driver beginning the journey?

