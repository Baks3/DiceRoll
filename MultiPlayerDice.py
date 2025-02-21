import random
import DiceRoll

print("Welcome to the Dice Simulator!")
num_players = int(input("Enter the number of players: "))
rounds = int(input("Enter the number of rounds: "))

scores = []
player_names = []
for num in range(num_players):
    scores.append(0)
    player = input(f"Player {num + 1} enter your name: ")
    player_names.append(player)

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}")
    for player in range(num_players):
        input(f"{player_names[player]}, press Enter to roll the dice...")
        number = random.randint(1, 6)
        print(f"You rolled a {number}\n")
        DiceRoll.show_dice(number)

        if number == 6:
            print("Lucky roll! You get an extra roll!")
            extra_roll = random.randint(1, 6)
            print(f"Extra roll: You rolled a {extra_roll}\n")
            DiceRoll.show_dice(extra_roll)
            scores[player] += extra_roll

        elif number == 1:
            print("Unlucky roll! You lose a point!")
            scores[player] -= 1
        else:
            scores[player] += number

        
        print(f"{player_names[player]}'s score: {scores[player]}")

    if random.choice([True, False]):
        print("Double points round! All points this round are doubled.")
        for player in range(num_players):
            scores[player] *= 2
            print(f"{player_names[player]}'s score after doubling: {scores[player]}")

print("\nFinal Scores:")
for player in range(num_players):
    print(f"{player_names[player]}: {scores[player]}")

high_score = max(scores)
winner = scores.index(high_score)
print(f"\nCongratulations, {player_names[winner]} wins! With a score of {high_score}")
