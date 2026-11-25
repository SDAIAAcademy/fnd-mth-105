---
course: "Discrete Mathematics and Logic for Computing"
code: "FND-MTH-105"
version: "2027.1.0"
deck: "week3"
day: 3
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-mth-105/slides/week3.html"
---

# Discrete Mathematics and Logic for Computing

## Week 3: Predicates, quantifiers and first proofs

Properties of relations stated with quantifiers, checked on data, then proved or refuted

#### [week3#title] Predicates, quantifiers and first proofs

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 3: Properties of relations stated with quantifiers, checked on data, then proved or refuted

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week3#agenda] Predicates, quantifiers and first proofs

*This week*

- **Session 1 · Quantifiers, relations and first proofs**: Predicates and quantifiers, the properties of relations, equivalence relations and orders, and direct proof, counterexample and contradiction

#### [week3#review-week2] Valid or not?

*Review · week 2*

**Question:** Rule: if a meter reading is missing, the bill is estimated. This bill is not estimated. What follows?

- A. The reading is not missing
- B. The reading is missing
- C. Nothing: the rule says nothing about estimated bills
- D. The bill would be estimated if the reading were present

### Session 1: Quantifiers, relations and first proofs

#### [week3#s1] Quantifiers, relations and first proofs

*Session 1*

- Write a relation property or a data-quality rule with quantifiers and negate it correctly
- Classify a relation as a function, an equivalence, a partial order or none, with a counterexample for each property it lacks
- Prove a short claim directly or by contradiction, and refute a false one with a counterexample

#### [week3#predicates] A predicate becomes true or false once you fill its variable

*Block A · quantifiers*

- **P(x)**: "x is overdue", over a domain such as the loans of a library
- **∀x P(x)**: every loan is overdue
- **∃x P(x)**: at least one loan is overdue
- The **domain** is part of the claim: change it and the truth can change

```python
# file: python
all(overdue(x) for x in loans)   # for every
any(overdue(x) for x in loans)   # there exists
```

#### [week3#quality-rules] A data-quality rule is a quantified statement your code can evaluate

*Data-quality rules*

| Rule in words | In logic |
| --- | --- |
| Every loan belongs to a member | ∀l ∃m: holder(l, m) |
| No member holds more than five loans | ∀m: count of l with holder(l, m) ≤ 5 |
| Every child member has a guardian on file | ∀m: child(m) → guardian(m) |

> **A failed rule** comes with a witness: the loan with no member, the child with no guardian. Print the witness, not only "False".

#### [week3#negation] Negating a quantifier swaps it and moves the "not" inside

*Negation*

| Statement | Its negation |
| --- | --- |
| ∀x P(x): every loan is returned | ∃x ¬P(x): some loan is not returned |
| ∃x P(x): some book is damaged | ∀x ¬P(x): no book is damaged |
| ∀x ∃y R(x, y): every member has a card | ∃x ∀y ¬R(x, y): some member has no card at all |

> **Order matters.** ∀x ∃y "every member has a card" is not ∃y ∀x "one card belongs to every member".

#### [week3#check-negation] What is the negation?

*Checkpoint*

**Question:** The claim: "every course has at least one tutor". Which statement is its negation?

- A. Every course has no tutor
- B. Some course has at least one tutor
- C. Some course has no tutor
- D. One tutor teaches no course

#### [week3#properties-quantified] Each property of a relation is a "for every" statement

*Block B · relation properties*

| Property | Statement | A counterexample is |
| --- | --- | --- |
| Reflexive | ∀x: x R x | one x not related to itself |
| Symmetric | ∀x, y: x R y → y R x | one pair related one way only |
| Antisymmetric | ∀x, y: x R y ∧ y R x → x = y | two different elements related both ways |
| Transitive | ∀x, y, z: x R y ∧ y R z → x R z | one chain x, y, z with x not related to z |

#### [week3#classify] The properties decide what a relation can be used for

*Kinds of relation*

| Kind | Properties | Example |
| --- | --- | --- |
| Equivalence | refl, sym, trans | born in the same month |
| Partial order | refl, anti, trans | is a subset of |
| Strict order | irrefl, anti, trans | finished earlier than |
| Preorder | refl, trans | is at least as tall as |

- Group with an **equivalence**
- Rank or schedule with an **order**
- A preorder ranks with ties between different elements

#### [week3#finite-is-proof] On a finite relation, checking every case is a proof

*Testing or proving*

- **Finite: check them all.** "Same month" on 40 people: 1,600 pairs and 64,000 triples. Checking them all proves the property for those 40.
- **Infinite: test, then prove.** "Subset of" on all sets, "divides" on all integers: no loop ends. Tests can refute; only an argument proves.

> **Mind the definition.** If a relation is defined by a rule ("within 5 km"), a property may fail for the next element even when it holds for today's data.

#### [week3#check-classify] Can it be used to form groups?

*Checkpoint*

**Question:** A delivery firm relates two depots when they are within 5 km of each other, and wants to form groups of "nearby" depots with it. What is this relation?

- A. An equivalence relation, so the groups are well defined
- B. Reflexive and symmetric, not transitive, so not an equivalence
- C. A partial order on the depots
- D. Symmetric only, as no depot relates to itself

#### [week3#direct-proof] A direct proof goes from the hypothesis to the conclusion, one justified step at a time

*Block C · proofs*

**Claim.** The sum of two even integers is even.

1. Let a and b be even: a = 2k and b = 2l for integers k, l (definition)
2. a + b = 2k + 2l = 2(k + l) (algebra)
3. k + l is an integer, so a + b is even (definition) ∎

- **The shape.** State the claim with its domain. Unfold the definitions. Calculate. Fold back into the definition of the conclusion. Name each reason.

#### [week3#counterexample] One counterexample refutes a "for every" claim

*Refuting*

| Claim | Counterexample |
| --- | --- |
| Every prime is odd | 2 |
| If a² = b² then a = b, for integers | a = 3, b = −3 |
| n² − n + 11 is prime for every n ≥ 1 | n = 11: 121 = 11 · 11 |

The last claim holds for n = 1 to 10. Code finds the counterexample in a moment; a person checking by hand may stop too early.

#### [week3#contradiction] A proof by contradiction assumes the opposite and reaches something impossible

*Contradiction*

**Claim.** If n² is even, then n is even (n an integer).

1. Suppose n² is even and n is odd: n = 2k + 1
2. n² = 4k² + 4k + 1 = 2(2k² + 2k) + 1, which is odd
3. n² is both even and odd: impossible. So n is even ∎

- **Say what you assumed.** The first line names the assumption; the last names the contradiction. A reader can then check that the assumption really is the negation of the claim.

#### [week3#check-method] What settles the claim?

*Checkpoint*

**Question:** An analyst claims: "for every integer n, n² + n is even". Her code checks n from −1,000 to 1,000 and finds no failure. What has she shown?

- A. That the claim is true, since 2,001 cases passed
- B. Nothing: tests are no evidence either way
- C. That the claim is false for some large n
- D. No counterexample in that range; a proof is still needed

#### [week3#lab-3-1] Relation properties checked in code

Lab 3.1 · 105 min

Write checkers for reflexive, symmetric, antisymmetric and transitive, classify nine relations from the centre's data and software, find the planted faults, and close the training prerequisites.

[W3_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W3_1.ipynb)

- [ ] Set up; properties as quantified statements (10 min)
- [ ] Write the property checkers (20 min)
- [ ] Classify nine relations (20 min)
- [ ] Counterexamples: the planted faults (15 min)
- [ ] Equivalence classes and the partition (10 min)
- [ ] Transitive closure of the training prerequisites (15 min)
- [ ] A claim over all integers: test, then prove (10 min)
- [ ] Record what the checks prove and what they only test (5 min)
- [ ] ✱ Stretch: Count, among the 512 relations on a three-element set, how many are equivalence relations

#### [week3#debrief-relations] One relation fails by meaning, one by data, and one order is the wrong order

*Debrief · lab 3.1*

| Relation | Verdict |
| --- | --- |
| Same district | equivalence: 11 classes |
| Born within a year of | not transitive: 144 and 350 days apart, but 494 |
| Lead can cover for lead | not symmetric: TL-04 covers TL-09, not back |
| Has at least the skills of | preorder: ties between different people |
| Release text at most | an order that puts 10.0.0 first |

- Prerequisites: 9 direct pairs, 21 after closure; T8 needs T1 to T7
- "Divides" passed every triple up to 60; the proof covers the rest

#### [week3#wrap-up] Three things to keep

*Week 3 · wrap-up*

- **Negate carefully.** Swap ∀ and ∃ and move the "not" inside. The negation tells you what a counterexample looks like.
- **Properties decide use.** Group only with an equivalence; rank only with an order. Check before you use.
- **Finite or infinite.** Every case checked is a proof for a finite set. For the integers, tests refute and proofs prove.

#### [week3#next] Week 4: Induction, invariants and the limits of testing

*Next*

Problem set 3 (60 minutes, AI off for the first attempt): labs/problem-sets/PS3.ipynb. The first supervised test follows week 4.
