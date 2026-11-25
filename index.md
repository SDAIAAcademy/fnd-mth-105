---
course: "Discrete Mathematics and Logic for Computing"
code: "FND-MTH-105"
version: "2027.1.0"
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-mth-105/index.html"
---

# Discrete Mathematics and Logic for Computing

الرياضيات المتقطعة والمنطق للحوسبة

Data & AI Foundations Track · 7 weeks + capstone · 40 hours · Level 100

Test a claim in code, then prove it: sets, relations, logic, induction, counting and graphs, applied to joins, rules, collisions, re-identification and pipelines

Participants practise the discrete mathematics and proof that computing degrees assume: sets, relations, logic, proof, counting and graphs. Code tests each claim on generated cases before it is proved, so the gap between testing and proof is visible. Labs link relations to joins, logic to rule checking, counting to collision and re-identification risk, and graphs to pipeline dependencies. Algorithms on graphs follow in FND-PRG-103.

**Who it is for:** Beginners. Career changers and non-computing graduates closing bridging gaps before advanced study, and computing graduates refreshing the mathematics behind models; a placement test lets participants skip any course whose content they already command.

**Format:** Extended: 7 weeks part-time, one session and one lab a week, weekly graded problem sets and a capstone portfolio

## The case study

**The community volunteer centre (fictional).** An unnamed non-profit in one unnamed city registers 4,000 volunteers, trains them and staffs community events in twelve postal districts; its analyst checks joins, access rules, a shift schedule, check-in codes, a de-identified extract and a nightly pipeline. All data is synthetic, generated with a fixed seed; people appear only as codes such as V-00412, never by name.

## The course

### Week 1: Sets, functions and relations

Slides: https://sdaiaacademy.github.io/fnd-mth-105/slides/week1.md

- **Session 1: Sets, functions and relations**
  - Compute set operations and the size of a Cartesian product, and check them in code
  - Decide whether a map from the data is a function and whether it is injective, surjective or bijective
  - Compose two relations and explain how a database join differs from the composition
  - [Lab 1.1: Sets, functions and joins in code (90 min)](https://sdaiaacademy.github.io/fnd-mth-105/labs/W1_1.ipynb)

### Week 2: Logic: truth tables and satisfiability

Slides: https://sdaiaacademy.github.io/fnd-mth-105/slides/week2.md

- **Session 1: Propositional logic, normal forms and SAT**
  - Translate a plain-language rule into a propositional formula and check it by truth table
  - Distinguish a valid argument from an invalid one by searching for a counterexample row
  - Encode a small scheduling problem in conjunctive normal form and solve it with a SAT solver
  - [Lab 2.1: Truth tables in code, and a scheduling puzzle solved with a SAT solver (105 min)](https://sdaiaacademy.github.io/fnd-mth-105/labs/W2_1.ipynb)

### Week 3: Predicates, quantifiers and first proofs

Slides: https://sdaiaacademy.github.io/fnd-mth-105/slides/week3.md

- **Session 1: Quantifiers, relations and first proofs**
  - Write a relation property or a data-quality rule with quantifiers and negate it correctly
  - Classify a relation as a function, an equivalence, a partial order or none, with a counterexample for each property it lacks
  - Prove a short claim directly or by contradiction, and refute a false one with a counterexample
  - [Lab 3.1: Relation properties checked in code (105 min)](https://sdaiaacademy.github.io/fnd-mth-105/labs/W3_1.ipynb)

### Week 4: Induction, invariants and the limits of testing

Slides: https://sdaiaacademy.github.io/fnd-mth-105/slides/week4.md

- **Session 1: Induction, invariants, testing and proof**
  - Prove a claim about the integers by mathematical induction after testing it in code
  - Prove a property of a recursive structure by structural induction
  - State and check a loop invariant, and use it to prove a loop correct
  - [Lab 4.1: Claims tested in code, then proved (105 min)](https://sdaiaacademy.github.io/fnd-mth-105/labs/W4_1.ipynb)

### Week 5: Counting, collisions and the birthday problem

Slides: https://sdaiaacademy.github.io/fnd-mth-105/slides/week5.md

- **Session 1: Counting arrangements and collisions**
  - Count arrangements and selections with the sum and product rules, permutations and combinations
  - Compute the chance that short codes collide and verify it by exact enumeration
  - Use the pigeonhole principle to show when a collision is certain
  - [Lab 5.1: Hash collisions and the birthday problem, by formula and by brute force (105 min)](https://sdaiaacademy.github.io/fnd-mth-105/labs/W5_1.ipynb)

### Week 6: Counting people: re-identification risk

Slides: https://sdaiaacademy.github.io/fnd-mth-105/slides/week6.md

- **Session 1: Inclusion-exclusion and linkage risk**
  - Count the people who share each combination of quasi-identifiers and find who is unique
  - Apply inclusion-exclusion to count records that meet at least one of several conditions, and check it with sets
  - Explain why removing the direct identifier does not anonymise data, and what generalisation changes
  - [Lab 6.1: Re-identification risk counted from birth date, sex and postal district in a synthetic register (105 min)](https://sdaiaacademy.github.io/fnd-mth-105/labs/W6_1.ipynb)

### Week 7: Graphs, topological order and growth

Slides: https://sdaiaacademy.github.io/fnd-mth-105/slides/week7.md

- **Session 1: Graphs, cycles, orders and recurrences**
  - Model dependencies as a directed graph and decide whether it has a cycle
  - Compute a topological order and check that every edge points forward
  - Set up a recurrence for a count, solve it, and compare how fast functions grow
  - [Lab 7.1: Cycle detection and topological order in a pipeline graph (105 min)](https://sdaiaacademy.github.io/fnd-mth-105/labs/W7_1.ipynb)

### Capstone: Portfolio oral defences

Slides: https://sdaiaacademy.github.io/fnd-mth-105/slides/capstone.md

## Capstone

A portfolio of three proofs, at least one by induction, each preceded by test code, with a ten-minute oral defence of one proof the assessor selects

**What you submit:** A link to a public GitHub repository holding the portfolio: three proofs, at least one by induction, each preceded by its test code and that code's output, with a record of any AI use; then a ten-minute oral defence of one proof the assessor selects, explained step by step, with a changed hypothesis to handle

**Rubric:**

- Each claim stated precisely: domain, quantifiers, hypothesis and conclusion: 15%
- Test code before each proof: generated or exhaustive cases, edge cases, and an honest note of what the tests cannot show: 20%
- Each proof valid: method named, every step justified, no gap: 30%
- The induction proof complete: base case, hypothesis stated, an inductive step that uses it (or an invariant with initialisation, maintenance and termination): 20%
- Portfolio readable and reproducible: code runs, AI use recorded, sources named: 15%

## Outcomes

- **LO1** Identify whether a relation is a function, an equivalence or an order, and which properties it has, given twelve relations from data and software (Awareness) Evidence: supervised AI-off test, at least 70% correct
- **LO2** Distinguish valid from invalid arguments and translate plain-language rules into propositional and predicate logic, given five access and data-quality rules (Awareness) Evidence: rules checked by truth table or solver, four of five correct
- **LO3** Describe direct, contradiction and induction proofs and identify the gap in a flawed proof, given six short proofs, two with planted errors (Awareness) Evidence: marked answers in the supervised test
- **LO4** Apply induction and loop invariants to prove simple claims about integers, sets and recursive code, given claims first tested in code (Applied) Evidence: rubric-marked proofs, each with its test code
- **LO5** Compute counts of arrangements, selections and collisions and verify them by enumeration, given hashing and record-linkage problems (Applied) Evidence: a notebook in which formula and brute-force counts agree
- **LO6** Use a graph model of dependencies to find cycles and compute a topological order, given a pipeline graph with a planted cycle (Applied) Evidence: output naming the cycle and a valid order once it is removed

## Tools

- **Satisfiability solver:** PySAT, Z3
- **Graph library:** NetworkX, igraph
- **Notebook environment:** JupyterLab, marimo, a free hosted notebook service
- **Hint-only tutor:** an open-weight model in tutor mode, an approved assistant with a tutor instruction

## Prerequisites

- School algebra
- Writes short Python programs with lists, loops, functions and recursion (FND-PRG-101 or equivalent)

## Sources

### National references

- [SDAIA: Data & AI Academic Programs Standards Framework (2026), section 3.6, the common prerequisite and bridging knowledge units](https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/Academic-Programs-Standards-Framework-Q3.pdf)
- [SDAIA: Personal Data Protection Law, Article 1, the definition of personal data (English text)](https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf)
- [SDAIA: Personal Data Destruction, Anonymization and Pseudonymisation Guideline, version 1.0](https://sdaia.gov.sa/Documents/PersonalDataDestructionAnonymizationAndEncryptionGuideline.pdf)

### Tools

- [PySAT: the SAT solver toolkit for Python (documentation)](https://pysathq.github.io/)
- [NetworkX: directed acyclic graph algorithms, topological sort and cycles](https://networkx.org/documentation/stable/reference/algorithms/dag.html)
- [Python standard library: hashlib, secure hashes and message digests](https://docs.python.org/3/library/hashlib.html)
- [Python standard library: sqlite3, the database used for the join in lab 1.1](https://docs.python.org/3/library/sqlite3.html)
- [Python standard library: fractions, exact rational arithmetic](https://docs.python.org/3/library/fractions.html)

---

SDAIA Academy · Data & AI Foundations Track · Discrete Mathematics and Logic for Computing

Course version 2027.1.0 · engine 1.0.0 · built 2026-11-25 · commit 9b66171
