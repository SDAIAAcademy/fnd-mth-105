<!-- academy:title -->
# Discrete Mathematics and Logic for Computing

الرياضيات المتقطعة والمنطق للحوسبة

Data & AI Foundations Track · SDAIA Academy · FND-MTH-105 · Level 100

Test a claim in code, then prove it: sets, relations, logic, induction, counting and graphs, applied to joins, rules, collisions, re-identification and pipelines

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
| Week 1 | Sets, functions and relations | Sets, functions and relations | [`slides/week1.html`](slides/week1.html) |
| Week 2 | Logic: truth tables and satisfiability | Propositional logic, normal forms and SAT | [`slides/week2.html`](slides/week2.html) |
| Week 3 | Predicates, quantifiers and first proofs | Quantifiers, relation properties and first proofs | [`slides/week3.html`](slides/week3.html) |
| Week 4 | Induction, invariants and the limits of testing | Induction, loop invariants and testing versus proof | [`slides/week4.html`](slides/week4.html) |
| Week 5 | Counting, collisions and the birthday problem | Counting arrangements, selections and collisions | [`slides/week5.html`](slides/week5.html) |
| Week 6 | Counting people: re-identification risk | Inclusion-exclusion and re-identification risk | [`slides/week6.html`](slides/week6.html) |
| Week 7 | Graphs, topological order and growth | Graphs, cycles, topological order and recurrences | [`slides/week7.html`](slides/week7.html) |
| Capstone | Portfolio oral defences |  | [`slides/capstone.html`](slides/capstone.html) |
<!-- /academy:units -->

## Case study

**The community volunteer centre (fictional).** An unnamed non-profit in one unnamed city registers 4,000 volunteers, trains them and staffs community events in twelve postal districts, coded PD-01 to PD-12. Its new data analyst, the participant's role, works with the volunteer coordinator, the data protection officer and the operations lead, by role only. Each week takes one of the centre's problems: badge numbers and a join that overcounts (week 1), access rules and a shift schedule (2), relations from its data and software (3), its team tree and loops (4), short check-in codes (5), a de-identified extract (6) and the nightly pipeline (7).

All data is synthetic, written by [`labs/prepare_data.py`](labs/prepare_data.py) with seed 105. People appear only as codes (V-00001 to V-04000); no person name, phone number or identifier of any real kind is generated. No public dataset is used and nothing is downloaded beyond the Python packages.

## Plan and minutes

The entry's 40 hours, in minutes:

| Catalog hours | Minutes | How they are spent |
|---|---:|---|
| Instruction 13 | 780 | Week 1: 120 minutes (with the setup check); weeks 2 to 7: 110 minutes each of teaching in three blocks, each closing with a checkpoint, plus a review checkpoint and the lab debrief |
| Lab 12 | 720 | Week 1: 90 minutes; weeks 2 to 7: 105 minutes each, with steps timed to the minute and one stretch |
| Guided self-study 7 | 420 | 7 problem sets of 60 minutes ([`labs/problem-sets/`](labs/problem-sets/)) |
| Assessment 3 | 180 | 2 supervised AI-off tests of proofs and short problems, 90 minutes each, after week 4 and after week 7 |
| Capstone 5 | 300 | portfolio clinic 20, independent portfolio work 230, peer dry run of the defence 25, oral defence 10, changeover 5, assessor's written feedback 10 |
| **Total** | **2,400** | 40 hours |

## Assessment

| Assessed work | Weight |
|---|---:|
| Weekly problem sets | 20% |
| Two supervised AI-off tests of proofs and short problems | 40% |
| Capstone portfolio, rubric-scored | 30% |
| Oral defence | 10% |

**Passing:** 60% overall and at least 50% on each supervised test.

**Authenticity:** Proctored tests without assistance, and an oral defence in which the participant explains a proof step by step and handles a changed hypothesis.

**Certificate:** completion with assessed work.

The code items of the problem sets are checked by [`labs/problem-sets/pscheck.py`](labs/problem-sets/pscheck.py), which stores no answers; the written items (proofs, translations, counts with reasons) are marked by the trainer. The portfolio rubric scores the portfolio only; the oral defence is scored on its own, so nothing counts twice.

**Held outside this repository**, in the trainer pack: the worked answers to the problem sets; the blueprint and items of the two supervised tests with their keys (the twelve relations of LO1, the six short proofs with two planted errors of LO3); the five access and data-quality rules of LO2 with their reference formulas; the list of claims the assessor issues for the portfolio, with the proof-marking guide; and the defence's changed-hypothesis prompts. Publishing them would defeat the assessment. The lab solutions, with model proofs of the labs' own claims, are public, in [`labs/solutions/`](labs/solutions/).

## AI policy

AI-off for first attempts at problem sets and proofs and in both tests. AI-tutor in labs, pointing at gaps without writing proofs. AI-full in the portfolio, which is defended orally.

The tutor's instruction is [`labs/tutor/TUTOR.md`](labs/tutor/TUTOR.md).

## Responsible use

Covers privacy through counting: participants count how many people in a synthetic register share each combination of quasi-identifiers and explain why removing names does not anonymise data.

The register has no names to remove: its direct identifier is the volunteer code, and the lab removes that column. The count shows how many people birth date, sex and postal district still single out.

<!-- academy:labs -->
## Labs

Every lab is a notebook in `labs/`. Open it in Google Colab from the course page, or run it locally with `uv`. Exercises raise `NotImplementedError` until they are done; the reference versions are in `labs/solutions/`.

| | Session | Lab | File |
|---|---|---|---|
| 1.1 | Week 1 · Session 1 | Sets, functions and joins in code | [`W1_1.ipynb`](labs/W1_1.ipynb) |
| 2.1 | Week 2 · Session 1 | Truth tables in code, and a scheduling puzzle solved with a SAT solver | [`W2_1.ipynb`](labs/W2_1.ipynb) |
| 3.1 | Week 3 · Session 1 | Relation properties checked in code | [`W3_1.ipynb`](labs/W3_1.ipynb) |
| 4.1 | Week 4 · Session 1 | Claims tested in code, then proved | [`W4_1.ipynb`](labs/W4_1.ipynb) |
| 5.1 | Week 5 · Session 1 | Hash collisions and the birthday problem, by formula and by brute force | [`W5_1.ipynb`](labs/W5_1.ipynb) |
| 6.1 | Week 6 · Session 1 | Re-identification risk counted from birth date, sex and postal district in a synthetic register | [`W6_1.ipynb`](labs/W6_1.ipynb) |
| 7.1 | Week 7 · Session 1 | Cycle detection and topological order in a pipeline graph | [`W7_1.ipynb`](labs/W7_1.ipynb) |
<!-- /academy:labs -->

Labs 2.1, 3.1, 5.1, 6.1 and 7.1 are the catalog entry's five lab lines, in its order and wording. Labs 1.1 and 4.1 are additions, so that each of the seven weekly sessions has a lab: they practise the entry's topics of sets, functions and joins as relation composition, and of induction, loop invariants and testing a claim versus proving it. Graph algorithms beyond cycles and topological order (breadth-first and depth-first search, shortest paths) follow in FND-PRG-103.

## Capstone

A portfolio of three proofs, at least one by induction, each preceded by test code, with a ten-minute oral defence of one proof the assessor selects

**Submission:** a link to a public GitHub repository holding the portfolio: three proofs, at least one by induction, each preceded by its test code and that code's output, with a record of any AI use. The assessor issues the claims; then a ten-minute oral defence of one proof the assessor selects, explained step by step, with a changed hypothesis to handle.

| Rubric criterion (the portfolio) | Weight |
|---|---:|
| Each claim stated precisely: domain, quantifiers, hypothesis and conclusion | 15 |
| Test code before each proof: generated or exhaustive cases, edge cases, and an honest note of what the tests cannot show | 20 |
| Each proof valid: method named, every step justified, no gap | 30 |
| The induction proof complete: base case, hypothesis stated, an inductive step that uses it (or an invariant with initialisation, maintenance and termination) | 20 |
| Portfolio readable and reproducible: code runs, AI use recorded, sources named | 15 |

## Repository

```
course.json      the course manifest: outcomes, units, sessions, labs, capstone, tools, sources
slides/          one deck per week and the capstone deck; the engine builds them into the course site
labs/            the lab notebooks, their solutions, the problem sets and their checker, the helper
                 module (dm.py), the data generator (prepare_data.py), the tutor instruction
assessments/     the public practice questions (bank.json); exam items are never kept here
```

Build and check with the Academy engine: `node academy.mjs check`, `node academy.mjs build`.

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
<!-- /academy:sources -->

### National references

- SDAIA Data & AI Academic Programs Standards Framework (2026): bridging unit MSF-Discrete at Explain level (one of the framework's common prerequisite and bridging knowledge units for post-bachelor programs, section 3.6): https://sdaia.gov.sa/en/MediaCenter/KnowledgeCenter/ResearchLibrary/Academic-Programs-Standards-Framework-Q3.pdf
- Personal Data Protection Law (PDPL): personal versus anonymised data, in the re-identification lab. The Law's definition of personal data (Article 1) is quoted from SDAIA's English text: https://sdaia.gov.sa/en/SDAIA/about/Documents/PersonalDataProtectionLaw.pdf. What anonymisation requires is quoted from SDAIA's Personal Data Destruction, Anonymization and Pseudonymisation Guideline, version 1.0, which states that it is not a binding legal document: https://sdaia.gov.sa/Documents/PersonalDataDestructionAnonymizationAndEncryptionGuideline.pdf
