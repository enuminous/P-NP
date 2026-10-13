# Complete 46-animal mapped audit — scope and status

The 46 names are taken from `enuminous/Monolithic-Zoo-Lean4/Registry.lean` (default branch, accessed 2026-10-13). All 46 receive a **mapped mathematical review** in `ZOO_46_MATRIX.csv`.

**Crucial qualification:** these checks are custom, topic-specific screening gates. They are **not executions of the 46 upstream Zoo implementations**, and their adapted labels are **not asserted to be canonical animal semantics**. The source registry gives names, not proof that the Python/Lean pipelines have been executed. No complete Zoo execution certificate is available here.

## Outcome

- The satisfiable 2-CNF gadget has a strict one-flip descent trap at all-zero initialization.
- The trap is replicated across arbitrary disjoint gadget copies.
- A plateau move followed by a second flip solves each gadget.
- Standard 2-SAT algorithms run in polynomial time; the gadget therefore cannot prove P≠NP.
- All numerical checks in the accompanying Python tests and exhaustive experiment are separate from the Lean proof status.

## Next step for genuine upstream execution

Pin all 46 Zoo upstream source revisions, run their executable kernels with defined SAT input adapters, retain stdout/stderr and hashes, and only mark each animal EXECUTED after that evidence exists. Many animals may not accept SAT instances without a validated adapter.
