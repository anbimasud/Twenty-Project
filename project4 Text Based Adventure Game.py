answer = input("Do you want to play this game? [Yes or NO]\n")

# Checking for 'yes' input (case-insensitive)
if answer.lower() == "yes":
    print("Welcome to the game!")
    answer = input("Do you want to go jungle or cave? [Jungle or Cave]\n")

    # Checking for 'yes' input (case-insensitive)
    if answer.lower() == "jungle":
        print("you see the hungry tiger 🐯Tiger will eat you.")
        print("Game Closed")

    elif answer.lower() == "cave":
        print("You seen the bear in front of cave")
        answer = input("Do you want to fight with the bear or run away! [Fight or Run]\n")

        # Checking for 'yes' input (case-insensitive)
        if answer.lower() == "fight":
            print("Bear is too much strong! you Couldn't for a bit ")
            print("You loss the game!")

        # Checking for 'yes' input (case-insensitive)
        elif answer.lower() == "run":
            print("You won the game! You are still alive")

        else:
            print("You did not enter the correct keyword.")
    else:
        print("You did not enter the correct keyword.")

# Checking for 'yes' input (case-insensitive)
elif answer.lower() == "no":
    print("You missed an adventure.")

else:
    print("You did not enter the correct keyword.")
