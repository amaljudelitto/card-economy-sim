# Card Game Economy Simulator

A headless, Monte Carlo simulation engine for analyzing card game economies. This project simulates hundreds of thousands of matches between AI agents to identify balance issues, first-turn advantages, and anomalous card win rates.

## Setup
1. `pip install -r requirements.txt`
2. Run the simulation: `python src/simulate.py`
3. Analyze the results in `analysis/analysis.ipynb`

## Architecture
- **`engine.py`**: The core ruleset handling state, mana progression, and health.
- **`agents.py`**: Decision-making algorithms (Heuristic/Greedy and Random).
- **`simulate.py`**: The execution loop that aggregates match data into a CSV dataset.
