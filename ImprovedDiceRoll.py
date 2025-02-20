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

print(scores)


