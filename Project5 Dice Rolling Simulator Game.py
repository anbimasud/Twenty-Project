import random

DiceRolling = True

while DiceRolling:
    print(random.randint(1,6))
    PlayAgain = input("Do you want to roll again [enter Y/N]\n")
    if PlayAgain.lower() == "y":
        continue
    elif PlayAgain.lower() == "n":
        print("Game Over")
        break

    else:
        print("You press the wrong key")
        