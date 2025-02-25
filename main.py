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

            roll = random.randint(1, 6)
            print(f"You rolled a {roll}")
            DiceRoll.show_dice(roll)

            if roll == 6:
                scores[player] += handle_extra_roll()
            elif roll == 1:
                print("Unlucky roll! You lose a point!")
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


def main():
    player_names = MPD.get_names()
    rounds = MPD.get_rounds()
    scores = roll_dice(rounds, player_names)
    MPD.final_scores(scores)


if __name__ == "__main__":
    main()