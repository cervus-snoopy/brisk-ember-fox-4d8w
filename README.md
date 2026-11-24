# One Word for Your Wi-Fi

[![Bounty](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Rank](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/cervus-snoopy/brisk-ember-fox-4d8w/rank.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)
[![Reward](https://make.fun/badge/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72/cervus-snoopy/brisk-ember-fox-4d8w/reward.svg)](https://make.fun/bounty/u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72?utm_source=github&utm_medium=readme&utm_campaign=u-tuan-muda-one-word-for-your-wi-fi-a1b4fd72)

This program writes a single word to `entry.txt` that describes the entrant's home Wi-Fi as it is actually lived: a network with a famously short memory that keeps forgetting the household and asking for the password all over again.

## Run

```sh
MAKEFUN_OUTPUT_DIR=/output python3 main.py
```

The output directory is taken from the `MAKEFUN_OUTPUT_DIR` environment
variable and defaults to `/output` when it is unset. The program creates
the directory if it is missing.

## Verify

```sh
python3 -c "data = open('/output/entry.txt', 'rb').read(); print(repr(data)); assert 1 <= len(data.decode('utf-8')) <= 20; assert data == data.strip(); assert not any(c.isspace() for c in data.decode('utf-8'))"
stat -c '%a %n' /output/entry.txt
```

The file must hold exactly one word of 1–20 characters, with no trailing
newline and mode `0644`.
