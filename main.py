import MultiPlayerDice as MPD
import DiceRoll
import time
import random

today = time.strftime("%b %d, %Y %H:%M:%S")
print("It is now: ", today)


def roll_dice(rounds, player_names):
    scores = {player: 0 for player in player_names}

    for round_number in range(1, rounds + 1):
        print("\nFinal Round" if round_number == rounds else f"\nRound {round_number}")

        for player in player_names:
            input(f"{player}, press Enter to roll the dice...\n")

            print("Rolling", end="", flush=True)
            for _ in range(3):  
                time.sleep(0.5)
                print(".", end="", flush=True)
            print()

            roll = random.randint(1, 6)
            print(f"You rolled a {roll}")
            DiceRoll.show_dice(roll)

            if roll == 6:
                scores[player] += handle_extra_roll()
            elif roll == 1:
                print("Unlucky roll! You lose a point!")
                if scores[player] > 0:
                    scores[player] -= 1
            else:
                roll = MPD.double_points(roll, player)
                scores[player] += roll

            print(f"\n{player}'s score: {scores[player]}\n")

    return scores


def handle_extra_roll():
    print("Lucky roll! You get an extra roll!")
    extra_roll = random.randint(1, 6)
    print(f"Extra roll: You rolled a {extra_roll}")
    DiceRoll.show_dice(extra_roll)
    return extra_roll + 6  


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


def main():
    player_names = MPD.get_names()
    rounds = MPD.get_rounds()
    scores = roll_dice(rounds, player_names)
    final_scores(scores)


if __name__ == "__main__":
    main()