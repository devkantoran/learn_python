# Dice - count doubles in user-defined number of rounds ... repeated

import random


# simulate rolling a six-sided die and return its value
def rollOneDie():
    # generate a random numbers between 1 and 6
    thisFace = random.randrange(1, 7)
    return thisFace


while True:
    nDoubles = 0
    maxRounds = input("How many rounds do you want to do? (Or ENTER to quit): ")
    if maxRounds == "":
        break
    try:
        maxRounds = int(maxRounds)
    except:
        print("Please enter an integer number.")
        continue  # go back to the while statement
    for roundNumber in range(0, maxRounds):
        die1 = rollOneDie()
        die2 = rollOneDie()
        if die1 == die2:
            nDoubles = nDoubles + 1
    percent = (nDoubles * 100.0) / maxRounds
    print("Out of", maxRounds, "you rolled", nDoubles, "doubles, or", percent, "%")
print("OK Bye")
