# Compound Growth Simulator

A small command-line tool that answers one question: **given a starting amount, an
annual return rate, and a target, how many years until you reach it?** It compounds
the balance year by year in a `while` loop and prints the path to the goal.

```text
Starting Amount ($): 10000
Annual Return Rate (%): 8
Target Goal ($): 20000
...
Year 9: $19,990.05
Success! Goal reached in 9 years.
```

## Why

Compounding is the most basic — and most counterintuitive — idea in finance: over
long horizons, *time* does more work than the size of each contribution. I built this
while learning Python (Angela Yu, 100 Days of Code) to make that intuition concrete
and to practice loop-driven control flow.

## Run

```bash
python3 compound-growth-loop.py
```

No third-party packages — standard library only (Python 3.8+).

## Scope & limitations

- A single fixed annual rate — no inflation, taxes, fees, or variable returns.
- Annual compounding only (not monthly or continuous).
- Floating-point math for readable output; not intended for exact financial accounting.
- A learning project, not investment advice.

---
*Created by Hakan Taşar*
