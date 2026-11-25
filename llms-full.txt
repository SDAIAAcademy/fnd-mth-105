---
course: "Discrete Mathematics and Logic for Computing"
code: "FND-MTH-105"
version: "2027.1.0"
scope: "course"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-mth-105/"
---

# Discrete Mathematics and Logic for Computing

Test a claim in code, then prove it: sets, relations, logic, induction, counting and graphs, applied to joins, rules, collisions, re-identification and pipelines

Participants practise the discrete mathematics and proof that computing degrees assume: sets, relations, logic, proof, counting and graphs. Code tests each claim on generated cases before it is proved, so the gap between testing and proof is visible. Labs link relations to joins, logic to rule checking, counting to collision and re-identification risk, and graphs to pipeline dependencies. Algorithms on graphs follow in FND-PRG-103.

- **Audience:** Beginners. Career changers and non-computing graduates closing bridging gaps before advanced study, and computing graduates refreshing the mathematics behind models; a placement test lets participants skip any course whose content they already command.
- **Prerequisites:** School algebra; Writes short Python programs with lists, loops, functions and recursion (FND-PRG-101 or equivalent)
- **Case study:** The community volunteer centre (fictional): An unnamed non-profit in one unnamed city registers 4,000 volunteers, trains them and staffs community events in twelve postal districts; its analyst checks joins, access rules, a shift schedule, check-in codes, a de-identified extract and a nightly pipeline. All data is synthetic, generated with a fixed seed; people appear only as codes such as V-00412, never by name.

## Outcomes

- LO1 (Awareness): Identify whether a relation is a function, an equivalence or an order, and which properties it has, given twelve relations from data and software
- LO2 (Awareness): Distinguish valid from invalid arguments and translate plain-language rules into propositional and predicate logic, given five access and data-quality rules
- LO3 (Awareness): Describe direct, contradiction and induction proofs and identify the gap in a flawed proof, given six short proofs, two with planted errors
- LO4 (Applied): Apply induction and loop invariants to prove simple claims about integers, sets and recursive code, given claims first tested in code
- LO5 (Applied): Compute counts of arrangements, selections and collisions and verify them by enumeration, given hashing and record-linkage problems
- LO6 (Applied): Use a graph model of dependencies to find cycles and compute a topological order, given a pipeline graph with a planted cycle

## Week 1: Sets, functions and relations

Data as sets of tuples, maps that are or are not functions, and joins as composition

#### [week1#title] Sets, functions and relations

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 1: Data as sets of tuples, maps that are or are not functions, and joins as composition

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week1#agenda] Sets, functions and relations

*This week*

- **Session 1 · Sets, functions and relations**: Sets and Cartesian products, injective, surjective and bijective functions, relations and their first properties, and joins as relation composition

#### [week1#test-then-prove] Every claim is tested in code first, then proved

*Seven weeks*

- **Test.** Run the claim on generated cases, or on every case when there are few. A failure is a counterexample.
- **Prove.** An argument that covers every case, including the ones no test reached.
- **Mind the gap.** A thousand passing tests prove nothing about the next case. Week 4 shows a claim that fails on its forty-first.

| Assessed work | Weight |
| --- | --- |
| Weekly problem sets | 20% |
| Two supervised AI-off tests of proofs and short problems | 40% |
| Capstone portfolio, rubric-scored | 30% |
| Oral defence | 10% |

#### [week1#setup-check] One command proves your setup

*Setup check*

From the course folder, in a terminal:

```bash
# file: terminal
cd labs
uv run python -c "import pysat, networkx; print('ready')"
```

"ready" means you can run every lab. In a free hosted notebook, the first cell of each lab installs what it needs.

- **What the course assumes.** School algebra, and Python with lists, loops, functions and recursion (FND-PRG-101 or equivalent). Nothing of FND-PRG-101 is taught again.

#### [week1#the-centre] All seven weeks work on one community volunteer centre

*The case*

- A non-profit in one city: **4,000 volunteers** in twelve postal districts, PD-01 to PD-12
- It trains them, staffs **30 events** a month and runs a nightly data pipeline
- You are its new data analyst; you work with the volunteer coordinator, the data protection officer and the operations lead

- **Synthetic, and coded.** Every record is generated with a fixed seed. People appear only as codes such as V-00412: no names, no phone numbers, no real identifiers.

### Session 1: Sets, functions and relations

#### [week1#s1] Sets, functions and relations

*Session 1*

- Compute set operations and the size of a Cartesian product, and check them in code
- Decide whether a map from the data is a function and whether it is injective, surjective or bijective
- Compose two relations and explain how a database join differs from the composition

#### [week1#sets-are-tables] A set has no order and no repeats, and a table of distinct rows is one

*Block A · sets*

- {2, 3, 5} = {5, 3, 2} = {2, 2, 3, 5}: order and repeats do not count
- **x ∈ A** reads "x is a member of A"; **A ⊆ B**, every member of A is in B
- A row of a table is a **tuple**: (T3, room 2) is not (room 2, T3)
- A table with no duplicate rows is a set of tuples

```python
# file: python
A = {2, 3, 5}
B = {5, 7}
A | B, A & B, A - B
# {2, 3, 5, 7}, {5}, {2, 3}
```

#### [week1#set-algebra] Union, intersection and difference answer the coordinator's first questions

*Operations*

| Question | Operation | Example: X = {a, b, c}, Y = {b, d} |
| --- | --- | --- |
| Worked at either site | X ∪ Y | {a, b, c, d} |
| Worked at both | X ∩ Y | {b} |
| Only at the first | X − Y | {a, c} |
| How many at either | \|X ∪ Y\| = \|X\| + \|Y\| − \|X ∩ Y\| | 3 + 2 − 1 = 4 |

The last line is inclusion-exclusion for two sets. Week 6 uses it on a whole register.

#### [week1#cartesian] A Cartesian product holds every pair, and its size is the product of the sizes

*Products*

{T1, T2} × {room 1, room 2, room 3} =

{(T1, room 1), (T1, room 2), (T1, room 3), (T2, room 1), (T2, room 2), (T2, room 3)}

**|A × B| = |A| · |B| = 2 · 3 = 6**

- **A relation is a subset of a product.** Any set of pairs from A × B is a relation from A to B. With 6 pairs there are 2⁶ = 64 relations, from the empty one to all of A × B.

#### [week1#check-sets] How many pairs?

*Checkpoint*

**Question:** A training team lists 8 modules and 5 rooms. It wants one row for every module and room that could be booked together. How many rows does that table have?

- A. 13
- B. 40
- C. 2 to the power 40
- D. 80

#### [week1#function-definition] A function gives every input exactly one output

*Block B · functions*

- **A function from X to Y.** A relation in which each x in X appears in exactly one pair. X is the domain, Y the codomain.
- **Two ways to fail.** Some x has no output (the map is partial), or some x has two outputs (the map is not single-valued).

| Module | Room | Verdict |
| --- | --- | --- |
| T1 | room 1 | fine |
| T2 | room 1, room 3 | two outputs: not a function |
| T3 | (none) | no output: partial |

#### [week1#three-kinds] Injective, surjective and bijective say how outputs are shared and covered

*Three properties*

- **Injective.** No two inputs share an output. Test: f(x) = f(x′) forces x = x′.
- **Surjective.** Every element of the codomain is reached by some input.
- **Bijective.** Both: a perfect pairing, so the map has an inverse.

> **On the integers.** n ↦ 3n is injective and not surjective (5 is never reached); n ↦ n − 7 is a bijection.

#### [week1#why-functions-matter] Each property is a promise a system relies on

*In data work*

| Property | Where a system relies on it |
| --- | --- |
| Function (total) | Every record finds its value in a lookup |
| Injective | A key or a code identifies one record: no two people check in as one |
| Surjective | Every category is used: every event has staff |
| Bijective | A code can be swapped back for the record: pseudonymisation, week 6 |

#### [week1#check-functions] What kind of map is this?

*Checkpoint*

**Question:** A sports hall gives each of its 120 lockers to one of 4 cleaning rounds, every round gets 30 lockers. As a map from lockers to rounds, which is true?

- A. A bijection, since every round gets the same number
- B. Not a function, since each round has many lockers
- C. Injective, since every round is used
- D. A surjective function that is not injective

#### [week1#relations-and-properties] Equivalences group things; orders rank them

*Block C · relations*

- **Equivalence relation.** Reflexive, symmetric and transitive. "Lives in the same district as" splits people into groups, the **equivalence classes**.
- **Partial order.** Reflexive, antisymmetric and transitive. "Must be taken before, directly or through others, or is the same module as" ranks modules; some pairs are not comparable.

- Reflexive: every x relates to itself. Symmetric: x R y gives y R x
- Transitive: x R y and y R z give x R z. Antisymmetric: x R y and y R x give x = y

#### [week1#composition] Composing two relations follows one, then the other

*Composition*

1. **R: module → room** (T1, r1), (T2, r1), (T3, r2)
2. **S: room → building** (r1, North), (r2, South), (r2, Annex)
3. **R then S** (T1, North), (T2, North), (T3, South), (T3, Annex)

(x, z) is in the composition when **some** y has (x, y) in R and (y, z) in S.

#### [week1#join-is-composition] A join is a composition that keeps repeats

*In a database*

```sql
-- file: sql
select r.module, s.building
from R r join S s on r.room = s.room
```

- One output row per **pair of matching rows**
- If T2 used room 1 twice (two bookings), (T2, North) appears twice
- `select distinct` returns the composition, a set

> **What goes wrong.** Counting join rows as "modules per building" overcounts by every repeat. The lab measures how many.

#### [week1#check-composition] Join rows or composition pairs?

*Checkpoint*

**Question:** A library joins loans (reader, copy) with copies (copy, title). One reader borrowed two copies of the same title. Compared with the composition "reader borrowed title", the join returns:

- A. the same number of rows as there are pairs
- B. one fewer row, as the second copy is dropped
- C. one more row: the (reader, title) pair appears twice
- D. an error, as the key repeats

#### [week1#lab-1-1] Sets, functions and joins in code

Lab 1.1 · 90 min

An added lab, beyond the entry's five: test the badge map for the properties of a function, and compare composing two tables with joining them in SQL.

[W1_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W1_1.ipynb)

- [ ] Set up and load the centre's tables (10 min)
- [ ] Set operations and Cartesian products, by hand and in code (10 min)
- [ ] Is the badge map a function? Total, injective, surjective (20 min)
- [ ] Shift to event: a function onto the events? (10 min)
- [ ] Inverse and composition of relations (15 min)
- [ ] Compose assignments with shifts, then join them in SQL (20 min)
- [ ] Record what the coordinator should fix (5 min)
- [ ] ✱ Stretch: Show on the three tables that composing relations is associative

#### [week1#debrief-badges] The badge map fails all three tests, and the join overcounts by eight

*Debrief · lab 1.1*

| Check | Result |
| --- | --- |
| Function on the 300 volunteers | no: V-00117 and V-00242 have no badge |
| Injective | no: BD-0059, BD-0420, BD-0909 issued twice |
| Shift to event | a function onto the 30 events, 3 shifts each |
| Join rows against composition | 600 rows, 592 distinct pairs |

- V-00117 is also on a shift: fix before the event
- Eight volunteers work two shifts of one event
- Count events per volunteer with distinct pairs

#### [week1#wrap-up] Three things to keep

*Week 1 · wrap-up*

- **Tables are sets of tuples.** Products count the possible rows; relations are subsets of them.
- **Functions make promises.** Total, single-valued, injective, surjective: check each one; data breaks them quietly.
- **Joins compose relations.** With repeats. Distinct pairs are the composition.

#### [week1#next] Week 2: Logic: truth tables and satisfiability

*Next*

Problem set 1 (60 minutes, AI off for the first attempt): labs/problem-sets/PS1.ipynb. Unfinished labs can be finished at home.

## Week 2: Logic: truth tables and satisfiability

Rules as formulas, arguments checked row by row, and a schedule found by a solver

#### [week2#title] Logic: truth tables and satisfiability

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 2: Rules as formulas, arguments checked row by row, and a schedule found by a solver

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week2#agenda] Logic: truth tables and satisfiability

*This week*

- **Session 1 · Propositional logic, normal forms and SAT**: Propositional logic and truth tables, valid and invalid arguments, conjunctive normal form and Boolean satisfiability with a solver

#### [week2#review-week1] Can the code be swapped back?

*Review · week 1*

**Question:** A school replaces each of its 500 pupil numbers with a random code from 1,000 possible codes, never giving one code twice. As a map from pupils to the 1,000 codes, what is it?

- A. A bijection
- B. Injective, not surjective
- C. Surjective, not injective
- D. Not a function

### Session 1: Propositional logic, normal forms and SAT

#### [week2#s1] Propositional logic, normal forms and SAT

*Session 1*

- Translate a plain-language rule into a propositional formula and check it by truth table
- Distinguish a valid argument from an invalid one by searching for a counterexample row
- Encode a small scheduling problem in conjunctive normal form and solve it with a SAT solver

#### [week2#propositions] A proposition is true or false, and connectives build bigger ones

*Block A · propositions*

| Symbol | Reads | True when |
| --- | --- | --- |
| ¬p | not p | p is false |
| p ∧ q | p and q | both are true |
| p ∨ q | p or q | at least one is true |
| p → q | if p then q | p is false, or q is true |
| p ↔ q | p if and only if q | both have the same value |

#### [week2#implication] "If p then q" is broken only by p true and q false

*Implication*

| p: over 20 kg | q: two lifters | p → q |
| --- | --- | --- |
| F | F | T |
| F | T | T |
| T | F | F |
| T | T | T |

- A light parcel lifted by two people does not break the rule
- A light parcel makes the rule true whatever happens: **vacuously**
- Only a heavy parcel lifted alone breaks it

#### [week2#truth-table-code] A truth table is a loop over every row of truth values

*In code*

```python
# file: python
import itertools

def implies(a, b):
    return (not a) or b

for p, q in itertools.product([False, True], repeat=2):
    print(p, q, implies(p, q))
```

- n variables give **2ⁿ rows**: 4 for two, 1,024 for ten
- Checking every row is a proof for a finite claim
- For 50 variables, 2⁵⁰ rows is out of reach: that is where a solver comes in

#### [week2#equivalence-laws] Two formulas are equivalent when they agree on every row

*Equivalence*

| Law | Equivalent pair |
| --- | --- |
| De Morgan | ¬(p ∧ q) and ¬p ∨ ¬q; ¬(p ∨ q) and ¬p ∧ ¬q |
| Contrapositive | p → q and ¬q → ¬p |
| Implication as or | p → q and ¬p ∨ q |
| Distribution | p ∧ (q ∨ r) and (p ∧ q) ∨ (p ∧ r) |

> **Not a law.** The converse q → p is a different rule: a parcel lifted by two people need not be heavy.

#### [week2#check-converse] Which sentence says the same thing?

*Checkpoint*

**Question:** A warehouse rule: "If a box is fragile, it is packed with foam." Which sentence is equivalent to it?

- A. If a box is packed with foam, it is fragile
- B. If a box is not fragile, it is not packed with foam
- C. Every box is fragile and packed with foam
- D. If a box is not packed with foam, it is not fragile

#### [week2#validity] An argument is valid when no row makes the premises true and the conclusion false

*Block B · arguments*

| Form | Premises | Conclusion | Verdict |
| --- | --- | --- | --- |
| Modus ponens | p → q, p | q | valid |
| Modus tollens | p → q, ¬q | ¬p | valid |
| Affirming the consequent | p → q, q | p | invalid: row p F, q T |
| Denying the antecedent | p → q, ¬p | ¬q | invalid: row p F, q T |

Validity is about form, not truth: a valid argument from a false premise can reach a false conclusion.

#### [week2#translating-rules] Words like "only if" and "unless" fix the direction of the arrow

*Rules in words*

| Words | Formula |
| --- | --- |
| p if q | q → p |
| p only if q | p → q |
| p unless q | ¬q → p, the same as p ∨ q |
| A or B and C | ambiguous: (A ∨ B) ∧ C, or A ∨ (B ∧ C) |

> **Habit.** Name each variable in one line, write the formula with brackets, then read it back in words.

#### [week2#check-only-if] Translate the rule

*Checkpoint*

**Question:** A laboratory: "A visitor may enter only if they wear goggles." With p = "the visitor enters" and s = "the visitor wears goggles", which formula is the rule?

- A. s → p
- B. p → s
- C. p ∧ s
- D. p ↔ s

#### [week2#cnf] Conjunctive normal form is an "and" of clauses, each an "or" of literals

*Block C · normal form*

(a ∨ b) ∧ (¬a ∨ c) ∧ (¬b ∨ ¬c)

- A **literal** is a variable or its negation
- A **clause** is an or of literals: at least one must hold
- Every formula has an equivalent CNF: one clause per row it must exclude

- **For a solver.** Variables are numbers and a clause is a list: [1, 2], [-1, 3], [-2, -3]. A minus sign is "not".

#### [week2#sat] A SAT solver finds a row that makes every clause true, or proves there is none

*Satisfiability*

1. **Encode** one variable per yes-or-no decision; one clause per rule
2. **Solve** a model: a value for every variable, or "unsatisfiable"
3. **Check** the model against the rules in words, with separate code

- Checking a proposed assignment is quick; finding one can take exponential time in the worst case with every known method
- "Unsatisfiable" is a proof that no assignment works; a solver can name a small set of rules that already conflict

#### [week2#encoding-counts] "Exactly one" and "at most two" become many small clauses

*Encoding*

| Rule over n yes-or-no variables | Clauses | For n = 8 |
| --- | --- | --- |
| At least one | 1 clause of n literals | 1 |
| At most one: no two together | one per pair, n(n − 1)/2 | 28 |
| At most two: no three together | one per triple, n(n − 1)(n − 2)/6 | 56 |
| At least two: someone besides each one | n clauses of n − 1 literals | 8 |

#### [week2#check-unsat] What does "unsatisfiable" tell the planner?

*Checkpoint*

**Question:** A clinic encodes its nurse rota and the solver answers "unsatisfiable". What has been established?

- A. The solver failed and should be run again with more time
- B. No rota was found among those the solver tried
- C. No rota meets all the clauses as written
- D. No rota meets the clinic's real rules

#### [week2#lab-2-1] Truth tables in code, and a scheduling puzzle solved with a SAT solver

Lab 2.1 · 105 min

Check laws and arguments by truth table, repair an access rule, and schedule ten volunteers with a solver.

[W2_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W2_1.ipynb)

- [ ] Set up; a truth table by hand and in code (15 min)
- [ ] Equivalent or not: laws by truth table (15 min)
- [ ] Valid and invalid arguments (15 min)
- [ ] Two phrasings of an access rule (15 min)
- [ ] Encode the shift puzzle in CNF (20 min)
- [ ] Solve, then check against every rule (10 min)
- [ ] The late change: unsatisfiable, and why (10 min)
- [ ] Small variant: brute force against solver (5 min)
- [ ] ✱ Stretch: Count every schedule of the full puzzle by blocking each one found

#### [week2#debrief-rules] The handbook opens contact details to anyone, for consenting volunteers

*Debrief · lab 2.1*

| Result | Value |
| --- | --- |
| Rows where the two phrasings differ | 2 of 16: o F, c F, s T |
| Shift puzzle | 50 variables, 800 clauses, a schedule found and checked |
| After the late change | unsatisfiable: one first-aider for SH-C and SH-D |
| Small variant | 36 schedules by brute force, by solver and by 3! · 3! |

- Fix the handbook with brackets: o ∨ (c ∧ (d ∨ s))
- The solver's core named the two first-aid rules
- Keeping V-00090 on SH-D, or dropping first aid on one shift, restores a schedule

#### [week2#wrap-up] Three things to keep

*Week 2 · wrap-up*

- **Only one row breaks "if".** p true and q false. The converse is a different rule.
- **Validity is a row search.** Look for premises true and conclusion false. None found in every row: valid.
- **Encode, solve, check.** A solver meets the clauses you wrote. Check its answer against the words.

#### [week2#next] Week 3: Predicates, quantifiers and first proofs

*Next*

Problem set 2 (60 minutes, AI off for the first attempt): labs/problem-sets/PS2.ipynb.

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

## Week 4: Induction, invariants and the limits of testing

Claims that pass every test you ran, and the proofs that cover the cases you did not

#### [week4#title] Induction, invariants and the limits of testing

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 4: Claims that pass every test you ran, and the proofs that cover the cases you did not

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week4#agenda] Induction, invariants and the limits of testing

*This week*

- **Session 1 · Induction, invariants, testing and proof**: Mathematical and structural induction, loop invariants, and why a claim tested on many cases is not proved

#### [week4#review-week3] Which property fails?

*Review · week 3*

**Question:** On the files of a shared drive, "file A is in the same folder as file B or in one of its subfolders" relates A to B. Which property does it lack?

- A. Reflexivity
- B. Transitivity
- C. It has all four, so it is an equivalence
- D. Symmetry

### Session 1: Induction, invariants, testing and proof

#### [week4#s1] Induction, invariants, testing and proof

*Session 1*

- Prove a claim about the integers by mathematical induction after testing it in code
- Prove a property of a recursive structure by structural induction
- State and check a loop invariant, and use it to prove a loop correct

#### [week4#induction-shape] Induction proves a claim for every n with two finite pieces of work

*Block A · induction*

1. **Base** show P(1), or P of the first value
2. **Hypothesis** assume P(k) for one k ≥ 1
3. **Step** show P(k + 1), using P(k)

- Base and step together reach every n: P(1), so P(2), so P(3), and so on
- Without the base, the step proves nothing; without the step, the base proves one case

#### [week4#induction-example] Test it, then prove it: 1 + 2 + … + n = n(n + 1) / 2

*Worked example*

```python
# file: python
all(sum(range(1, n + 1)) == n * (n + 1) // 2
    for n in range(1, 5001))   # True
```

1. **Base.** n = 1: 1 = 1 · 2 / 2
2. **Hypothesis.** 1 + … + k = k(k + 1) / 2
3. **Step.** 1 + … + k + (k + 1) = k(k + 1) / 2 + (k + 1) = (k + 1)(k + 2) / 2, using the hypothesis for the first k terms ∎

#### [week4#strong-induction] Strong induction may assume the claim for every value below k + 1

*Strong induction*

**Claim.** Every integer n ≥ 2 is a product of primes.

- If n is prime, it is a product of one prime
- Otherwise n = a · b with 2 ≤ a, b < n
- By the hypothesis for a and for b, both are products of primes, so n is too ∎

- **When to use it.** When the step needs a smaller case that is not k itself: a factor, half of n, a subtree. Recursive code that splits its input is proved this way.

#### [week4#check-induction-parts] What is missing?

*Checkpoint*

**Question:** A proof that "n + 1 < n for every n ≥ 1" assumes k + 1 < k and adds 1 to both sides to get k + 2 < k + 1. What is wrong with it?

- A. It has no base case, and the base case is false
- B. Adding 1 to both sides is not allowed
- C. The hypothesis assumes what it wants to prove
- D. It needs strong induction instead

#### [week4#structural] Structural induction follows the way a structure is built

*Block B · structural induction*

- **A recursive definition.** A nested list is either a number, or a list of nested lists. A tree is a node with a list of subtrees.
- **Its induction.** Prove the claim for the smallest pieces, then show that building from pieces that satisfy it gives a whole that satisfies it.

> **No n needed.** The induction is on the structure itself; each recursive call works on a smaller part.

#### [week4#structural-example] In a tree where every node has 0 or 2 children, leaves = inner nodes + 1

*Worked example*

- **Base.** A single node: 1 leaf, 0 inner nodes
- **Step.** A root with subtrees L and R that satisfy it: leaves = (inner(L) + 1) + (inner(R) + 1) = (inner(L) + inner(R) + 1) + 1
- The root is the one new inner node, so leaves = inner + 1 ∎

```python
# file: python
def leaves(t):
    if not t["children"]:
        return 1
    return sum(leaves(c) for c in t["children"])
```

#### [week4#recursion-correct] A recursive function is proved correct by induction on the size of its input

*Recursive code*

```python
# file: python
def total(xs):
    if not xs:
        return 0
    return xs[0] + total(xs[1:])
```

1. **Base.** The empty list returns 0, its sum
2. **Hypothesis.** total is right on lists of length k
3. **Step.** On length k + 1 it returns xs[0] plus the sum of the rest, by the hypothesis: the sum ∎

#### [week4#check-structural] What may the step assume?

*Checkpoint*

**Question:** To prove by structural induction that a recursive depth function on nested lists is correct, the step for a list [a, b, c] may assume:

- A. that the function is correct on [a, b, c]
- B. that it is correct on a only
- C. that it is correct on each of a, b and c
- D. that it is correct on every list of length 2

#### [week4#invariants] An invariant is true before the loop and after every pass

*Block C · loop invariants*

```python
# file: python
total, i = 0, 0
while i < len(xs):
    # invariant: total == sum(xs[:i])
    total += xs[i]
    i += 1
```

| Part | Show |
| --- | --- |
| Initialisation | true before the first pass |
| Maintenance | a pass keeps it true |
| Termination | the loop stops |
| At exit | invariant and exit condition give the result |

#### [week4#testing-vs-proof] A pattern can hold for every case you tried and still break

*The gap*

| Points on a circle | Regions |
| --- | --- |
| 1 | 1 |
| 2 | 2 |
| 3 | 4 |
| 4 | 8 |
| 5 | 16 |
| 6 | 31 |

- Join every pair of points with a chord, no three chords meeting inside
- The first five suggest 2ⁿ⁻¹; the sixth gives **31**, not 32
- A test can refute a pattern; only a proof can confirm it

#### [week4#what-tests-give] Generated tests find counterexamples cheaply, so run them before you prove

*Using tests well*

- **Many cases.** Every n up to a bound, or random inputs. Cheap evidence and a fast way to find a false claim.
- **Edge cases.** Zero, one, the empty list, equal values, the first case where a pattern could change.
- **Their limit.** Write what the tests cover: "n from 1 to 1,000, no counterexample". Never write "true".

#### [week4#check-invariant] Which statement is an invariant?

*Checkpoint*

**Question:** A loop counts the even numbers in a list: count starts at 0, i at 0; each pass adds 1 to count if xs[i] is even, then adds 1 to i. Which invariant proves it correct?

- A. count ≥ 0
- B. count equals the number of evens in the whole list
- C. count = i
- D. count equals the number of evens in xs[:i]

#### [week4#lab-4-1] Claims tested in code, then proved

Lab 4.1 · 105 min

An added lab: test claims on generated cases, prove them by induction and invariants, and find the gap in a flawed proof.

[W4_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W4_1.ipynb)

- [ ] Set up; test a sum formula on many cases (10 min)
- [ ] Prove it by induction (15 min)
- [ ] True for forty cases, false on the next (10 min)
- [ ] Structural induction on the team tree (20 min)
- [ ] Loop invariants asserted in code (20 min)
- [ ] Find the gap in a flawed proof (15 min)
- [ ] Record which claims are proved (15 min)
- [ ] ✱ Stretch: Prove an invariant for binary search over the volunteer codes

#### [week4#debrief-claims] Forty passes did not make claim B true, and one hidden assumption broke a proof

*Debrief · lab 4.1*

| Claim | Status |
| --- | --- |
| Sum of first n odd numbers is n² | tested to 1,000, proved |
| n² + n + 41 is prime | passes n = 0 to 39; at 40: 1,681 = 41 · 41 |
| Edges = nodes − 1 | team tree 25 and 24; 500 trees; proved |
| divide(a, b) | 2,000 pairs; proved from its invariant |
| 2ⁿ ≥ n² for n ≥ 1 | fails at n = 3; step needs k ≥ 3 |

- The flawed step used k² ≥ 2k + 1, false for k = 1 and 2
- Repaired: 2ⁿ ≥ n² for every n ≥ 4

#### [week4#wrap-up] Three things to keep

*Week 4 · wrap-up*

- **Base, hypothesis, step.** Say where the step uses the hypothesis. A step alone proves nothing.
- **Induction follows structure.** Integers, lists, trees and loops: the proof follows the way the thing is built.
- **Tests refute, proofs confirm.** Write what your tests cover, never "true", until the proof exists.

#### [week4#next] Week 5: Counting, collisions and the birthday problem

*Next*

Problem set 4 (60 minutes, AI off for the first attempt): labs/problem-sets/PS4.ipynb. Then the first supervised test, on weeks 1 to 4.

## Week 5: Counting, collisions and the birthday problem

Sum and product rules, arrangements and selections, and when two codes must collide

#### [week5#title] Counting, collisions and the birthday problem

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 5: Sum and product rules, arrangements and selections, and when two codes must collide

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week5#agenda] Counting, collisions and the birthday problem

*This week*

- **Session 1 · Counting arrangements and collisions**: The sum and product rules, permutations and combinations, the pigeonhole principle and collisions of short codes

#### [week5#review-week4] Where is the hypothesis used?

*Review · week 4*

**Question:** To prove 1 + 3 + 9 + … + 3ⁿ⁻¹ = (3ⁿ − 1) / 2 by induction, the step for k + 1 must:

- A. check the formula for n = k + 1 by computing both sides for k = 5
- B. assume the formula for k + 1 and simplify
- C. replace the first k terms by (3ᵏ − 1) / 2, add 3ᵏ, and simplify to (3ᵏ⁺¹ − 1) / 2
- D. test the formula for n up to 1,000

### Session 1: Counting arrangements and collisions

#### [week5#s1] Counting arrangements and collisions

*Session 1*

- Count arrangements and selections with the sum and product rules, permutations and combinations
- Compute the chance that short codes collide and verify it by exact enumeration
- Use the pigeonhole principle to show when a collision is certain

#### [week5#sum-product] Multiply for "and then", add for "either, or"

*Block A · two rules*

- **Product rule.** A plate of 3 letters then 4 digits: 26 · 26 · 26 · 10 · 10 · 10 · 10 = 175,760,000 plates.
- **Sum rule.** A PIN of 4, 5 or 6 digits: 10⁴ + 10⁵ + 10⁶ = 1,110,000 PINs. The three lengths never overlap.

> **The sum rule needs disjoint cases.** When cases overlap, subtract what was counted twice: inclusion-exclusion, week 6.

#### [week5#perm-comb] Order matters in an arrangement, not in a selection

*Arrangements and selections*

| Question, from 8 people | Formula | Count |
| --- | --- | --- |
| Chair, deputy and secretary | P(8, 3) = 8 · 7 · 6 | 336 |
| A committee of 3 | C(8, 3) = P(8, 3) / 3! | 56 |
| Why divide by 3! | each committee can be ordered in 3! = 6 ways |  |

P(n, k) = n! / (n − k)! and C(n, k) = n! / (k! (n − k)!).

#### [week5#check-counting] Arrangement or selection?

*Checkpoint*

**Question:** A tasting panel of 4 judges is chosen from 9 cooks; the judges have no roles. How many panels are possible?

- A. 3,024
- B. 126
- C. 6,561
- D. 36

#### [week5#collision-count] All-different assignments are an arrangement count

*Block B · collisions*

- n people, each given one of N codes: **Nⁿ** assignments
- All codes different: **N (N − 1) … (N − n + 1)** = P(N, n)
- Chance all different = P(N, n) / Nⁿ, a count divided by a count

- **Checked by listing.** 6 codes, 3 people: listing all 216 assignments finds 120 with no repeat, and 6 · 5 · 4 = 120. The chance is 120 / 216 = 5/9.

#### [week5#birthday-curve] With 100 codes, 13 people already share one more often than not

*The birthday effect*

| Item | Value |
| --- | --- |
| 5 people | 9.65% |
| 10 people | 37.18% |
| 13 people | 55.72% |
| 20 people | 86.96% |

Exact chance of a shared code among n people with 100 equally likely codes.

#### [week5#expected-pairs] The average number of colliding pairs is C(n, 2) / N

*Pairs*

- Each of the C(n, 2) pairs shares a code in N · Nⁿ⁻² of the Nⁿ assignments
- So, averaged over all assignments, a pair collides 1/N of the time
- 30 people, 100 codes: C(30, 2) / 100 = **4.35** colliding pairs on average

- **A count, not a simulation.** The average is a total over every assignment divided by their number. Brute force on small cases checks it exactly.

#### [week5#check-collision] How many colliding pairs to expect?

*Checkpoint*

**Question:** A shop gives each of 50 loyalty cards a random 3-digit code (1,000 codes). On average over all assignments, how many pairs of cards share a code?

- A. 0.05
- B. 2.45
- C. 50
- D. 1.225

#### [week5#pigeonhole] More items than boxes means some box holds two, and ⌈n / N⌉ is guaranteed

*Block C · pigeonhole*

- 1,000 people and 366 possible birthdays: some day holds at least ⌈1000 / 366⌉ = **3** people
- Proof by contradiction: if every box held at most ⌈n / N⌉ − 1, the boxes would hold fewer than n items
- Below n = N, nothing is guaranteed, though collisions may be likely

- **In hashing.** Any map from long codes to short codes squeezes many inputs into each output: collisions are certain, only their rate is in question.

#### [week5#choosing-length] Choose a code length from the risk you accept, not from the number of people

*Design*

1. **State the risk** "at most 1 in 100 that any two share a code"
2. **Compute exactly** the chance for each length, with the formula
3. **Plan for the rest** a second check when a collision still happens

> **What goes wrong.** "We have 4,000 people and 65,536 codes, so codes are plenty" ignores the pairs. The lab measures how wrong that is.

#### [week5#check-pigeonhole] What is guaranteed?

*Checkpoint*

**Question:** A depot sorts 830 parcels into 100 bays by the last two digits of the parcel number. What does the pigeonhole principle guarantee?

- A. Some bay receives at least 9 parcels
- B. Every bay receives 8 or 9 parcels
- C. Some bay receives at least 8 parcels, and no more is guaranteed
- D. Nothing, since 830 is less than 100 · 100

#### [week5#lab-5-1] Hash collisions and the birthday problem, by formula and by brute force

Lab 5.1 · 105 min

Cut check-in codes from a hash, count collisions two ways, and choose a code length.

[W5_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W5_1.ipynb)

- [ ] Set up; sum and product rules (10 min)
- [ ] Arrangements and selections, two ways (15 min)
- [ ] Short check-in codes from a hash (10 min)
- [ ] Collision-free count: formula and brute force (20 min)
- [ ] The birthday problem exactly, with fractions (15 min)
- [ ] Expected colliding pairs against those issued (15 min)
- [ ] Pigeonhole: when a collision is certain (10 min)
- [ ] Choose the code length and record it (10 min)
- [ ] ✱ Stretch: Count the shared birthdays in the register and compare with the formula

#### [week5#debrief-codes] Four symbols leave 125 colliding pairs; the centre needs eight

*Debrief · lab 5.1*

| k | Codes | Expected pairs | Counted |
| --- | --- | --- | --- |
| 3 | 4,096 | 1,952.6 | 2,026 |
| 4 | 65,536 | 122.0 | 125 |
| 5 | 1,048,576 | 7.6 | 6 |
| 6 | 16,777,216 | 0.5 | 1 |

- Birthdays: 23 people pass one half; four symbols: 302 codes
- k = 2: at least 16 share a code; the largest group found is 27
- 1% risk: k = 8 for 4,000 (0.19%), k = 10 for 40,000

#### [week5#wrap-up] Three things to keep

*Week 5 · wrap-up*

- **Multiply, add, divide.** Product for steps, sum for disjoint cases, divide by the orderings you do not want.
- **Pairs drive collisions.** C(n, 2) / N pairs on average; trouble starts near the square root of N.
- **Check counts by listing.** Brute force on small cases catches the errors a formula hides.

#### [week5#next] Week 6: Counting people: re-identification risk

*Next*

Problem set 5 (60 minutes, AI off for the first attempt): labs/problem-sets/PS5.ipynb.

## Week 6: Counting people: re-identification risk

Why removing the identifier column does not anonymise a register

#### [week6#title] Counting people: re-identification risk

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 6: Why removing the identifier column does not anonymise a register

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week6#agenda] Counting people: re-identification risk

*This week*

- **Session 1 · Inclusion-exclusion and linkage risk**: Inclusion-exclusion, the product rule over quasi-identifiers, class sizes in a register, generalisation, and personal versus anonymised data

#### [week6#review-week5] How many all-different assignments?

*Review · week 5*

**Question:** Five interns each draw one of 8 desk numbers. In how many of the 8⁵ draws do all five get different desks?

- A. 56
- B. 32,768
- C. 6,720
- D. 40,320

### Session 1: Inclusion-exclusion and linkage risk

#### [week6#s1] Inclusion-exclusion and linkage risk

*Session 1*

- Count the people who share each combination of quasi-identifiers and find who is unique
- Apply inclusion-exclusion to count records that meet at least one of several conditions, and check it with sets
- Explain why removing the direct identifier does not anonymise data, and what generalisation changes

#### [week6#ie-two] Add the sets, then subtract what you counted twice

*Block A · inclusion-exclusion*

**|A ∪ B| = |A| + |B| − |A ∩ B|**

|A| = 60, |B| = 50, |A ∩ B| = 20: |A ∪ B| = 90.

**Three sets:** |A ∪ B ∪ C| = |A| + |B| + |C| − |A ∩ B| − |A ∩ C| − |B ∩ C| + |A ∩ B ∩ C|

- **Why it works.** An element in exactly two of three sets is added twice and subtracted once; one in all three is added three times, subtracted three times, added once. Every element ends with count 1.

#### [week6#ie-code] A formula over counts can be checked against the sets themselves

*Checked with sets*

```python
# file: python
ie = len(A) + len(B) - len(A & B)
assert ie == len(A | B)
```

- The formula needs only counts: useful when the sets are held by different teams
- The union needs the elements themselves
- On data you hold, compute both: they must agree

#### [week6#check-ie] How many are in at least one?

*Checkpoint*

**Question:** Of a club's members, 45 read the newsletter, 30 attend events and 12 do both. How many do at least one of the two?

- A. 75
- B. 63
- C. 51
- D. 33

#### [week6#quasi-identifiers] Quasi-identifiers single people out in combination

*Block B · counting people*

- **Direct identifier.** Identifies a person alone: a name, a member number, a code assigned to one person. "Removing names" removes these columns.
- **Quasi-identifiers.** Shared by many people alone, but rare in combination: birth date, sex, postal district. Often known to neighbours and colleagues.

> **The question to count.** After the direct identifiers are gone, how many people are alone in their combination of quasi-identifiers?

#### [week6#product-people] When combinations outnumber people, almost everyone is unique

*The product rule again*

| A town of 20,000 adults, 10 districts | Combinations | People each |
| --- | --- | --- |
| Birth date (60 years), sex, district | 438,000 | 0.05 |
| Birth year, sex, district | 1,200 | 16.67 |
| 10-year band, sex, district | 120 | 166.67 |

If people spread evenly, n (1 − 1/M)ⁿ⁻¹ of them are alone among M combinations: 95.5% in the first row.

#### [week6#class-sizes] Count the people in each combination, then the people alone

*By hand first*

| Six members: year, sex, area | People |
| --- | --- |
| 1990, F, D1 | 2 |
| 1990, M, D1 | 1 |
| 1985, F, D2 | 2 |
| 1972, M, D3 | 1 |

- A combination held by one person is a **class of size 1**
- The smallest class says how alone the most exposed people are
- A release rule can set a smallest class, for example five

#### [week6#check-unique] What does the product rule predict?

*Checkpoint*

**Question:** A survey of 500 people keeps age in years (60 values), sex and one of 4 regions. Roughly how many combinations are there per person?

- A. 240,000
- B. 66
- C. about 0.48
- D. about 0.96

#### [week6#pdpl] Data that can identify a person indirectly is personal data

*Block C · the law*

- **Personal Data Protection Law, Article 1.** Personal data includes data that "may directly or indirectly make it possible to identify an individual" (SDAIA's English text).
- **SDAIA's anonymisation guideline.** Anonymised data "shall no longer be considered personal data"; the guideline asks that it be irreversible, with an assessment of re-identification. It states that it is not a binding legal document.

> **So.** An extract in which birth date, sex and district single people out still makes identification indirectly possible: removing the code column does not anonymise it.

#### [week6#generalise] Coarser columns make classes bigger and lose detail

*Generalisation*

**Birth date** 438,000 combinations in the parallel town → **Birth year** 1,200 → **10-year band** 120

- The guideline's examples include age bands and birth year in place of the full date
- Each step trades analysis detail for larger classes: say what the analysis loses

#### [week6#linkage] Releases combine: the risk is the union, not the safer of the two

*Linkage*

- Two tables, each with few people alone, are released: A and B are the people alone in each
- Anyone in A ∪ B can be found: |A| + |B| − |A ∩ B| people
- A list published elsewhere with the same columns links back row by row

- **Count before you publish.** For each row of a list to be posted, count how many people in your register share its quasi-identifiers. One means that row names a person.

#### [week6#check-anonymised] Is it anonymised?

*Checkpoint*

**Question:** A gym removes member numbers from its list and keeps full birth date, sex and home district. Most members are alone in their combination. Under the Law's definition, the list is:

- A. anonymised, since no identifier remains
- B. still personal data, since it makes identification indirectly possible
- C. pseudonymised, so outside the Law
- D. personal data only if more than half are unique

#### [week6#lab-6-1] Re-identification risk counted from birth date, sex and postal district in a synthetic register

Lab 6.1 · 105 min

Count who shares each combination of birth date, sex and district, generalise, and link a posted sheet back.

[W6_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W6_1.ipynb)

- [ ] Set up; the extract without the volunteer code (10 min)
- [ ] People per combination of the three columns (15 min)
- [ ] Product rule: combinations and expected uniques (15 min)
- [ ] Generalise: birth year, five-year bands, district groups (20 min)
- [ ] Inclusion-exclusion, checked with sets (15 min)
- [ ] Link the posted sign-in sheet (15 min)
- [ ] Record for the data protection officer (15 min)
- [ ] ✱ Stretch: Find the most detailed release in which every combination holds five people

#### [week6#debrief-reid] Without its codes, the register still singles out 98.9% of volunteers

*Debrief · lab 6.1*

| Release | Unique | Smallest class |
| --- | --- | --- |
| Date, sex, district | 3,956 | 1 |
| Year, sex, district | 245 | 1 |
| 5-year band, sex, district | 19 | 1 |
| 5-year band, sex, district group | 6 | 1 |
| 10-year band, sex, district group | 0 | 8 |

- Even spread predicts 3,966 unique; by year it predicts 193, against 245 counted
- Three tables, each modest alone: 572 people unique in at least one
- The posted sign-in sheet: all 60 rows match exactly one volunteer

#### [week6#wrap-up] Three things to keep

*Week 6 · wrap-up*

- **Subtract the overlap.** Inclusion-exclusion counts a union from its parts, and code can check it.
- **Count who is alone.** Removing the identifier column leaves quasi-identifiers; count the classes of size 1.
- **Releases add up.** Two safe-looking tables, or a posted list, can name people together.

#### [week6#next] Week 7: Graphs, topological order and growth

*Next*

Problem set 6 (60 minutes, AI off for the first attempt): labs/problem-sets/PS6.ipynb.

## Week 7: Graphs, topological order and growth

Dependencies as a directed graph, the cycle that blocks a run, and how counts grow

#### [week7#title] Graphs, topological order and growth

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Week 7: Dependencies as a directed graph, the cycle that blocks a run, and how counts grow

Data & AI Foundations Track · 7 weeks + capstone · 1 session · 1 lab · FND-MTH-105

#### [week7#agenda] Graphs, topological order and growth

*This week*

- **Session 1 · Graphs, cycles, orders and recurrences**: Graphs, trees and directed acyclic graphs, paths and cycles, topological order, and recurrences and the growth of functions

#### [week7#review-week6] How many people can be found?

*Review · week 6*

**Question:** Two tables are released. 32 people are alone in their combination in the first, 18 in the second, and 7 of them are alone in both. How many people are alone in at least one table?

- A. 43
- B. 50
- C. 32
- D. 36

### Session 1: Graphs, cycles, orders and recurrences

#### [week7#s1] Graphs, cycles, orders and recurrences

*Session 1*

- Model dependencies as a directed graph and decide whether it has a cycle
- Compute a topological order and check that every edge points forward
- Set up a recurrence for a count, solve it, and compare how fast functions grow

#### [week7#graphs] A directed graph is a set of nodes and a relation on them

*Block A · graphs*

- An **edge** (u, v) is a pair in the relation: here "u must finish before v starts"
- **In-degree**: edges arriving; **out-degree**: edges leaving
- A **source** has in-degree 0; a **sink** has out-degree 0
- A **path** follows edges forward; a **cycle** is a path that returns to its start
- A **DAG** is a directed graph with no cycle; a **tree** has no cycle even with edges read both ways

- **A morning of five tasks.** A and B feed C; C feeds D and E. Sources A, B; sinks D, E. The in-degrees add up to 4, the number of edges.

#### [week7#cycle-blocks] A cycle of dependencies means no job on it can ever start

*Why cycles matter*

1. **1 · Start what is ready** Every job whose dependencies have all finished
2. **2 · Peel it off** Remove it; its successors lose one unfinished dependency
3. **3 · Repeat or stop** All gone: no cycle. Some left, none ready: a cycle among them

> **Takeaway.** In a graph with no cycle there is always a job with nothing unfinished before it, so peeling only stops early when a cycle exists.

#### [week7#check-cycle] Which jobs are never ready?

*Checkpoint*

**Question:** Edges: A → B, B → C, C → D, D → B, A → E. Peeling starts with every job that has no dependency. Which jobs are never ready?

- A. B, C and D
- B. D only
- C. B, C, D and E
- D. none, since A has no dependency

#### [week7#topo-order] A topological order puts every edge forward

*Block B · topological order*

The jobs in the order they are peeled form a **topological order**: for every edge (u, v), u comes before v.

The morning of five tasks has 4 of them: ABCDE, ABCED, BACDE, BACED. An order is rarely unique.

| Order A C B D E: edge | Positions | Forward? |
| --- | --- | --- |
| A → C | 1, 2 | yes |
| B → C | 3, 2 | no |
| C → D | 2, 4 | yes |
| C → E | 2, 5 | yes |

> **Check, do not trust.** The definition is edge by edge: one backward edge makes an order invalid, and no backward edge, with every node once, makes it valid.

#### [week7#invariant] A loop invariant proves the peeled order is topological

*Why peeling is correct*

| Part | For the invariant "every job in the list has all its predecessors earlier in the list" |
| --- | --- |
| Initialisation | The list is empty: nothing to check |
| Maintenance | A job is added only when all its predecessors are already in the list |
| Termination | If every job is peeled, the invariant covers every edge: the list is a topological order |

#### [week7#check-topo] Which order is valid?

*Checkpoint*

**Question:** Edges: P → R, Q → R, R → S, Q → S. Which running order respects every edge?

- A. P R Q S
- B. Q P S R
- C. Q P R S
- D. R Q P S

#### [week7#recurrence-paths] Count paths into a node from the counts into its predecessors

*Block C · recurrences*

In a grid walked right or down, the paths into a point are the paths into the point above plus the paths into the point on the left: **P(i, j) = P(i − 1, j) + P(i, j − 1)**, with 1 along the edges.

| 1 | 1 | 1 |
| --- | --- | --- |
| 1 | 2 | 3 |
| 1 | 3 | 6 |

- **Why it works.** Every path into a point arrives by exactly one last edge, so the paths split into disjoint groups, one per predecessor: the sum rule of week 5. Walk the points in a topological order so each sum uses finished counts.

#### [week7#growth] Counts that look small at n = 10 are out of reach at n = 30

*Growth*

| n | n² | 2ⁿ | n! |
| --- | --- | --- | --- |
| 10 | 100 | 1,024 | 3.6 × 10⁶ |
| 20 | 400 | 1,048,576 | 2.4 × 10¹⁸ |
| 30 | 900 | 1,073,741,824 | 2.7 × 10³² |

- Paths across an n by n grid: 252 at n = 5, 184,756 at n = 10, about 1.2 × 10¹⁷ at n = 30
- Listing every path or order is fine for a toy and hopeless at scale
- A recurrence does one step per node: count without listing

#### [week7#solve-recurrence] Guess a closed form from the first values, then prove it by induction

*Solve, then prove*

1. **1 · Recurrence** Links among n people: H(1) = 0, H(n) = H(n − 1) + (n − 1)
2. **2 · Guess** 0, 1, 3, 6, 10: H(n) = n(n − 1)/2
3. **3 · Prove** H(n − 1) + (n − 1) = (n − 1)(n − 2)/2 + (n − 1) = n(n − 1)/2

> **Takeaway.** The step uses the hypothesis for n − 1: that is the induction. Test the guess in code first, as the capstone asks.

#### [week7#check-recurrence] What does the recurrence give?

*Checkpoint*

**Question:** H(1) = 0 and H(n) = H(n − 1) + (n − 1). What is H(6)?

- A. 21
- B. 30
- C. 36
- D. 15

#### [week7#beyond] This course stops at cycles, orders and counts

*Where this goes next*

- **Here.** Graphs as relations, degrees, cycles, topological order, path counts by recurrence, and growth.
- **FND-PRG-103.** Graph algorithms: breadth-first and depth-first search and shortest paths, with their running times.

#### [week7#lab-7-1] Cycle detection and topological order in a pipeline graph

Lab 7.1 · 105 min

Find and name the cycle in the centre's thirty nightly jobs, remove the wrong edge, check an order edge by edge, and count paths two ways.

[W7_1.ipynb](https://sdaiaacademy.github.io/fnd-mth-105/labs/W7_1.ipynb)

- [ ] A small graph by hand; load the pipeline (10 min)
- [ ] Degrees, sources and sinks (10 min)
- [ ] Find a cycle: library and peeling (20 min)
- [ ] Name the cycle and remove the wrong edge (10 min)
- [ ] A topological order, checked edge by edge (15 min)
- [ ] Count paths: recurrence and listing (20 min)
- [ ] How path counts grow (10 min)
- [ ] Record for the operations lead (10 min)
- [ ] ✱ Stretch: Earliest round of each job when every ready job runs at once

#### [week7#debrief-pipeline] Three jobs waiting on each other stopped eleven

*Debrief · lab 7.1*

| Measure | Value |
| --- | --- |
| Jobs, dependencies | 30, 42 |
| Peeled before the run blocked | 19 |
| Cycle: J12 → J19 → J23 → J12 | 3 jobs |
| Paths from a source to J30 | 29 |
| Rounds if ready jobs run at once | 12 |

- Removing J23 → J12 leaves no cycle; peeled, library and checked orders all pass
- The alphabetical order breaks an edge
- Chained diamonds: 2ᵏ paths through 3k + 1 jobs

#### [week7#wrap-up] Three things to keep

*Week 7 · wrap-up*

- **Peel to find cycles.** If jobs remain and none is ready, a cycle holds them.
- **Check every edge.** An order is valid when every edge points forward: a finite check.
- **Count by recurrence.** Sum over predecessors, then prove the closed form by induction.

#### [week7#next] Capstone: Portfolio oral defences

*Next*

Problem set 7, then the second test. Your portfolio: three proofs from the claim list, each with its test code first, in a public GitHub repository.

## Capstone: Portfolio oral defences

Ten minutes each: one proof the assessor selects, explained step by step, then a changed hypothesis

#### [capstone#title] Portfolio oral defences

*SDAIA Academy · Discrete Mathematics and Logic for Computing*

Capstone: Ten minutes each: one proof the assessor selects, explained step by step, then a changed hypothesis

Data & AI Foundations Track · 7 weeks + capstone · 10 min talk and demo · FND-MTH-105

#### [capstone#agenda] How the defences run

*Capstone*

- **Portfolio clinic**: questions on the claims, the tests and the rubric
- **Portfolio work and a peer dry run**: finish the three proofs, then defend one to a partner
- **Oral defences**: one proof each, explained step by step, then a changed hypothesis
- **Feedback and closing**: the assessor's written feedback, what next

#### [capstone#rubric] The portfolio rubric

*How the portfolio is scored*

| Item | Value |
| --- | --- |
| Claims stated precisely | 15% |
| Test code before each proof, limits stated | 20% |
| Each proof valid: every step justified | 30% |
| The induction proof complete | 20% |
| Readable, reproducible, AI use recorded | 15% |

> **Test first, then prove.** A passing test is evidence for the cases it ran; only the proof covers the rest.

#### [capstone#format] 10 minutes for each defence

*Format*

- **1 · The claim.** The assessor picks one of your three proofs. State the claim and the method you chose. About one minute.
- **2 · Step by step.** Walk through the proof and say why each step holds, then what your tests showed. About six minutes.
- **3 · A changed hypothesis.** The assessor changes one assumption. Say whether the proof survives and which step breaks. About three minutes.

> **Peer dry run.** Pairs defend one proof to each other and change one hypothesis for each other. The partner writes one strength, one question and one suggestion.

#### [capstone#running-order] Who defends when

*Running order*

| # | Participant code | Proof selected |
| --- | --- | --- |
| 1 |  |  |
| 2 |  |  |
| 3 |  |  |
| 4 |  |  |
| 5 |  |  |
| 6 |  |  |
| 7 |  |  |
| 8 |  |  |

#### [capstone#final-prep] Portfolio clinic · 20 minutes

*Before the work starts*

Bring one question about a claim, a test or the rubric.

#### [capstone#dry-run] Peer dry run · 25 minutes

*Before the defences*

Defend one proof to your partner, then swap. Change one hypothesis for each other.

#### [capstone#now-presenting] Defence

*Now defending*

#### [capstone#review] What the defences showed

*Assessor review*

- **Strongest patterns.** What several portfolios got right.
- **Common gaps.** The steps most often left unjustified.
- **One surprise.** A test or a changed hypothesis nobody expected.

#### [capstone#what-next] Keep going

*After the course*

- **Your portfolio stays yours:** add a fourth claim, tested first, then proved
- **Next Academy course:** FND-PRG-103 takes graphs further, with search and shortest paths

#### [capstone#thanks] Thank you

*SDAIA Academy*

Discrete Mathematics and Logic for Computing
