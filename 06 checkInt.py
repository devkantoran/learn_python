# Ask the user to enter an integer within a given range
def getIntegerInRange(prompt, lowEnd, includedHighEnd):
    while True:
        number = input(prompt)
        try:
            number = int(number)
        except:
            print("That is not an integer, please try again.")
            continue
        if (number < lowEnd) or (number > includedHighEnd):
            print(
                "The number you entered is not in between",
                lowEnd,
                "and",
                includedHighEnd,
            )
        else:
            # Everything OK
            return number


# Ask user to give a number between -5 and 20
myInteger = getIntegerInRange("Please enter an integer:", -5, 21)
print("The number you entered was: ", myInteger)
