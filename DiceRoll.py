import random
print("This is a dice roll simulator")
x = "y"

while x == "y":
    number = random.randint(1,6)

    match number:


        case 1:
            print("----------")
            print("|        |")
            print("|    O   |")
            print("|        |")
            print("----------")
        case 2:
            print("----------")
            print("|        |")
            print("| O    O |")
            print("|        |")
            print("----------")
        case 3:
            print("----------")
            print("|    O   |")
            print("|    O   |")
            print("|    O   |")
            print("----------")
        case 4:
            print("----------")
            print("| O    O |")
            print("|        |")
            print("| O    O |")
            print("----------")
        case 5:
            print("----------")
            print("| O    O |")
            print("|    O   |")
            print("| O    O |")
            print("----------")
        case 6:
            print("----------")
            print("| O    O |")
            print("| O    O |")
            print("| O    O |")
            print("----------")
    x = input("Press 'y' to roll again or any other key to exit: ")

print("Thank you for using the dice simulator!")
    
