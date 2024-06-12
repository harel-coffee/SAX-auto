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
* CR1: $\lnot (A\xrightarrow{C}C) \Leftarrow C\xrightarrow{C}A$ (no symmetry inference)
* CR2: $A\xrightarrow{C}C \Leftarrow (A\xrightarrow{C}B) \land (B\xrightarrow{C}C)$ (transitive inference) [relevant only in the mediator pattern]
* CR3: $A\xleftarrow{C}B \Leftarrow B\xrightarrow{C}A$ (cause vs because as $\xleftarrow{C}$) 
* CR4: $\lnot B \Leftarrow (A\xrightarrow{C}B) \land \lnot A$ [similarly $A \Leftarrow (A\xrightarrow{C}B) \land B$](entailed from the meaning of $\xrightarrow{C}$)

#### Combined:
* PCR1: $A\rightarrow B \Leftarrow A\xrightarrow{C}B$ (i.e., IF (A causes B)=TRUE THEN (A precedes B)=TRUE)
* PCR2: $\lnot (B\xrightarrow{C}A) \Leftarrow A\rightarrow B$ (i.e., IF (A precedes B)=TRUE THEN (B causes A)=FALSE)

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
* QC1: Does B cause the execution of A? A: No (CR1)
* QC2: Does C cause the execution of A? A: No (CR1)
* QC3: Does B execute because of A? A: Yes (CR3)
* QC4: Does C execute because of A? A: Yes (CR3)
* QC5: If A doesn’t execute, will B ever execute? A: No (CR4)
* QC6: If A doesn’t execute, will C ever execute? A: No (CR4)

#### Combined:
* QPC1: Does B cause the execution of C? A: No (because we don’t know according to close world assumption)
* QPC2: Does C cause the execution of B? A: No (because we don’t know, and $B\rightarrow C$ implies $\lnot(C\xrightarrow{C}B) $)

## Situation 3: Collider with no discrepancy
* Process: $A\rightarrow C, B\rightarrow C$ (join)
* Causal: $A\xrightarrow{C}C, B\xrightarrow{C}C$

### Situation Phrases $\mathcal{S}_3$
* A, B, and C are activities in some process.
#### Process: 
* A occurs before C. B occurs before C.
#### Causal: 
* A causes the execution of C. B causes the execution of C.

### Rules $\mathcal{R}_3$
Same as in $\mathcal{R}_1$ and $\mathcal{R}_2$.
#### Combined: (possible extension if we add $||$ support in process)
* PCR1: $A||B \Leftarrow (A\rightarrow C) \land (B\rightarrow C) \land ((A\xrightarrow{C}C) \lor (B\xrightarrow{C}C))$ [added if we extend to support || in the process, forces a AND-join similar to forcing AND-split in the confounder case for the non discrepancy cases]
>* If we know that both $A\xrightarrow{C}C$ and $B\xrightarrow{C}C$, it may imply that $A||B$ on the process side.
>* If only $A\xrightarrow{C}C$ and not $B\xrightarrow{C}C$, it would still require that $A||B$, otherwise $B\rightarrow C$ becomes blocked if $A$ doesn’t execute (being the cause for $C$).
>* Similarly, if only $B\xrightarrow{C}C$ and $\lnot (A\xrightarrow{C}C)$, it implies $A||B$, otherwise $A\rightarrow C$ becomes blocked.
>* Finally, an XOR-join is only possible if neither $A$ or $B$ cause $C$ (unless $A\xrightarrow{C}C$ implies causes sometimes which we don’t consider at this stage). 

### Questions $\mathcal{Q}_3$
#### Process:
* QP1: Does A occur before B? A. No. (provided close world assumption, may be different if we also know that $A$# $B$ or that $A||B$ when using more expressive process notation, distinguishing between XOR-join and AND-join).
* QP2: Does B occur before A? A. No (Similarly in the opposite direction, same argumentation).

#### Causal:
None added.

#### Combined: (w.r.t possible extension if we add $||$ support in process)
* QPC1: Does A always occur before B? A. No. (PCR1)
* QPC2: Does B always occur before A? A. No. (PCR1)
* QPC3: Does A and B occur in parallel? A. Yes. (PCR1)

## Situation 4: Collider with discrepancy
* Process: $A\rightarrow B\rightarrow C$ (or $B\rightarrow A\rightarrow C$)
* Causal: $A\xrightarrow{C}C, B\xrightarrow{C}C$

### Situation Phrases $\mathcal{S}_4$
* A, B, and C are activities in some process.
#### Process: 
* A occurs before B. B occurs before C.
#### Causal: 
* A causes the execution of C. B causes the execution of C.

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

## Situation 5: Mediator
* P: A>B; B>C
* C: A>B; B>C

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
