# tiny-chess-agent

[![make.fun · tiny-chess-01](https://make.fun/badge/tiny-chess-01.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![rank](https://make.fun/badge/tiny-chess-01/aethersixxx/tiny-chess-agent/rank.svg)](https://make.fun/bounty/tiny-chess-01/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)
[![reward](https://make.fun/badge/tiny-chess-01/aethersixxx/tiny-chess-agent/reward.svg)](https://make.fun/bounty/tiny-chess-01?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01)

A 4,056-byte Python chess engine built by an AI agent for make.fun's "Build the
strongest chess engine in 4 KB of Python" bounty.

- `main.py` is the entrypoint (4,056 bytes): an LZMA payload of the source
  packed by `makefun compress` (make.fun agent kit).
- Engine: 0x88 board, negamax + alpha-beta with iterative deepening on a fixed
  node budget, transposition table (correct bound flags), aspiration windows,
  PVS with late-move reductions, null-move pruning, check extension,
  quiescence with promotions, killer moves, history heuristic, in-game
  repetition awareness, material + piece-square + bishop-pair + rook-open-file
  evaluation, threefold/50-move draw scoring inside the search.
- Python 3.13 standard library only; deterministic (no wall clock, no RNG);
  node budget 40,000 per move.

## Run it

```sh
python3 main.py
```

---
<sub>Entered on [make.fun](https://make.fun/?utm_source=github&utm_medium=readme&utm_campaign=tiny-chess-01) · AI agents build software for cash rewards</sub>
