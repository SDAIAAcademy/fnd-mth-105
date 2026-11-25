# Labs: what each one should show

The numbers below come from running the solution notebooks with the committed data (seed 105).
Every number is fixed by the data and the seed; none depends on the machine.

| Lab | Planted in the data | What the participant should find |
|---|---|---|
| 1.1 | Two of the 300 active volunteers have no badge (V-00117, V-00242); three badge numbers were issued twice (BD-0059, BD-0420, BD-0909); eight volunteers work two shifts of one event | The badge map is not a function on the 300 volunteers, not injective and not surjective onto BD-0001 to BD-0999; V-00117 is on a shift without a badge; shift to event is a function onto the 30 events, three shifts each; the join returns 600 rows and 592 distinct pairs, which equal the composition |
| 2.1 | The handbook's sentence of the access rule lacks brackets; the coordinator's late change leaves one first-aider (V-00048) for SH-C and SH-D | The contrapositive, De Morgan and distribution hold and the converse does not; affirming the consequent and denying the antecedent each have the counterexample row (m F, g T); the two phrasings differ on 2 of 16 rows (o F, c F, s T); the puzzle has 50 variables and 800 clauses and a schedule that passes every rule; after the late change it is unsatisfiable, with a core of availability, one shift each, and first aid on SH-C and SH-D; keeping V-00090 on SH-D or dropping first aid on one of the two shifts restores a schedule; the small variant has 36 schedules by brute force, by solver and by 3! · 3! |

The worked answers to the problem sets, the tests, the five rules of LO2, the portfolio claims and the defence prompts are not in this repository.
