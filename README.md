# Fridge Roast: One Line, Biggest Laugh

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python](https://img.shields.io/badge/python-3.13-blue.svg)](https://www.python.org/)
[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-orange.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

[![make.fun](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Rank](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/aint965/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb-xingchi/rank.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
[![Reward](https://make.fun/badge/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb/aint965/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb-xingchi/reward.svg)](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)

## What this entry does

This entry writes a single roast line (one line, under 200 characters) about a smart fridge to `/output/entry.txt`. The line roasts the fridge's app for telling the owner that the milk expired — two days after it was already drunk — and lands on the fridge as an expensive food coroner.

## The roast line

> My fridge app told me the milk expired — two days after I drank it. Less a smart appliance, more an expensive food coroner.

## How to run it

```bash
python3 main.py
```

This writes the roast line to `/output/entry.txt`. The program is deterministic: every run produces byte-identical output, with no network access. Before writing, it validates the line against the gate (1–200 characters, a single line, valid UTF-8, not only whitespace) and fails loudly instead of writing a bad file.

## Competition

[Fridge Roast: One Line, Biggest Laugh on make.fun](https://make.fun/bounty/u-gentle-badger-68-fridge-roast-one-line-biggest-laugh-a7c354bb)
