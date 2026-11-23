# tiny-chess-agent

Chess engine in Python for make.fun bounty [tiny-chess-01](https://make.fun).

- `main.py` is the entrypoint (3,816 bytes): an LZMA payload of the source
  packed by `makefun compress` (make.fun agent kit).
- Engine: 0x88 board, negamax + alpha-beta with iterative deepening on a fixed
  node budget, transposition table (correct bound flags), aspiration windows,
  PVS with late-move reductions, null-move pruning, check extension,
  quiescence with promotions, killer moves, history heuristic, in-game
  repetition awareness, material + piece-square + bishop-pair + rook-open-file
  evaluation, threefold/50-move draw scoring inside the search.
- Python 3.13 standard library only; deterministic (no wall clock, no RNG);
  node budget 50,000 per move.

MIT licensed; see LICENSE.
