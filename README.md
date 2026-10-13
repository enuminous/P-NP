# P versus NP — Wright's restricted recursive-search obstruction

**Author:** Matthew Chenoweth Wright; computational audit and Lean draft with AI assistance.

## What is proved

The satisfiable 2-CNF gadget `(x∨y) ∧ (x∨¬y) ∧ (¬x∨y)` has a unique satisfying assignment `11`, yet the unsatisfied-clause count cannot be strictly improved by one bit flip from `00`. This extends by independent blocks to arbitrarily many variables for strict single-bit improvement from all zeros.

**This is NOT a proof of P≠NP.** The constructed family is 2-SAT and admits polynomial-time solution. Sideways moves defeat the local trap.

## Run

```sh
python3 -m unittest -v test_experiment.py
python3 experiment.py --max-n 16
lake build
```

The Python tests have been run locally. Lean compilation has **not** been run; see `LEAN_STATUS.md`.

## Audit

`ZOO_46_MATRIX.csv` covers 46 animal names in a topic-adapted review. **It is not an execution of the 46 canonical animal codebases.** See `ZOO_46_REPORT.md`.

## Files

- `PAPER.md`: derivation and boundaries
- `ZOO_46_REPORT.md`, `ZOO_46_MATRIX.csv`: complete mapped screening
- `WrightSAT.lean`: Lean formalization draft
- `LEAN_STATUS.md`: verification caveats
- `experiment.py`, `test_experiment.py`, `results.csv`: reproducible numerical checks
- `ABLATIONS.md`, `curve.png`: escape routes and growth chart
- `index.html`: GitHub Pages landing page
