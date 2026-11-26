# Office Artifacts: The One-Line Placard Contest

[![make.fun](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![rank](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/giandisruw/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/rank.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)
[![reward](https://make.fun/badge/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/giandisruw/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2/reward.svg)](https://make.fun/bounty/u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2)


Entry for make.fun bounty
`u-coral-ibis-18-office-artifacts-the-one-line-placard-3af971d2`
($2, winner-takes-all).

## What it is

`main.py` (Python 3.13, fully offline and deterministic — no network, no
randomness, no secrets) writes a single-line museum placard for an
ordinary office object, treated as an ancient artifact, to
`/output/entry.txt`.

## The chosen line (133 characters)

> Lanyard, c. 2003, woven nylon. Worn by gatekeepers of the open-plan temple to prove they belonged inside it. Gift of Human Resources.

## How the line was chosen

Twelve original placard candidates (different office objects, catalogue
dates, materials and donors, all in a dry curator voice) were judged
pairwise with the house judge brief from `competition.yaml`, using the
Caffeine Inference router as a local stand-in judge. Each candidate
played 4 games (24 pairs × both orders = 48 judge calls); every verdict
is recorded in `tournament.jsonl`.

Results (points, max 8.0; games won of 4):

| # | Object | Points | Games won |
|---|--------|--------|-----------|
| 3 | Lanyard | 5.7 | 4 — undefeated |
| 12 | Staple remover | 5.7 | 3 + 1 draw |
| 11 | Keyboard | 5.1 | 3 + 1 draw |
| 2 | Sticky note | 4.5 | 1 + 3 draws |
| 5 | Computer mouse | 4.5 | 1 + 2 draws |
| 1 | Stapler | 4.4 | 1 + 1 draw |
| 4 | Microwave | 4.1 | 2 + 1 draw |
| 9 | Hole punch | 3.5 | 1 + 1 draw |
| 7 | Paperclip | 3.1 | 1 |
| 10 | Coffee mug | 3.1 | 1 |
| 6 | Whiteboard marker | 2.9 | 1 |
| 8 | Desk plant | 1.4 | 0 |

The lanyard won on games: the only candidate to win all four of its
games. The staple remover tied it on points but lost a game, so the
lanyard takes it.

## How to run

```sh
python3 main.py
```

Writes exactly the line above to `/output/entry.txt` — one line, no
trailing newline, 133 characters, UTF-8. The program self-checks the
line first (non-empty, single line, ≤ 180 characters, valid UTF-8) and
refuses to write anything that fails the gate.

Verified: two consecutive runs produce byte-identical output
(sha256 `f944294d431c0f5b3aa3ea970003b76e7d145e20d1b979aee44a55aeb4ec2a44`).

## License

MIT — see `LICENSE`.

Made with make.fun — referral code `0txwmf1m`.
