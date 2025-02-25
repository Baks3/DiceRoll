import random
import DiceRoll


def get_names():
    while True:
        try:
            num_players = int(input("Enter the number of players: "))
            player_names = []

            for i in range(num_players):
                player = input(f"Player {i + 1}, enter your name: ").strip()

                while not name_valid(player, player_names):
                    player = input(f"That name is either taken or not valid.\nPlayer {i + 1}, enter your name: ").strip()

                player_names.append(player.title())

            return player_names
        except ValueError:
            print("Please enter a valid number!")


def name_valid(name, names):
    return bool(name.strip()) and name.title() not in names and not name.isdigit()


def get_rounds():
    while True:
        try:
            return int(input("Enter the number of rounds: "))
        except ValueError:
            print("Please enter a valid number!")




def final_scores(scores):
    print("\nFinal Scores:")
    for player, score in scores.items():
        print(f"{player}: {score}")

    high_score = max(scores.values())
    winners = [player for player, score in scores.items() if score == high_score]

    if len(winners) == 1:
        print(f"\nCongratulations, {winners[0]} wins with a score of {high_score}!\n")
    else:
        print(f"\nIt's a tie! The winners are {', '.join(winners)} with a score of {high_score}!\n")


def double_points(number, player):
    if random.choice([True, False]):
        print(f"Double points round! {player} gets their number doubled.")
        number *= 2
        print(f"{player}'s number after doubling: {number}")
    return number



