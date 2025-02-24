import MultiPlayerDice as MPD

def main():
    print("Welcome to the Dice Simulator!")
    
    player_names = MPD.get_names()
    rounds = MPD.get_rounds()

    scores = [0] * len(player_names)

    MPD.roll_dice(rounds, player_names, scores)
    MPD.final_scores(player_names, scores)

if __name__ == "__main__":
    main()

