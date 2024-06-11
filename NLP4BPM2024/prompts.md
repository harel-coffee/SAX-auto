# P1: LLM as a judge for faithfulness assessment

## INPUT:
**Template question:**
If we shorten C, will B be shortened?

**Instantiated question:**
If we shorten Damage assessment team inspects the damage and estimates the cost of repair in duration, will Insurance policyholder receives the payout be shortened? 

**Instruction:**
Considering the instantiated question above a concrete version of the template question where the letters are replaced with process activity descriptions, when replacing these descriptions with their corresponding letters in the template, how would you rate the similarity between the revised instantiated question and the template question (where a 1 rate means they are identical and 0 they are completely different)? In your output, print only the rate value on a 0-1 scale.

## OUTPUT (Mixtral):
0.9 or 90% similarity.
