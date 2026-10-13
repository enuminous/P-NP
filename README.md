# P versus NP — Wright's restricted recursive-search obstruction

**Author:** Matthew Chenoweth Wright · Formalization and computational audit with AI assistance

[Research dashboard](https://enuminous.github.io/P-NP/) · [Lean verification (passed)](https://github.com/enuminous/P-NP/actions/runs/38431493342) · [Lean source](WrightSAT.lean)

## Verified result

For the satisfiable 2-CNF formula

```text
G(x,y) = (x ∨ y) ∧ (x ∨ ¬y) ∧ (¬x ∨ y)
```

the unique satisfying assignment is `(true,true)`. Starting from `(false,false)`, neither single-variable flip strictly reduces the number of unsatisfied clauses. Thus a strictly improving one-bit local search stops at a non-solution. A sideways move followed by a flip escapes the trap.

**This is not a proof of P ≠ NP.** This formula belongs to 2-SAT, which has polynomial-time algorithms. The arbitrary-block generalization is explained in [PAPER.md](PAPER.md), but a complete Lean theorem about all list-wide one-bit updates remains future work.

## Lean 4: verified on GitHub Actions

- **Toolchain:** Lean 4 v4.19.0 (pinned in `lean-toolchain`)
- **CI:** [Successful build and dependency audit](https://github.com/enuminous/P-NP/actions/runs/38431493342)
- **Compilation:** `lake build` succeeded
- **Theorem dependency audit:** `lake env lean ProofAudit.lean` reported no axiom dependencies for eight named theorems
- **Unfinished-proof check:** passed on the successful run

The earlier CI failures were workflow configuration issues: missing `lake-manifest.json` in the first setup, and an overly broad `sorry` text search matching a source comment. They were repaired; the subsequent workflow succeeded.

### Reproduce

```sh
lake update
lake build
lake env lean ProofAudit.lean
python3 -m unittest -v test_experiment.py
python3 experiment.py --max-n 16
```

## Audit boundaries

The [46-animal matrix](ZOO_46_MATRIX.csv) is a topic-adapted screening of the 46 animal names, **not** execution of all 46 upstream Zoo codebases. The numerical experiments exhaustively checked instances through 16 variables, but cannot establish general complexity-class separations.

## Repository guide

| File | Purpose |
|---|---|
| [PAPER.md](PAPER.md) | Mathematical argument, proof and limits |
| [WrightSAT.lean](WrightSAT.lean) | Lean 4 theorem definitions |
| [ProofAudit.lean](ProofAudit.lean) | Theorem axiom-dependency reports |
| [.github/workflows/lean.yml](.github/workflows/lean.yml) | Automatic Lean CI |
| [ZOO_46_REPORT.md](ZOO_46_REPORT.md) | Adapted Zoo review |
| [ZOO_46_MATRIX.csv](ZOO_46_MATRIX.csv) | Per-animal screening matrix |
| [ABLATIONS.md](ABLATIONS.md) | Sideways-move and other ablations |
| [experiment.py](experiment.py) | Exhaustive finite experiment |
| [test_experiment.py](test_experiment.py) | Python tests |
| [results.csv](results.csv) | Recorded numerical results |
| [curve.png](curve.png) | Search-space growth figure |
| [LEAN_STATUS.md](LEAN_STATUS.md) | Original pre-build verification status (historical) |

## Next theorem target

Formalize arbitrary finite disjoint copies of the gadget and prove that every single-bit flip from the all-zero state fails to strictly improve total unsatisfied-clause cost. Then investigate stronger solver families with memory, plateau moves, restarts, and branching.
