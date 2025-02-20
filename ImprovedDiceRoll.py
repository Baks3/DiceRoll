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
    


