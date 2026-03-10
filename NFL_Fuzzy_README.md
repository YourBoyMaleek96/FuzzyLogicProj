# NFL Game Outcome Prediction — Fuzzy Inference System

A fuzzy logic system that predicts NFL game outcomes using Mamdani-style reasoning across 7 linguistic input variables, with game data loaded from Google Sheets.

---

## Project Overview

This project implements a fuzzy inference system (FIS) to predict win/loss probabilities for NFL matchups. Rather than relying on crisp binary inputs, the system models uncertainty and gradation in game statistics using Gaussian membership functions and a rule base of 30 fuzzy rules covering both favorable and unfavorable game conditions.

---

## System Design

### Input Variables (Antecedents)

| Variable | Range | Linguistic Terms |
|---|---|---|
| `PassingYards` | 0 – 400 | low, average, high |
| `RushYards` | 0 – 300 | low, average, high |
| `Sacks` | 0 – 6 | low, average, high |
| `Interceptions` | 0.4 – 1.9 | low, average, high |
| `TravelDistance` | 0 – 4500 mi | low, average, high |
| `Weather` | 0 – 1.8 | bad, ok, good |
| `HomeField` | 0 – 1.8 | away, neutral, home |

### Output Variable (Consequent)

| Variable | Range | Linguistic Terms |
|---|---|---|
| `WinningPercent` | 0 – 1.8 | Lose, Draw, Win |

All membership functions use **Gaussian curves** (`skfuzzy.gaussmf`) parameterized with empirically derived means and standard deviations.

---

## Fuzzy Rule Base

The system contains **30 fuzzy rules** split across two sets:

**Team 1 Rules (15 rules) — Win conditions**, for example:
- High passing yards + high rush yards + low sacks + low interceptions + home field + good weather → **Win**
- Average passing yards + average rush yards + neutral field + ok weather → **Win**

**Team 2 Rules (15 rules) — Lose conditions**, for example:
- Low passing yards + low rush yards + high sacks + high interceptions + away + bad weather → **Lose**
- Average passing yards + high rush yards + away field + bad weather → **Lose**

Rules are combined into a single `ControlSystem` and evaluated using **Mamdani-style inference** via scikit-fuzzy's `ControlSystemSimulation`.

---

## Data Source

Game statistics are loaded from a **Google Sheets** spreadsheet named `FuzzyData` via a Google service account.

### Required Sheet Structure

| Column | Description |
|---|---|
| Week | NFL week number (1–9) |
| Team | Team name |
| PassingYards | Passing yards for the game |
| RushYards | Rushing yards for the game |
| Sacks | Sacks allowed |
| Interceptions | Interceptions thrown |
| TravelDistance | Miles traveled to game |
| Weather | Weather score (0=bad, 1=good) |
| HomeField | Home field value (0=away, 0.5=neutral, 1=home) |

---

## Setup

### 1. Install Dependencies

```bash
pip install numpy scikit-fuzzy matplotlib pandas gspread oauth2client
```

### 2. Google Sheets Authentication

- Create a project in [Google Cloud Console](https://console.cloud.google.com/)
- Enable the **Google Sheets API** and **Google Drive API**
- Create a service account and download the JSON credentials file as `fuzzy.json`
- Share your `FuzzyData` Google Sheet with the service account email

> **Note:** Never commit `fuzzy.json` to version control. Add it to `.gitignore`.

### 3. Place Credentials

Save your service account JSON file as `fuzzy.json` in the project root directory.

---

## Usage

```bash
python fuzzy_nfl.py
```

The script processes Weeks 1–9, printing a matchup table for each week:

```
Week      Team1          Team2          Team 1 win %        Team 2 win %        Winner
1         Chiefs         Raiders        0.78                0.22                Chiefs
...
```

---

## Dependencies

| Library | Purpose |
|---|---|
| numpy | Numerical array operations and universe of discourse |
| scikit-fuzzy | Fuzzy membership functions, rules, and control system |
| matplotlib | Membership function visualization (optional) |
| pandas | Game data manipulation |
| gspread | Google Sheets API integration |
| oauth2client | Google service account authentication |

---

## Notes

- Membership function visualization is included but commented out. To view all input/output membership function plots, uncomment the block at the bottom of the script
- The system evaluates one team per matchup and derives the opponent's win probability as `1 - winning_percent_team`
- Weather and HomeField inputs are encoded as continuous numeric scores rather than categorical labels

---

## Author

**Malik Freeman**  
M.S. Software Engineering — Mercer University
