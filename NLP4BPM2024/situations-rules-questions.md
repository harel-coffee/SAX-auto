# Overall BP<sup>C</sup> domain as a combination of three underlying causal patterns and the corresponding viable process structures:

## Assumptions: 

* $A = True$ means that A executed and $A = False$ means that A did not execute.
* $\rightarrow$ denotes <i>occurs before</i> which means that given $A\rightarrow B$, for any process execution in which both $A$ and $B$ execute, the execution of $A$ occurs before the execution of $B$.
* $\xrightarrow{C}$ denotes <i>causal-execution-dependence</i> which means that given $A\xrightarrow{C}B$, if $A$ executes, $B$ will necessarily execute sometime later. ***Note: “always” causes.*** 
* **Close world assumption.** For any premise $p$, if $p$ is not in explicitly articulated in the situation phrases $\mathcal{S}$ then $p=False$.

## Situation 1: Confounder with no discrepancy

* Process: $C\rightarrow A$, $C\rightarrow B$ (split)
* Causal: $C\xrightarrow{C}A$, $C\xrightarrow{C}B$

### Situation Phrases $\mathcal{S}_1$
* A, B, and C are activities in some process.
#### Process: 
* C occurs before A. C occurs before B.
#### Causal: 
* C causes the execution of A. C causes the execution of B.

### Rules $\mathcal{R}_1$
#### Process:
* PR1: $A\rightarrow C \Leftarrow (A\rightarrow B) \land (B\rightarrow C)$ (transitive inference) - i.e., IF (a before b)=TRUE AND (b before c)=TRUE THEN (a before c)=TRUE
* PR2: $\lnot (B\rightarrow A) \Leftarrow A\rightarrow B$ (no symmetry inference) [relate to DAG and k-unfolding]
* PR3: $A\leftarrow B \Leftarrow B\rightarrow A$ (antonym precedence negation inference)
* PR4: $A\not\rightarrow A$ (no reflexivity) [no repetitions]

#### Causal: 
* No additional rules.

#### Combined:
* No additional rules.

### Questions $\mathcal{Q}_1$
#### Process:
* QP1: Does A occur before B? A: No (deduced from close world assumption)
* QP2: Does B occur before A? A: No (same as Q1)
* QP3: Does A occur after B? A: No (PR3 + close world assumption)
* QP4: Does B occur after A? A: No (PR3 + close world assumption)

#### Causal:
* Since the pattern is the same for causal as in situation #2, no additional questions here (see situation #2).

#### Combined:
* None.

## Situation 2: Confouder with discrepancy
* Process: $A\rightarrow B\rightarrow C$ (or $A\rightarrow C\rightarrow B$)
* Causal: $A\xrightarrow{C}B, A\xrightarrow{C}C$

### Situation Phrases $\mathcal{S}_2$
* A, B, and C are activities in some process.
#### Process: 
* A occurs before B. B occurs before C.
#### Causal: 
* A causes the execution of B. A causes the execution of C.

### Rules $\mathcal{R}_2$
#### Process:
* PR1: $A\rightarrow C \Leftarrow (A\rightarrow B) \land (B\rightarrow C)$ (transitive inference)
* PR2: $\lnot (B\rightarrow A) \Leftarrow A\rightarrow B$ (no symmetry inference) [relate to DAG and k-unfolding]
* PR3: $A\leftarrow B \Leftarrow B\rightarrow A$ (antonym precedence negation inference)
* PR4: $A\not\rightarrow A$ (no reflexivity) [no repetitions]
* PR5: $B \Leftarrow (A\rightarrow B) \land A$ (entailed from the meaning of $\rightarrow$)

#### Causal: 
* CR1: not a>c: c>a (no symmetry inference)
* CR2: a>c: a>b, b>c (transitive inference) [relevant only in the mediator pattern]
* CR3: a<b: b>a (cause vs because) 
* CR4: not b: a>b, not a [similarly a: a>b, b]

#### Combined:
* PCR1: a>>b: a>b (i.e., IF (a causes b)=TRUE THEN (a precedes b)=TRUE)
* PCR2: not b>a: a>>b (i.e., IF (a precedes b)=TRUE THEN (b causes a)=FALSE)

### Questions $\mathcal{Q}_2$
#### Process:
* QP1: Does A occur before C? A: Yes (deduced from PR1)
* QP2: Does C occur before A? A: No (deduced from PR2 deduced from (A occurs before C) = TRUE in Q1)
* QP3: Does B occur after A? A: Yes (deduced from PR3 deduced from (A occurs before B) = TRUE in phrase )
* QP4: Does C occur after A? A: Yes (deduced from PR3 deduced from (A occurs before C) = TRUE in Q1)
* QP5: Does A occur after B? A: No (deduced from PR2 since (A occurs before B) = TRUE in phrase )
* QP6: Does A occur after C? A: No (deduced from PR2 since (A occurs before C) = TRUE in Q1)
* QP7: Does B occur after C? A: No (deduced from PR3 since (C occurs before B) = FALSE deduced from PR2 )

#### Causal:
* QC1: Does A cause the execution of C? A: No (CR1)
* QC2: Does B cause the execution of C? A: No (CR1)
* QC3: Does A execute because of C? A: Yes (CR3)
* QC4: Does B execute because of C? A: Yes (CR3)
* QC5: If C doesn’t execute, will A ever execute? A: No (CR4)
* QC6: If C doesn’t execute, will B ever execute? A: No (CR4)

#### Combined:
* QPC1: Does A cause the execution of B? A: No (because we don’t know according to close world assumption)
* QPC2: Does B cause the execution of A? A: No (because we don’t know, and A>>B implies not B>A)

## Situation 3: Collider with no discrepancy
C: A>C; B>C
P: A>C; B>C (join)

## Situation 4: Collider with discrepancy
C: A>C; B>C
P: A>B>C (or B>A>C)

## Situation 5: Mediator
C: A>B; B>C
P: A>B; B>C

# Work in progress

## Situation 2
Additional rules not manifested in the process perspective:
PR: a >>> b: exists c such that a>>>c, c>>b [***no manifestation in this pattern]
PR: a#b: not a>>b, not b>>a [***no manifestation in this pattern]
PR: a||b: a>>b, b>>a [***no manifestation in this pattern]

Additional possible questions for wider coverages of process perspective for situation 2: [not in paper]

Q: Does C occur before A? A: Yes. (obvious to test the stated)
Q: Does A occur before B? A: Yes. (obvious as stated)
Q: Does A occur before C? A: No. (PR2)
Q: Does B occur before A? A: No. (PR2)
Q: Does B occur after A? A: Yes. (PR3)
Q: Does A occur after C? A: Yes. (PR3)
Q: Does C occur before B? A: Yes (PR1)
Q: Does C occur before C? A: No (missing)

Causal rule extension and corresponding questions:
* CR5: shorten(b): a>b, shorten(a)

* QC7: If we shorten(A), will shorten(B) hold? A: No (same for extend)
* QC8: If we shorten(B), will shorten(A) hold? A: No (same for extend)
* QC9: If we shorten(C), will shorten(A) hold? A: Yes (same for extend)
* QC10: If we shorten(C), will shorten(B) hold? A: Yes (same for extend)




Test 1 (step 1):

Use LLM to see how it answers to (a set of X) questions as phrased in the above (with the phrase template given in the context). Comapare Merlinite to openAI.

***LIOR: for the paper, a technical spec of the models compared below?

Process reasoning results (success rate):

Phrase:

A, B, and C are activities in some process. C occurs before A. A occurs before B. 

Instruction:

Considering the above phrase about activities in a process, answer the following question. Your answer should be limited to either Yes or No and nothing else.

Question

Answer

Merlinite-7b (10 runs)

Mixtral instruct 8x 7b

GPT4o

GPT4

GPT3.5

Total

58%

71%

100%

85%

65%

Does C occur before B? 

Yes

1/10

10/10

10/10

10/10

9/10

Does B occur before C? 

No

10/10

10/10

10/10

10/10

10/10

Does A occur after C?

Yes

0/10

0/10

10/10

10/10

10/10

Does B occur after C? 

Yes

0/10

10/10

10/10

10/10

10/10

Does C occur after A?

No

10/10

10/10

10/10

10/10

4/10

Does C occur after B? 

No

10/10

0/10

10/10

0/10

1/10

Does A occur after B? 

No

10/10

10/10

10/10

10/10

2/10

Causal process reasoning results:

Phrase:

A, B, and C are activities in some process. C causes the execution of A. C causes the execution of B.

Instruction:

Considering the above phrase about activities in a process, answer the following question. Your answer should be limited to either Yes or No and nothing else.

Question

Answer

Merlinite-7b (10 runs)

Mixtral instruct 8x 7b

GPT4o

GPT4

GPT3.5

Total

66%

100%

100%

100%

56%

Does A cause the execution of C? 

No

10/10

10/10

10/10

10/10

3/10

Does B cause the execution of C? 

No

10/10

10/10

10/10

10/10

4/10

Does A execute because of C? 

Yes

0/10

10/10

10/10

10/10

10/10

Does B execute because of C? 

Yes

0/10

10/10

10/10

10/10

10/10

If C doesn’t execute, will A ever execute? 

No

10/10

10/10

10/10

10/10

4/10

If C doesn’t execute, will B ever execute?

No

10/10

10/10

10/10

10/10

3/10

Combined process and causal reasoning results:

Phrase:

A, B, and C are activities in some process. C occurs before A. A occurs before B. C causes the execution of A. C causes the execution of B.

Instruction:

Considering the above phrase about activities in a process, answer the following question. Your answer should be limited to either Yes or No and nothing else.

Question

Answer

Merlinite-7b (10 runs)

Mixtral instruct 8x 7b

GPT4o

GPT4

GPT3.5

Total

66%

66%

80%

70%

41%

Does A cause the execution of B?

No

10/10

10/10

10/10

6/10

0/10

Does B cause the execution of A?

No

10/10

10/10

10/10

10/10

3/10

If we shorten A, will B be shortened? 

No

10/10

0/10

8/10

2/10

2/10

If we shorten B, will A be shortened? 

No

10/10

10/10

10/10

10/10

1/10

If we shorten C, will A be shortened?

Yes

0/10

10/10

5/10

5/10

9/10

If we shorten C, will B be shortened? 

Yes

0/10

0/10

5/10

9/10

10/10

Test 2 (step 2):

Use Mixtral instruct 8x 7b to instantiate the phrase and the questions to concrete problem domain statements.

Phrase statements: A, B, and C are activities in some process. C occurs before A. A occurs before B. 

Question: Does C occur before B? 

Instruction: Considering the above question, choose any relevant concrete activities A, B, and C in the domain of transportation that retain the truth of the phrase statements. Using these terms, instantiate corresponding phrase statements and a question statement in a form that matches the above statements and question.

Possible domains: transportation, manufacturing, logistic, retail, finance, insurance, medical…

Example:

Concrete Activities:

A: Boarding the plane B: Takeoff of the plane C: Check-in at the airport

Instantiated Phrase Statements: Check-in at the airport occurs before boarding the plane. Boarding the plane occurs before takeoff of the plane.

Instantiated Question Statement: Does check-in at the airport occur before takeoff of the plane?

***NOTE: For the paper, since we are pursuing an exemplar attempt of the overall process, I didn’t record the mappings between the letters A,B,C and the instantiated activity as in the above. However, in the full process, it will be essential to ensure not only that we get it in the output from the LLM, but we also need it to later populate a more reliable score of whether the instantiated question is a faithful instantiation of the template question (LLM as a judge), as this will be crucial for establishing the quality (accuracy/correctness) of the populated set.

Process reasoning questions instantiation (across domains):

Phrase statements: A, B, and C are activities in some process. C occurs before A. A occurs before B. 

Question: Does C occur before B? 

Instruction: Considering the above question, choose any relevant concrete activities A, B, and C in the domain of transportation that retain the truth of the phrase statements. Using these terms, instantiate corresponding phrase statements and a question statement in a form that matches the above statements and question.

Question template

Phrase template

Domain

Concrete phrase

Concrete question

Example (GPT3.5): Does C occur before B? 

C occurs before A. A occurs before B. 

Transportation

Check-in at the airport occurs before boarding the plane. Boarding the plane occurs before takeoff of the plane.

Does check-in at the airport occur before takeoff of the plane?

Does C occur before B? 

C occurs before A. A occurs before B.

Finance

1. Issuing a financial report (C) occurs before completing a financial audit (A). 2. Completing a financial audit (A) occurs before analyzing the financial data (B).

Does issuing a financial report (C) occur before analyzing the financial data (B)?

Does B occur before C?

^^^

Transportation

1. Arriving at the station (C) and boarding the train (A) are activities in the process of taking a train. Arriving at the station (C) occurs before boarding the train (A). 2. Boarding the train (A) and departing from the station (B) are activities in the process of taking a train. Boarding the train (A) occurs before departing from the station (B).

Does departing from the station (B) occur before arriving at the station (C)?

Does A occur after C?

^^^

Logistics

1. Receiving goods (C) and inspecting goods (A) are activities in the process of logistics. Receiving goods (C) occurs before inspecting goods (A). 2. Inspecting goods (A) and shipping goods (B) are activities in the process of logistics. Inspecting goods (A) occurs before shipping goods (B).

Does inspecting goods (A) occur after receiving goods (C)?

Does B occur after C? 

^^^

Retail

1. Receiving stock (C) and counting inventory (A) are activities in the process of retail management. Receiving stock (C) occurs before counting inventory (A). 2. Counting inventory (A) and restocking shelves (B) are activities in the process of retail management. Counting inventory (A) occurs before restocking shelves (B).

Does restocking shelves (B) occur after receiving stock (C)?

Does C occur after A?

^^^

Manufacturing

1. Raw material inspection (C) and assembly (A) are activities in the process of manufacturing. Raw material inspection (C) occurs before assembly (A). 2. Assembly (A) and quality control (B) are activities in the process of manufacturing. Assembly (A) occurs before quality control (B).

Does raw material inspection (C) occur after assembly (A)?

Does C occur after B? 

^^^

Insurance

1. Claim submission (C) and claim investigation (A) are activities in the process of insurance. Claim submission (C) occurs before claim investigation (A). 2. Claim investigation (A) and claim payment (B) are activities in the process of insurance. Claim investigation (A) occurs before claim payment (B).

Does claim submission (C) occur after claim payment (B)?

Does A occur after B? 

^^^

Medical

1. Patient registration (C) and patient consultation (A) are activities in the process of medical treatment. Patient registration (C) occurs before patient consultation (A). 2. Patient consultation (A) and prescription (B) are activities in the process of medical treatment. Patient consultation (A) occurs before prescription (B).

Does patient consultation (A) occur after prescription (B)?

Causal reasoning questions instantiation:

Phrase statements: A, B, and C are activities in some process. C causes the execution of A. C causes the execution of B. 

Question: Does A cause the execution of C? 

Instruction: Considering the above question, choose any relevant concrete activities A, B, and C in the domain of transportation that retain the truth of the phrase statements. Using these terms, instantiate corresponding phrase statements and a question statement in a form that matches the above statements and question.

Question template

Phrase template

Domain

Concrete phrase

Concrete question

Does A cause the execution of C? 

C causes the execution of A. C causes the execution of B.

Finance

1. An Increase in Inflation (C) causes the implementation of an Interest Rate Hike (A). 2. An Increase in Inflation (C) causes a Decrease in Investment (B).

Does an Interest Rate Hike (A) cause an Increase in Inflation (C)?

Does B cause the execution of C? 

^^^

Transportation

1. A Vehicle Approaching an Intersection (C) causes the Traffic Light to Change (A). 2. A Vehicle Approaching an Intersection (C) causes a Vehicle Stop (B).

Does a Vehicle Stop (B) cause a Vehicle to Approach an Intersection (C)?

Does A execute because of C? 

^^^

Logistics

1. Goods Receipt at Warehouse (C) causes the execution of Goods Delivery (A). 2. Goods Receipt at Warehouse (C) causes the execution of Warehouse Stocking (B).

Does Goods Delivery (A) execute because of Goods Receipt at Warehouse (C)?

Does B execute because of C? 

^^^

Retail

1. New Product Arrival (C) causes the execution of Product Display Update (A). 2. New Product Arrival (C) causes the execution of Product Restocking (B).

Does Product Restocking (B) execute because of New Product Arrival (C)?

If C doesn’t execute, will A ever execute? 

^^^

Manufacturing

1. Component Manufacturing (C) causes the execution of Product Assembly (A). 2. Component Manufacturing (C) causes the execution of Component Installation (B).

If Component Manufacturing (C) doesn't execute, will Product Assembly (A) ever execute?

If C doesn’t execute, will B ever execute?

^^^

Insurance

1. Policyholder Reporting an Incident (C) causes the execution of Claims Processing (A). 2. Policyholder Reporting an Incident (C) causes the execution of Claims Investigation (B).

If Policyholder Reporting an Incident (C) doesn't execute, will Claims Investigation (B) ever execute?

Combined process and causal reasoning questions instantiation:

Phrase statements: A, B, and C are activities in some process. C occurs before A. A occurs before B. C causes the execution of A. C causes the execution of B. 

Question: Does A cause the execution of B?

Instruction: Considering the above question, choose any relevant concrete activities A, B, and C in the domain of transportation that retain the truth of the phrase statements. Using these terms, instantiate corresponding phrase statements and a question statement in a form that matches the above statements and question.

Question template

Phrase template

Domain

Concrete phrase

Concrete question

Does A cause the execution of B?

C occurs before A. A occurs before B. C causes the execution of A. C causes the execution of B. 

Transportation

1. C (Vehicle maintenance team checks and maintains the truck) occurs before A (Truck driver starts the engine). 2. A (Truck driver starts the engine) occurs before B (Truck driver begins the journey). 3. C (Vehicle maintenance team checks and maintains the truck) causes the execution of A (Truck driver starts the engine). 4. C (Vehicle maintenance team checks and maintains the truck) causes the execution of B (Truck driver begins the journey).

Does A (Truck driver starts the engine) cause the execution of B (Truck driver begins the journey)?

Does B cause the execution of A?

^^^

Finance

1. C (Credit analyst reviews the loan application) occurs before A (Loan officer approves a loan application). 2. A (Loan officer approves a loan application) occurs before B (Loan officer disburses the approved loan amount to the borrower). 3. C (Credit analyst reviews the loan application) causes the execution of A (Loan officer approves a loan application). 4. C (Credit analyst reviews the loan application) causes the execution of B (Loan officer disburses the approved loan amount to the borrower).

Does B (Loan officer disburses the approved loan amount to the borrower) cause the execution of A (Loan officer approves a loan application)?

If we shorten A, will B be shortened? 

^^^

Logistics

1. C (Logistics coordinator inspects and releases the cargo for transportation) occurs before A (Warehouse worker loads cargo onto a truck). 2. A (Warehouse worker loads cargo onto a truck) occurs before B (Truck driver delivers the cargo to the recipient). 3. C (Logistics coordinator inspects and releases the cargo for transportation) causes the execution of A (Warehouse worker loads cargo onto a truck). 4. C (Logistics coordinator inspects and releases the cargo for transportation) causes the execution of B (Truck driver delivers the cargo to the recipient).

If we shorten A (Warehouse worker loads cargo onto a truck) in duration, will B (Truck driver delivers the cargo to the recipient) be shortened?

If we shorten B, will A be shortened? 

^^^

Retail

1. C (Online order management system confirms the customer's order and assigns it to a sales associate) occurs before A (Sales associate picks and packs items for customer's online order). 2. A (Sales associate picks and packs items for customer's online order) occurs before B (Delivery driver delivers the customer's order to their address). 3. C (Online order management system confirms the customer's order and assigns it to a sales associate) causes the execution of A (Sales associate picks and packs items for customer's online order). 4. C (Online order management system confirms the customer's order and assigns it to a sales associate) causes the execution of B (Delivery driver delivers the customer's order to their address).

If we shorten B (Delivery driver delivers the customer's order to their address) in duration, will A (Sales associate picks and packs items for customer's online order) be shortened?

If we shorten C, will A be shortened?

^^^

Manufacturing

1. C (Machine operator sets up and calibrates the machinery used to produce the component) occurs before A (Assembly line worker installs a component onto a product). 2. A (Assembly line worker installs a component onto a product) occurs before B (Quality control inspector checks the product for defects). 3. C (Machine operator sets up and calibrates the machinery used to produce the component) causes the execution of A (Assembly line worker installs a component onto a product). 4. C (Machine operator sets up and calibrates the machinery used to produce the component) causes the execution of B (Quality control inspector checks the product for defects).

If we shorten C (Machine operator sets up and calibrates the machinery used to produce the component) in duration, will A (Assembly line worker installs a component onto a product) be shortened?

If we shorten C, will B be shortened? 

^^^

Insurance

1. C (Damage assessment team inspects the damage and estimates the cost of repair) occurs before A (Insurance claims adjuster assesses the damage and determines the payout amount). 2. A (Insurance claims adjuster assesses the damage and determines the payout amount) occurs before B (Insurance policyholder receives the payout). 3. C (Damage assessment team inspects the damage and estimates the cost of repair) causes the execution of A (Insurance claims adjuster assesses the damage and determines the payout amount). 4. C (Damage assessment team inspects the damage and estimates the cost of repair) causes the execution of B (Insurance policyholder receives the payout).

If we shorten C (Damage assessment team inspects the damage and estimates the cost of repair) in duration, will B (Insurance policyholder receives the payout) be shortened?

After cleaning the phrasing to match exactly the templates, we then use the instnatiated questions for benchmarking.

Process reasoning benchmarking

Phrase:

Issuing a financial report occurs before completing a financial audit. Completing a financial audit occurs before analyzing the financial data.

Instruction:

Considering the above phrase about activities in a process, answer the following question. Your answer should be limited to either Yes or No and nothing else.

Question:

Does issuing a financial report occur before analyzing the financial data?

Question

Phrase

Answer

Merlinite-7b 

Mixtral instruct 8x 7b

Total

100%

100%

Does issuing a financial report occur before analyzing the financial data?

Issuing a financial report occurs before completing a financial audit. Completing a financial audit occurs before analyzing the financial data.

Yes

10/10

10/10

Does departing from the station occur before arriving at the station?

Arriving at the station occurs before boarding the train. Boarding the train occurs before departing from the station.

No

10/10

10/10

Does inspecting goods occur after receiving goods?

Receiving goods occurs before inspecting goods. Inspecting goods occurs before shipping goods.

Yes

10/10

10/10

Does restocking shelves occur after receiving stock?

Receiving stock occurs before counting inventory. Counting inventory occurs before restocking shelves.

Yes

10/10

10/10

Does raw material inspection occur after assembly?

Raw material inspection occurs before assembly. Assembly occurs before quality control.

No

10/10

10/10

Does claim submission occur after claim payment?

Claim submission occurs before claim investigation. Claim investigation occurs before claim payment.

No

10/10

10/10

Does patient consultation occur after prescription?

Patient registration occurs before patient consultation. Patient consultation occurs before prescription.

No

10/10

10/10

Causal reasoning benchmarking

Phrase:

An Increase in Inflation causes the implementation of an Interest Rate Hike. An Increase in Inflation causes a Decrease in Investment.

Instruction:

Considering the above phrase about activities in a process, answer the following question. Your answer should be limited to either Yes or No and nothing else.

Question:

Does an Interest Rate Hike cause an Increase in Inflation?

Question

Phrase

Answer

Merlinite-7b 

Mixtral instruct 8x 7b

Total

98%

100%

Does an Interest Rate Hike cause an Increase in Inflation?

An Increase in Inflation causes the implementation of an Interest Rate Hike. An Increase in Inflation causes a Decrease in Investment.

No

10/10

10/10

Does a Vehicle Stop cause a Vehicle to Approach an Intersection?

A Vehicle Approaching an Intersection causes the Traffic Light to Change. 2. A Vehicle Approaching an Intersection causes a Vehicle Stop.

No

9/10

10/10

Does Goods Delivery execute because of Goods Receipt at Warehouse?

Goods Receipt at Warehouse causes the execution of Goods Delivery. Goods Receipt at Warehouse causes the execution of Warehouse Stocking.

Yes

10/10

10/10

Does Product Restocking execute because of New Product Arrival?

New Product Arrival causes the execution of Product Display Update. New Product Arrival causes the execution of Product Restocking.

Yes

10/10

10/10

If Component Manufacturing doesn't execute, will Product Assembly ever execute?

Component Manufacturing causes the execution of Product Assembly. Component Manufacturing causes the execution of Component Installation.

No

10/10

10/10

If Policyholder Reporting an Incident doesn't execute, will Claims Investigation ever execute?

Policyholder Reporting an Incident causes the execution of Claims Processing. Policyholder Reporting an Incident causes the execution of Claims Investigation.

No

10/10

10/10

Combined process and causal reasoning benchmarking

Phrase:

Vehicle maintenance team checking and maintaining the truck occurs before Truck driver starting the engine. Truck driver starting the engine occurs before Truck driver beginning the journey. Vehicle maintenance team checking and maintaining the truck causes the execution of Truck driver starting the engine. Vehicle maintenance team checking and maintaining the truck causes the execution of Truck driver beginning the journey.

Instruction:

Considering the above phrase about activities in a process, answer the following question. Your answer should be limited to either Yes or No and nothing else.

Question:

Does Truck driver starting the engine cause the execution of Truck driver beginning the journey?

Question

Phrase

Answer

Merlinite-7b 

Mixtral instruct 8x 7b

Total

66%

65%

Does Truck driver starting the engine cause the execution of Truck driver beginning the journey?

Vehicle maintenance team checking and maintaining the truck occurs before Truck driver starting the engine. Truck driver starting the engine occurs before Truck driver beginning the journey. Vehicle maintenance team checking and maintaining the truck causes the execution of Truck driver starting the engine. Vehicle maintenance team checking and maintaining the truck causes the execution of Truck driver beginning the journey.

No

1/10

9/10

Does Loan officer disburses the approved loan amount to the borrower cause the execution of Loan officer approves a loan application?

Credit analyst reviews the loan application occurs before Loan officer approves a loan application. Loan officer approves a loan application occurs before Loan officer disburses the approved loan amount to the borrower. Credit analyst reviews the loan application causes the execution of Loan officer approves a loan application. Credit analyst reviews the loan application causes the execution of Loan officer disburses the approved loan amount to the borrower.

No

10/10

10/10

If we shorten Warehouse worker loads cargo onto a truck in duration, will Truck driver delivers the cargo to the recipient be shortened?

Logistics coordinator inspects and releases the cargo for transportation occurs before Warehouse worker loads cargo onto a truck. Warehouse worker loads cargo onto a truck occurs before Truck driver delivers the cargo to the recipient. Logistics coordinator inspects and releases the cargo for transportation causes the execution of Warehouse worker loads cargo onto a truck. Logistics coordinator inspects and releases the cargo for transportation causes the execution of Truck driver delivers the cargo to the recipient.

No

0/10

10/10

If we shorten Delivery driver delivers the customer's order to their address in duration, will Sales associate picks and packs items for customer's online order be shortened?

Online order management system confirms the customer's order and assigns it to a sales associate occurs before Sales associate picks and packs items for customer's online order. Sales associate picks and packs items for customer's online order occurs before Delivery driver delivers the customer's order to their address. Online order management system confirms the customer's order and assigns it to a sales associate causes the execution of Sales associate picks and packs items for customer's online order. Online order management system confirms the customer's order and assigns it to a sales associate causes the execution of Delivery driver delivers the customer's order to their address.

No

10/10

10/10

If we shorten Machine operator sets up and calibrates the machinery used to produce the component in duration, will Assembly line worker installs a component onto a product be shortened?

Machine operator sets up and calibrates the machinery used to produce the component occurs before Assembly line worker installs a component onto a product. Assembly line worker installs a component onto a product occurs before Quality control inspector checks the product for defects. Machine operator sets up and calibrates the machinery used to produce the component causes the execution of Assembly line worker installs a component onto a product. Machine operator sets up and calibrates the machinery used to produce the component causes the execution of Quality control inspector checks the product for defects.

Yes

10/10

0/10

If we shorten Damage assessment team inspects the damage and estimates the cost of repair in duration, will Insurance policyholder receives the payout be shortened?

Damage assessment team inspects the damage and estimates the cost of repair occurs before Insurance claims adjuster assesses the damage and determines the payout amount. Insurance claims adjuster assesses the damage and determines the payout amount occurs before Insurance policyholder receives the payout. Damage assessment team inspects the damage and estimates the cost of repair causes the execution of Insurance claims adjuster assesses the damage and determines the payout amount. Damage assessment team inspects the damage and estimates the cost of repair causes the execution of Insurance policyholder receives the payout.

Yes

9/10

0/10

Extending the templates for “complete” (pattern-relative) coverage (we only add aspects specificto the different :

patterns unfolding from non-discrepancy (confounder):

No Discrepancy: (confounder)

Process: C>>A; C>>B (split) 

Causal: C>A; C>B

Phrase templates (knowledge facts reflective of the above pattern): 

A, B, and C are activities in some process.

C occurs before A. C occurs before B.

C causes the execution of A. C causes the execution of B.

Process reasoning (temporal): 

We anticipate (process related inference rules):

PR1: a>>>c: a>>b, b>>c (transitive inference) - i.e., IF (a before b)=TRUE AND (b before c)=TRUE THEN (a before c)=TRUE

PR2: not b>>a: a>>b (no symmetry inference) [relate to DAG and k-unfolding]

PR3: a<<b: b>>a (antonym precedence negation inference)

PR4: a>>a (no reflexivity) [no repetitions]

In more expressive process forms that also have || (parralelism):a||b: c>>a, c>>b,not a>>b,not b>>a [To verify. but in our case, not considered)

Process: C>>A; C>>B (split) 

Questions:

QP1: Does A occur before B? A: No (deduced from close world assumption)

QP2: Does B occur before A? A: No (same as Q1)

QP3: Does A occur after B? A: No (PR3 + close world assumption)

QP4: Does B occur after A? A: No (PR3 + close world assumption)

Lior: I think other questions may be redundant.

Causal process reasoning:

With respect to the causal rules, since the pattern is the same for causal, so no additional questions here.

Combined process and causal reasoning:

Lior: I can’t think of anything that could be added here.

patterns unfolding from discrepancy (collider):

Discrepancy: (collider)

Process: A>>B>>C  (or B>>A>>C)

Causal: A>C; B>C 

Phrase templates (knowledge facts reflective of the above discrepancy pattern): 

A, B, and C are activities in some process.

A occurs before B. B occurs before C.

A causes the execution of C. B causes the execution of C.

Process reasoning (temporal): 

The same as in the discrepency case for a confounder.

Causal process reasoning: 

w.r.t. CR4: not b: a>b, not a, here also, it may be interesting

QC1: If A doesn’t execute, will C ever execute? A: No (CR4)

QC2: If B doesn’t execute, will C ever execute? A: No (CR4)

Combined process and causal process reasoning:

Since A>>B, such a relation may be deceiving, hence motovating two questions:

QCP1: Does A cause the execution of B? A: No (close world assumption)

QCP2: Does B cause the execution of A? A: No (both close world and also entailment from A>>B)

patterns unfolding from non discrepancy (collider):

No Discrepancy: (collider)

Process: A>>C; B>>C  (join)

Causal: A>C; B>C

Phrase templates (knowledge facts reflective of the above discrepancy pattern): 

A, B, and C are activities in some process.

A occurs before C. B occurs before C.

A causes the execution of C. B causes the execution of C.

Process reasoning (temporal): 

QP1: Does A occur before B? A. No. (provided close world assumption, may be different if we also know that A#B or that A||B distinguishing between XOR-join and AND-join).

Similarly in the opposite direction:

QP2: Does B occur before A? A. No (same argumentation).

Process and causal reasoning: 

PCR1: A||B: A>>C, B>>C, (A>C or B>C) [added if we extend to support || in the process, forces a AND-join similar to forcing AND-split in the confounder case for the non discrepancy cases]

I think that if we know the both A>C and B>C, it may imply that A||B on the process side. If say only A>C and not B>C, it would still require that A||B, otherwise B>>C becomes blocked if A doesn’t execute (being the cause for C).

Similarly, if say only B>C and not A>C, it implies A||B, otherwise A>>C becomes blocked. Finally, an XOR-join is only possible if neither A or B cause C (unless A>C implies causes sometimes which we don’t consider at this stage). 

Q: Does A always occur before B? A. No. (PCR1)

Q: Does B always occur before A? A. No. (PCR1)

Q: Does A and B occur in parallel? A. Yes. (PCR1)

patterns unfolding from discrepancy (mediator): 

Discrepancy: (mediator)

Process: A>>M; M>>B 

Causal:  A>B

?

Process: A>>B

Causal: A>M>B;

process reasoning:

Same as above. Nothing added.

causal reasoning:

QC1: If A doesn’t execute, will B execute? A: No. (CR4)

process and causal reasoning:

QPC1: If M doesn’t execute and A executes, will B execute? A: Yes. (???)

patterns unfolding from no discrepancy (mediator): 

No Discrepancy: (mediator)

Process: A>>M; M>>B; 

Causal: A>M>B; 

process reasoning:

Same as above. Nothing added.

causal reasoning:

QC1: If M doesn’t execute, will B execute? A: No. 

QC2: If A doesn’t execute, will B execute? A: No. 

QC3: Does A cause the execution of B? A: Yes (CR2 transitive)

process and causal reasoning:

Nothing added.

LLM as a judge for faithfulness assessment (see below evaluation):

Template question: If we shorten C, will B be shortened? 

Instantiated question: If we shorten Damage assessment team inspects the damage and estimates the cost of repair in duration, will Insurance policyholder receives the payout be shortened? 

Considering the instantiated question above a concrete version of the template question where the letters are replaced with process activity descriptions, when replacing these descriptions with their corresponding letters in the template, how would you rate the similarity between the revised instantiated question and the template question (where a 1 rate means they are identical and 0 they are completely different)? In your output, print only the rate value on a 0-1 scale.

OUTPUT (Mixtral):

0.9 or 90% similarity.

Additional point for the paper:

Can LLM train itself: e.g., a certain domain is underperforming, so generate itself more Q&As?

Need arguments for why using one model to populate the questions, and the other for training? 

Are we developing a dataset such that it can be used in two ways:

Present all questions without the answers as a benchmark.

Train on say 80% of it, and use the remaining 20% to test the (improved) performance?

To elaborate on w.r.t. Evaluation of the Benchmark

Completeness - unfolding from the patterns

Correctness - of the instantiated questions. Implied from the faithful representation of the template question. use “LLM as a judge” to verify faithfulness.

Accuracy - the percentage of correct answers in the instantiated questions for the given input. In our case given correctness accuracy is 100% because the answers are derived from the template. 

Reliability - consistent across multiple tests. May also be affected by consistency of the LLM regardless of the benchmark. Also methodologically need to invoke the LLM each time ensuring no prior context is shading over the interaction.

convergent (and discriminant) validity of the instantiated items to the corresponding templates.

Another attempt at Mixtral prompt for generation of instantiated phrases/questions: 

Instruction: 

You are a helpful assistant, very precise in following instructions for text generation. 

Given a phrase describing a business process related to activities A, B and C and a question related to the phrase,  perform the following steps: 

1.choose three activities A, B, C in one of the domains of :transportation, manufacturing, retail, finance, insurance, medical (choose one domain from this list, you are also encouraged to be creative and choose other domains);

2.generate an instance of the phrase with the chosen activities which still retains the truth of the original statement

3.generate an instance of the question with the chosen activities in a form that matches the phrase instance and original question structure.

Do not return ANYTHING besides the requested output: the chosen activities, the instance of the phrase and the instance of the question. Nothing more should be returned, no accompanying text nor any explanations on the generation

Example: 

Input: Input:  Phrase: A, B, and C are activities in some process. C occurs before A. A occurs before B.  Question: Does C occur before B? 

Output:  Output:Concrete Activities:  A: Boarding the plane; B: Takeoff of the plane; C: Check-in at the airport Instantiated Phrase Statements: Check-in at the airport occurs before boarding the plane. Boarding the plane occurs before takeoff of the plane. Instantiated Question Statement: Does check-in at the airport occur before takeoff of the plane?

Test:

Input: 

Measuring the quality of the generated dataset:

Some ideas how to ensure quality of generation: we can assume we cover the range of questions in the method we generate the data (covering “completeness” metric) . We also generate based on template , so we know the correct answer - therefore if the phrase/question are coherent and stick to the template, we know the correct answer - therefore we also partially cover the “accuracy” metric (assuming the phrase/question are correct - this we can check with judge model see clause ‘c’)

when generating massive amount of examples, use Langchain Output parser to make sure the result is returned in the expected form. Filter out the wrongly structured ones.

Filter out duplicates - same activity names for example? (diversity metric)

Use a judge model (use the best there is - gpt-4o for example) for remaining examples: score each phrase/question for sticking to template, coherence and correctness. Throw away the samples which score low

Use human annotators to check the remaining samples

  Relevant metrics and approaches to measure the quality of dataset: 

https://selectstar-ai.medium.com/is-my-dataset-good-checking-the-quality-of-your-collected-data-a0087f276d9

When creating a dataset for training and benchmarking the performance of large language models (LLMs) on particular reasoning tasks, it is important to consider several standard metrics to ensure the quality and utility of your dataset. These metrics can help evaluate various aspects such as accuracy, completeness, consistency, and relevance. Here are some commonly used metrics:

Accuracy:

Correctness: Measures the proportion of correctly answered questions or tasks.

Precision: The ratio of relevant instances among the retrieved instances.

Recall: The ratio of relevant instances that have been retrieved over the total amount of relevant instances.

F1 Score: The harmonic mean of precision and recall.

Completeness:

Coverage: Ensures that the dataset comprehensively covers the range of concepts and scenarios relevant to the reasoning task.

Consistency:

Intra-annotator Agreement: The consistency of the same annotator's annotations over time.

Inter-annotator Agreement: The consistency between different annotators' annotations, commonly measured using Cohen’s Kappa or Krippendorff’s Alpha.

Relevance:

Relevance Score: How pertinent the questions and answers are to the reasoning tasks being evaluated.

Difficulty Distribution:

Ensures a balanced mix of easy, medium, and hard questions to adequately test different levels of reasoning ability.

Diversity:

Lexical Diversity: The variety of vocabulary used in the dataset.Conceptual Diversity: The range of different concepts and scenarios included.

Bias and Fairness:

Bias Detection Metrics: Identifies and measures potential biases in the dataset related to gender, race, socioeconomic status, etc.Fairness Metrics: Ensures that the model's performance does not disproportionately favor or disadvantage any particular group.

Human Judgment:

Human Evaluation Scores: Scores given by human evaluators based on criteria like fluency, relevance, and correctness.

Statistical Properties:

Distribution Analysis: Analyzes the statistical distribution of data points to ensure there is no skewness or imbalance.Entropy: Measures the amount of unpredictability or randomness in the dataset, ensuring the dataset is not overly predictable.

Usability:

Ease of Use: Evaluates how easy it is for researchers and practitioners to use the dataset, including clarity of documentation, and availability of tools for data manipulation.

For creating a high-quality dataset, you might consider these metrics in the following process:

Define Objectives: Clearly outline what reasoning tasks your dataset should benchmark.

Design Dataset: Create the dataset ensuring diversity, relevance, and proper difficulty distribution.

Annotate Data: Use multiple annotators to ensure high inter-annotator agreement.

Evaluate and Validate: Use the metrics above to continuously evaluate and validate the dataset.

Iterate and Improve: Based on feedback and metric evaluations, refine the dataset.

Applying these metrics will help you ensure that your dataset is robust, fair, and comprehensive, ultimately leading to more reliable benchmarking of LLMs on reasoning tasks.

Phrase: A causes B, B causes C, C causes D and D causes M

Question: What is the chain of events which cause

Answer: 

consider the general structure of a sentence: A is a cause for B and B is a cause for C. Instantiate this structure in a form of some phrase in the domain of transportation.

ChatGPT

Sure, here is a phrase in the domain of transportation that follows the structure:

"Traffic congestion is a cause for increased travel time, and increased travel time is a cause for higher fuel consumption."

Given A, B, C are activities in a business process, instantiate again accordingly.

ChatGPT

Certainly, here is a phrase instantiating the given structure in the context of a business process:

"Delays in order processing are a cause for late shipments, and late shipments are a cause for customer dissatisfaction."

can you rephrase this sentence in 10 different forms while keeping the inner structure intact.

ChatGPT

Sure, here are ten different rephrasings of the sentence while maintaining the inner structure:

"Slow order processing leads to delayed shipments, and delayed shipments result in customer dissatisfaction."

"Order processing delays cause shipment delays, and shipment delays cause customer dissatisfaction."

"Processing orders slowly causes late deliveries, and late deliveries lead to unhappy customers."

"Delays in processing orders result in late shipments, and late shipments cause customers to be dissatisfied."

"Inefficient order processing results in shipment delays, and shipment delays result in dissatisfied customers."

"Delays in the order processing stage lead to delays in shipping, and delays in shipping lead to customer dissatisfaction."

"If order processing is delayed, it causes delayed shipments, which in turn cause customer dissatisfaction."

"Order processing slowdowns cause shipment delays, and shipment delays lead to customer dissatisfaction."

"When order processing is slow, it leads to late shipments, which in turn leads to customer dissatisfaction."

"Order processing delays lead to shipping delays, and shipping delays result in dissatisfied customers."

phrase: "Order processing delays cause shipment delays, and shipment delays cause customer dissatisfaction." Question: "what is the root cause for customer dissatisfaction?"

ChatGPT

Phrase: "Order processing delays cause shipment delays, and shipment delays cause customer dissatisfaction."

Question: "What is the root cause of customer dissatisfaction?"

phrase: "Order processing delays cause shipment delays, and shipment delays cause customer dissatisfaction." Question: "what is the root cause for customer dissatisfaction?" Answer:

ChatGPT

Phrase: "Order processing delays cause shipment delays, and shipment delays cause customer dissatisfaction."

Question: "What is the root cause for customer dissatisfaction?"

Answer: "The root cause for customer dissatisfaction is order processing delays."

phrase: "Order processing delays cause shipment delays, and shipment delays cause customer dissatisfaction." Question: "what is the direct cause for customer dissatisfaction?" Answer:

ChatGPT

Phrase: "Order processing delays cause shipment delays, and shipment delays cause customer dissatisfaction."

Question: "What is the direct cause for customer dissatisfaction?"

Answer: "The direct cause for customer dissatisfaction is shipment delays."

Fact one: Flight EL823 was late at the gate. Fact two: Passengers' boarding on flight EL824, which is the subsequent flight, was delayed. Fact three: EL824 departure was delayed. Was the delay in EL824 departure caused by the late arrival of Flight EL823 at the gate?

