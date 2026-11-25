---
course: "Discrete Mathematics and Logic for Computing"
code: "FND-MTH-105"
version: "2027.1.0"
deck: "week2"
day: 2
language: "en"
view: "trainee"
source: "https://sdaiaacademy.github.io/fnd-mth-105/slides/week2.html"
---

# Discrete Mathematics and Logic for Computing

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
