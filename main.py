import MultiPlayerDice as MPD
import time

today = time.strftime("%b %d, %Y %H:%M:%S")
print("It is now: ", today)

def main():
    player_names = MPD.get_names()
    rounds = MPD.get_rounds()
    scores = MPD.roll_dice(rounds, player_names)
    MPD.final_scores(scores)


if __name__ == "__main__":
    main()