---
course: "Discrete Mathematics and Logic for Computing"
code: "FND-MTH-105"
version: "2027.1.0"
deck: "week1"
day: 1
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-mth-105/slides/week1.html"
---

# Discrete Mathematics and Logic for Computing

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
