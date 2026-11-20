"""Run the Dugout fantasy cricket project from the repository root."""

from pathlib import Path

from haroon_dugout.loader import load_player, load_teams


BASE_DIR = Path(__file__).resolve().parent
DATA_DIR = BASE_DIR / "data"


def show_pool(players):
    """Print player counts by franchise and role."""
    by_franchise = {}
    by_role = {}
    for player in players.values():
        by_franchise[player.franchise] = by_franchise.get(player.franchise, 0) + 1
        by_role[player.role] = by_role.get(player.role, 0) + 1

    print("\nPLAYERS BY FRANCHISE")
    for franchise in sorted(by_franchise):
        print(f"  {franchise}: {by_franchise[franchise]}")

    print("\nPLAYERS BY ROLE")
    for role in sorted(by_role):
        print(f"  {role}: {by_role[role]}")


def show_team(team):
    """Print one fantasy team's details."""
    print(f"\nTeam: {team.team_name} | Owner: {team.owner}")
    for player in team.players:
        print(f"  {player}")
    print(f"Total credits: {team.total_credits():.1f}")
    captain_name = team.captain.name if team.captain else "Not selected"
    vice_name = team.vice_captain.name if team.vice_captain else "Not selected"
    print(f"Captain: {captain_name} | Vice-captain: {vice_name}")


def main():
    print("=" * 52)
    print("       DUGOUT - FANTASY CRICKET LEAGUE")
    print("=" * 52)

    players = load_player(DATA_DIR / "players.csv")
    print(f"\nPlayer pool loaded: {len(players)} players")
    show_pool(players)

    teams = load_teams(DATA_DIR / "sample_teams.csv", players)
    legal = []
    illegal = []

    print("\nSAMPLE TEAM RULE CHECKS")
    for team in teams:
        show_team(team)
        errors = team.check_rules()
        if errors:
            illegal.append(team)
            print("Status: ILLEGAL")
            for error in errors:
                print(f"  - {error}")
        else:
            legal.append(team)
            print("Status: LEGAL")

    print("\nSUMMARY")
    print(f"{len(legal)} legal, {len(illegal)} illegal out of {len(teams)} sample teams")
    print("Legal teams:", ", ".join(team.team_name for team in legal) or "None")
    print("Illegal teams:", ", ".join(team.team_name for team in illegal) or "None")

    print("\nYOUR TEAM TEMPLATE")
    print("Team name: Usman Barlas XI")
    print("Owner: usman barlas")
    print("Open data/my_team.csv and add your own 11 player IDs, captain ID, and vice-captain ID.")


if __name__ == "__main__":
    main()
