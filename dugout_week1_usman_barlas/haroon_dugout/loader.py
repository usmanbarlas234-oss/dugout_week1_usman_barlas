"""CSV loading helpers for the Dugout fantasy cricket project."""

import csv
from pathlib import Path

from haroon_dugout.models import FantasyTeam, Player


def load_player(path):
    """Load players from a CSV file and return a dictionary keyed by player ID."""
    players = {}
    with open(path, newline="", encoding="utf-8") as file:
        for row in csv.DictReader(file):
            player = Player.from_row(row)
            players[player.player_id] = player
    return players


def team_from_row(row, players):
    """Build one FantasyTeam from a CSV row."""
    team = FantasyTeam(row["team_name"].strip(), row["owner"].strip())

    player_ids = [item.strip() for item in row.get("players", "").split(";") if item.strip()]
    for player_id in player_ids:
        if player_id not in players:
            raise ValueError(f"Unknown player ID '{player_id}' in team '{team.team_name}'.")
        team.add_player(players[player_id])

    captain_id = row.get("captain", "").strip()
    vice_captain_id = row.get("vice_captain", "").strip()
    captain = players.get(captain_id) if captain_id else None
    vice_captain = players.get(vice_captain_id) if vice_captain_id else None
    team.set_captain(captain, vice_captain)
    return team


def load_team(path, players):
    """Load the first team from a CSV file, or return None if it has no rows."""
    with open(path, newline="", encoding="utf-8") as file:
        row = next(csv.DictReader(file), None)
    return team_from_row(row, players) if row else None


def load_teams(path, players):
    """Load every team from a CSV file."""
    with open(path, newline="", encoding="utf-8") as file:
        return [team_from_row(row, players) for row in csv.DictReader(file)]
