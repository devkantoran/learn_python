def separateRuns():
    print("**********")
    print()


def getGroceries():
    print("Sugar")
    print("Butter")
    print("Apples")
    print("Peaches")
    print("Bananas")
    print("Cereal")
    separateRuns()


def getMyGroceries(item1, item2, item3, item4, item5):
    print(item1)
    print(item2)
    print(item3)
    print(item4)
    print(item5)
    separateRuns()


getGroceries()
getMyGroceries("Milk", "Flour", "Sugar", "Butter", "Eggs")


def addTwo(startingValue):
    endingValue = startingValue + 2
    print("The sum of", startingValue, "and 2 is:", endingValue)


# Call the function twice with different arguments
addTwo(5)
addTwo(10)
separateRuns()


def calculateAverage(param1, param2, param3, param4):
    # Add up numbers, divide by the number of numbers
    total = param1 + param2 + param3 + param4
    average = total / 4.0
    print("Average value is:", average)


calculateAverage(2, 3, 4, 5)
calculateAverage(-3, 5.2, 15, 1000.8)
calculateAverage(1.4, -2.5, 14.3, 200.5)
separateRuns()


