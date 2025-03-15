import random

RandomNumber = random.randrange(1,200)

userInput = int (input ("Guess the namber: "))

if userInput > RandomNumber:
    print("Actual Number is:",RandomNumber)
    print("The number is to high")
elif RandomNumber > userInput:
    print("Actual Number is:",RandomNumber)
    print("The number is to low")
else:
    print("Actual Number is:", RandomNumber)
    print(" 'Congratulation' The number is match")