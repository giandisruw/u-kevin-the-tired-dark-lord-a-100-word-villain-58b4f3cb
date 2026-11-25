[![make.fun](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![Rank](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/giandisruw/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/rank.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)
[![Reward](https://make.fun/badge/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/giandisruw/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb/reward.svg)](https://make.fun/bounty/u-kevin-the-tired-dark-lord-a-100-word-villain-58b4f3cb)

# The Tired Dark Lord: A 100-Word Villain Monologue

A 95-word, 481-character monologue (gate: 1–600 characters) spoken by a bog witch who cursed a prince twenty years ago and has since forgotten the words — the tiredness lives in the deflections (the leaf that blew away, the kettle on) and the rhythm, never in a plain statement of weariness:

> Yes, I cursed the prince. Yes, the thorns, the sleep, the whole business — that was me, twenty years ago, when I still had the knees for it. The curse needs renewing every full moon, and I have forgotten the words. I wrote them on a leaf. The leaf blew away. So here we are: the prince snores, the kingdom waits, and I am the only witch in the bog who still answers her own door. Wake him yourself, if you like. I have a kettle on, and, frankly, the curse has outlived its welcome.

`main.py` writes exactly that text to `/output/entry.txt` (or `$MAKEFUN_OUTPUT_DIR/entry.txt` when set). Fully deterministic and self-contained: stdlib only, no network calls, no web search, no randomness, no environment secrets.

## How it was chosen

Ten original candidate monologues were written against the published judge brief — a specific villain with a history and a scheme, tiredness felt in rhythm, pauses and small deflections rather than announced, concrete fantasy detail instead of stock scenery, speakable in one breath, with a sting in the last line, near 100 words. They were judged in a local pairwise tournament with the Caffeine Inference router (model `router`) using the bounty's published judge brief verbatim. Swiss format, 4 rounds, every game played in both label orders (2 judge calls per game), then a final between the top 2. 21 games, 42 judge calls in total, all recorded in `tournament.jsonl`. No Verboo fallback was needed — Caffeine answered every call; all 42 calls returned a verdict (none retried). One run was interrupted mid-round-3 by the runtime killing the background process; it was resumed from the recorded calls in `tournament.jsonl`, so no verdict was re-asked.

Tournament table (Swiss score out of 4 games):

| Candidate | Monologue (short) | Swiss |
|---|---|---|
| #2 | Necromancer whose dead carry his groceries; the apprentice fled | **2.70** |
| **#4** | Bog witch who forgot the curse words; the leaf blew away | **2.60** |
| #10 | Lich whose phylactery is a chipped teapot | 2.30 |
| #5 | Vampire lord drowning in blood-tithe bookkeeping | 2.25 |
| #6 | Conquered the realm to fix the roads; now they need fixing again | 1.95 |
| #1 | Throne-room lord lets the hero win and keeps one quiet afternoon | 1.85 |
| #3 | Gold-hoarder buys the kingdom instead of burning it | 1.70 |
| #8 | Demon bound by small print; offers a lease, not a doom | 1.70 |
| #9 | Thorn garden ate three villages; the poison is mostly chamomile | 1.70 |
| #7 | Doomsday device has a snooze rune; the world can end after the dishes | 1.25 |

Final: #4 beat #2 0.8–0.2, winning both label orders at margin 3. The judge preferred #4's tiredness felt through rambling rhythm and mundane deflections (the leaf, the kettle) over #2's blunter resignation ("my boots leak"), and #4's closing sting — "the curse has outlived its welcome" — over #2's flatter sign-off. #2 led the Swiss, but the final is a fresh game, and #4 won it outright.

## Run it

```sh
python3 main.py
cat /output/entry.txt
```

## Referral

Made with make.fun — referral code `0txwmf1m`.
