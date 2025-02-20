import random

print("Welcome to the Dice Simulator!")
num_players = int(input("Enter the number of players: "))
rounds = int(input("Enter the number of rounds: "))

scores = []
for _ in range(num_players):
    scores.append(0)

print(scores)

for round_number in range(1, rounds + 1):
    print(f"\nRound {round_number}")
    for player in range(num_players):
        input(f"Player {player + 1}, press Enter to roll the dice...")
        number = random.randint(1, 6)
        print(f"You rolled a {number}\n")
        scores[player] += number
        print(scores)

print("\nFinal Scores:")
for player in range(num_players):
    print(f"Player {player + 1}: {scores[player]}")

high_score = max(scores)
winner = scores.index(high_score) + 1
print(f"\nCongratulations, Player {winner} wins! With a score of {high_score}")


