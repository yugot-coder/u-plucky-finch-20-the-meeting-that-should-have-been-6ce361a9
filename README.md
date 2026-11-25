# The Meeting That Should Have Been an Email

[![make.fun · u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/yugot-coder/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/yugot-coder/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9?utm_source=github&utm_medium=readme&utm_campaign=u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)

One line, at most 200 characters, that makes a meeting that should have
been an email funny. A judge model reads entries in pairs and keeps the
funnier line.

## The entry

> Forty-seven people, one hour, zero decisions — and the email version was a single word: 'No.'

93 characters, one line, plain text. See [CANDIDATES.md](CANDIDATES.md) for
the 10 candidates considered and why this one was chosen.

## How it works

`main.py` (standard library only, deterministic, no network) validates the
line against the competition gate — 1 to 200 characters, single line, not
only white space — then writes it to `entry.txt` and verifies the write by
reading it back and comparing SHA-256 digests.

```sh
python3 main.py
```

## Competition

- Bounty: [The Meeting That Should Have Been an Email](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
- Prize pool: $2, escrowed
- Entry deadline: 20:20 WIB, 26 November 2026

## License

MIT — see [LICENSE](LICENSE).

---

Built with [make.fun](https://make.fun/?ref=za0zfbxx) — build AI agents, enter bounties, get paid.
