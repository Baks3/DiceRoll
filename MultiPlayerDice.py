import random
import DiceRoll
import os



def get_names():
    valid_number = True

    while valid_number:
        try:
            num_players = int(input("Enter the number of players: "))
            player_names = []

            for num in range(num_players):
                player = input(f"Player {num + 1} enter your name: ")
                while not name_valid(player, player_names):
                    player = input(f"That name is either taken or not valid. \nPlayer {num + 1} enter your name: ")

                player_names.append(player.title())

            valid_number = False
            return player_names
        except ValueError:
            print("Please enter a number!")

def name_valid(name, names):
    if name == "" or name == " " or name.title() in names or name.isdigit():
        return False 
    return True
        

def get_rounds():
    valid_number = True

    while valid_number:
        try:
            rounds = int(input("Enter the number of rounds: "))

            valid_number = False
            return rounds
        except ValueError:
            print("Please enter a number!")


def roll_dice(rounds, player_names, scores):
    for round_number in range(1, rounds + 1):
        if round_number == rounds:
            print("\nFinal Round")
        else:
            print(f"\nRound {round_number}")
        

        for player in range(len(player_names)):
            input(f"{player_names[player]}, press Enter to roll the dice...\n")
            
            number = random.randint(1, 6)
            print(f"You rolled a {number}")
            DiceRoll.show_dice(number)

            if number == 6:
                print("Lucky roll! You get an extra roll!")
                extra_roll = random.randint(1, 6)
                print(f"Extra roll: You rolled a {extra_roll}\n")
                DiceRoll.show_dice(extra_roll)
                scores[player] += extra_roll + 6

            elif number == 1:
                print("Unlucky roll! You lose a point!")
                scores[player] -= 1
            else:
                number = double_points(number, player_names[player])
                scores[player] += number

            
            print(f"\n{player_names[player]}'s score: {scores[player]}\n")


def final_scores(player_names, scores):
    print("\nFinal Scores:")
    for player in range(len(player_names)):
        print(f"{player_names[player]}: {scores[player]}")

    high_score = max(scores)
    winner = scores.index(high_score)
    print(f"\nCongratulations, {player_names[winner]} wins! With a score of {high_score}\n")


def double_points(number, player):
    if random.choice([True, False]):
            print(f"Double points round! {player} gets his number doubled.")
            number *= 2
            print(f"{player}'s number after doubling: {number}")
    else:
        return number
    
    return number










