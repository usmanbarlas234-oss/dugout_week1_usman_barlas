# Dugout — Fantasy Cricket League

A Python project for the Week 1 assignment, combining the player/team concepts, Git workflow, CSV loading, rule validation, and league examples covered in the supplied sessions.

## Project structure

```text
dugout_week1_usman_barlas/
├── data/
│   ├── players.csv        # Player pool supplied with the course material
│   ├── sample_teams.csv  # Example teams for testing
│   └── my_team.csv       # Your team template
├── haroon_dugout/
│   ├── __init__.py
│   ├── loader.py         # Reads player and team CSV files
│   ├── models.py         # Player, FantasyTeam, and League classes
│   └── rules.py          # Fantasy team validation rules
├── main.py               # Main program
├── .gitignore
└── README.md
```

## Requirements

- Python 3.9 or newer
- No third-party packages are required; the project uses Python's standard library.

## Run the project

Open a terminal in this folder and run:

```bash
python main.py
```

The program loads the player pool, displays counts by franchise and role, checks the sample teams, and prints a summary of legal and illegal teams.

## Your own team

`data/my_team.csv` is a starter template for **Usman Barlas XI**, owned by **usman barlas**. The Lahore Lions row from the course examples has not been treated as your personal team.

To complete your own XI, replace the blank fields in the row with:

- `captain`: the captain's player ID
- `vice_captain`: the vice-captain's player ID
- `players`: exactly 11 player IDs separated by semicolons (`;`)

Use IDs from `data/players.csv`. The team must follow these course rules:

- Exactly 11 players
- Maximum 100 credits
- Maximum 7 players from one franchise
- WK: 1–2, BAT: 3–5, AR: 1–3, BOWL: 3–5
- Captain and vice-captain must both be selected, must belong to the team, and must be different players

## GitHub commands

Run these commands from this project folder after creating a GitHub repository named `dugout`:

```bash
git init
git status
git add .
git commit -m "Complete Week 1 Dugout project"
git branch -M main
git remote add origin https://github.com/YOUR-USERNAME/dugout.git
git push -u origin main
```

Replace `YOUR-USERNAME` with your GitHub username. If Git says the remote already exists, use `git remote set-url origin https://github.com/YOUR-USERNAME/dugout.git`.

## Course data note

The player pool and sample team data are carried over from the supplied Sunday session ZIP. The course README attributes match data to Cricsheet and says roles and credits were set for the course from PSL 2024 and 2025 performances.
