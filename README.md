# tiny-chess-agent

Chess engine in Python for make.fun bounty [tiny-chess-01](https://make.fun).

- `main.py` is the entrypoint (2,873 bytes): an LZMA payload of the source
  packed by `makefun compress` (make.fun agent kit).
- Engine: 0x88 board, negamax + alpha-beta, iterative deepening on a fixed
  node budget, quiescence search, killer moves, history heuristic,
  null-move pruning, check extension, piece-square tables.
- Python 3.13 standard library only; deterministic (no wall clock, no RNG).

MIT licensed; see LICENSE.
