<!-- academy:title -->
# Discrete Mathematics and Logic for Computing

الرياضيات المتقطعة والمنطق للحوسبة

Data & AI Foundations Track · SDAIA Academy · FND-MTH-105 · Level 100

REPLACE: one line under the title: what participants can do after the course

Participants practise the discrete mathematics and proof that computing degrees assume: sets, relations, logic, proof, counting and graphs. Code tests each claim on generated cases before it is proved, so the gap between testing and proof is visible. Labs link relations to joins, logic to rule checking, counting to collision and re-identification risk, and graphs to pipeline dependencies. Algorithms on graphs follow in FND-PRG-103.

**Format:** Extended: 7 weeks part-time, one session and one lab a week, weekly graded problem sets and a capstone portfolio

**Course page:** https://sdaiaacademy.github.io/fnd-mth-105/
<!-- /academy:title -->

## Outcomes

| | Outcomes | Level | Evidence |
|---|---|---|---|
| LO1 | Identify whether a relation is a function, an equivalence or an order, and which properties it has, given twelve relations from data and software | Awareness | supervised AI-off test, at least 70% correct |
| LO2 | Distinguish valid from invalid arguments and translate plain-language rules into propositional and predicate logic, given five access and data-quality rules | Awareness | rules checked by truth table or solver, four of five correct |
| LO3 | Describe direct, contradiction and induction proofs and identify the gap in a flawed proof, given six short proofs, two with planted errors | Awareness | marked answers in the supervised test |
| LO4 | Apply induction and loop invariants to prove simple claims about integers, sets and recursive code, given claims first tested in code | Applied | rubric-marked proofs, each with its test code |
| LO5 | Compute counts of arrangements, selections and collisions and verify them by enumeration, given hashing and record-linkage problems | Applied | a notebook in which formula and brute-force counts agree |
| LO6 | Use a graph model of dependencies to find cycles and compute a topological order, given a pipeline graph with a planted cycle | Applied | output naming the cycle and a valid order once it is removed |

<!-- academy:units -->
## Units

| Unit | Title | Sessions | Slides |
|---|---|---|---|
| Week 1 | REPLACE: the theme of this unit, in a few words | REPLACE: the title of Session 1 | [`slides/week1.html`](slides/week1.html) |
| Week 2 | REPLACE: the theme of this unit, in a few words | REPLACE: the title of Session 1 | [`slides/week2.html`](slides/week2.html) |
| Week 3 | REPLACE: the theme of this unit, in a few words | REPLACE: the title of Session 1 | [`slides/week3.html`](slides/week3.html) |
| Week 4 | REPLACE: the theme of this unit, in a few words | REPLACE: the title of Session 1 | [`slides/week4.html`](slides/week4.html) |
| Week 5 | REPLACE: the theme of this unit, in a few words | REPLACE: the title of Session 1 | [`slides/week5.html`](slides/week5.html) |
| Week 6 | REPLACE: the theme of this unit, in a few words | REPLACE: the title of Session 1 | [`slides/week6.html`](slides/week6.html) |
| Week 7 | REPLACE: the theme of this unit, in a few words | REPLACE: the title of Session 1 | [`slides/week7.html`](slides/week7.html) |
| Capstone | Capstone project presentations |  | [`slides/capstone.html`](slides/capstone.html) |
<!-- /academy:units -->

## Case study

**REPLACE: the name of the fictional organisation every lab works on.** REPLACE: two sentences on the case study and its synthetic data

<!-- academy:labs -->
## Labs

Every lab is a notebook in `labs/`. Open it in Google Colab from the course page, or run it locally with `uv`. Exercises raise `NotImplementedError` until they are done; the reference versions are in `labs/solutions/`.

| | Session | Lab | File |
|---|---|---|---|
| 1.1 | Week 1 · Session 1 | REPLACE: what participants build in lab 1.1 | [`W1_1.ipynb`](labs/W1_1.ipynb) |
| 2.1 | Week 2 · Session 1 | REPLACE: what participants build in lab 2.1 | [`W2_1.ipynb`](labs/W2_1.ipynb) |
| 3.1 | Week 3 · Session 1 | REPLACE: what participants build in lab 3.1 | [`W3_1.ipynb`](labs/W3_1.ipynb) |
| 4.1 | Week 4 · Session 1 | REPLACE: what participants build in lab 4.1 | [`W4_1.ipynb`](labs/W4_1.ipynb) |
| 5.1 | Week 5 · Session 1 | REPLACE: what participants build in lab 5.1 | [`W5_1.ipynb`](labs/W5_1.ipynb) |
| 6.1 | Week 6 · Session 1 | REPLACE: what participants build in lab 6.1 | [`W6_1.ipynb`](labs/W6_1.ipynb) |
| 7.1 | Week 7 · Session 1 | REPLACE: what participants build in lab 7.1 | [`W7_1.ipynb`](labs/W7_1.ipynb) |
<!-- /academy:labs -->

## Capstone

A portfolio of three proofs, at least one by induction, each preceded by test code, with a ten-minute oral defence of one proof the assessor selects

**Submission:** REPLACE: what participants submit and how: a public repository link, or a shared folder for a course without code

## Prerequisites

- School algebra
- Writes short Python programs with lists, loops, functions and recursion (FND-PRG-101 or equivalent)

<!-- academy:tools -->
## Tools

Each line is a capability; the examples are interchangeable.

- **Satisfiability solver:** PySAT, Z3
- **Graph library:** NetworkX, igraph
- **Notebook environment:** JupyterLab, marimo, a free hosted notebook service
- **Hint-only tutor:** an open-weight model in tutor mode, an approved assistant with a tutor instruction
<!-- /academy:tools -->

<!-- academy:sources -->
## Sources

- REPLACE: every source the course cites, with its address, in course.json under "sources"; this list is written from there
<!-- /academy:sources -->

### National references

- SDAIA Data & AI Academic Programs Standards Framework (2026): bridging unit MSF-Discrete at Explain level: REPLACE: the address of the official text
- Personal Data Protection Law (PDPL): personal versus anonymised data, in the re-identification lab: REPLACE: the address of the official text
