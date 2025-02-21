import random

print("Welcome to the Dice Simulator!")
num_players = int(input("Enter the number of players: "))
rounds = int(input("Enter the number of rounds: "))

scores = []
player_names = []
for num in range(num_players):
    scores.append(0)
    player = input(f"Player {num + 1} enter your name: ")
    player_names.append(player)

print(scores)

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}")
    for player in range(num_players):
        input(f"{player_names[player]}, press Enter to roll the dice...")
        number = random.randint(1, 6)
        print(f"You rolled a {number}\n")
        scores[player] += number
        print(scores)

print("\nFinal Scores:")
for player in range(num_players):
    print(f"{player_names[player]}: {scores[player]}")

high_score = max(scores)
winner = scores.index(high_score)
print(f"\nCongratulations, {player_names[winner]} wins! With a score of {high_score}")


