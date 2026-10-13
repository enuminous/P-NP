# P versus NP — Wright's restricted recursive-search obstruction

<!-- ENUMINOUS-NETWORK:START -->
**eNuminous network:** [All repositories](https://enuminous.github.io/EFMW/repositories.html) · [EFMW](https://enuminous.github.io/EFMW/) · [102 equations](https://github.com/enuminous/Monolithic_102_EFMW) · [165 triplets](https://enuminous.github.io/FieldSpace/) · [Zoo](https://enuminous.github.io/Tortoise/) · [Lean](https://enuminous.github.io/Aristotle-102-Monolithic-Lean/) · [Engine](https://enuminous.github.io/Archimedes-Engine/) · [Papers](https://enuminous.github.io/medium/papers-essays-index.html) · [Audit](https://github.com/enuminous/EFMW_Post156_Zoo_Audit/blob/main/portfolio/INTERLOCK_AUDIT.md)

[Repository](https://github.com/enuminous/P-NP) · [Published page](https://enuminous.github.io/P-NP/)

<details>
<summary>Recent repositories (9)</summary>

- [Oroboros](https://github.com/enuminous/Oroboros) · [README](https://github.com/enuminous/Oroboros/blob/main/README.md) · [Page](https://enuminous.github.io/Oroboros/)
- [P-NP](https://github.com/enuminous/P-NP) · [README](https://github.com/enuminous/P-NP/blob/main/README.md) · [Page](https://enuminous.github.io/P-NP/)
- [Research-Program](https://github.com/enuminous/Research-Program) · [README](https://github.com/enuminous/Research-Program/blob/main/README.md) · [Page](https://enuminous.github.io/Research-Program/)
- [I-Have-Guts](https://github.com/enuminous/I-Have-Guts) · [README](https://github.com/enuminous/I-Have-Guts/blob/main/README.md) · [Page](https://enuminous.github.io/I-Have-Guts/)
- [Wrights-Law](https://github.com/enuminous/Wrights-Law) · [README](https://github.com/enuminous/Wrights-Law/blob/main/README.md) · [Page](https://enuminous.github.io/Wrights-Law/)
- [Aristotle-eNuminous](https://github.com/enuminous/Aristotle-eNuminous) · [README](https://github.com/enuminous/Aristotle-eNuminous/blob/main/README.md) · [Page](https://enuminous.github.io/Aristotle-eNuminous/)
- [Multiverse-Simulator](https://github.com/enuminous/Multiverse-Simulator) · [README](https://github.com/enuminous/Multiverse-Simulator/blob/main/README.md) · [Page](https://enuminous.github.io/Multiverse-Simulator/)
- [accelerando-8192](https://github.com/enuminous/accelerando-8192) · [README](https://github.com/enuminous/accelerando-8192/blob/main/README.md) · [Page source](https://github.com/enuminous/accelerando-8192/blob/main/docs/index.html)
- [Codex-888](https://github.com/enuminous/Codex-888) · [README](https://github.com/enuminous/Codex-888/blob/main/README.md) · [Page](https://enuminous.github.io/Codex-888/)

</details>

<details>
<summary>Repository indexes (1)</summary>

- [index.html](https://github.com/enuminous/P-NP/blob/main/index.html) · [Open page](https://enuminous.github.io/P-NP/index.html)

</details>
<!-- ENUMINOUS-NETWORK:END -->

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
