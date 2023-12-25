def separateRuns():
    print("**********")
    print()


def addTwo(startingValue):
    endingValue = startingValue + 2
    return endingValue


# returns a result to the caller
sum1 = addTwo(5)
sum2 = addTwo(10)
print("The results of adding 2 to 5 and 2 to 10 are:", sum1, "and", sum2)
separateRuns()


def calculateAverage(param1, param2, param3, param4):
    # Add up numbers, divide by the number of numbers
    total = param1 + param2 + param3 + param4
    average = total / 4.0
    return average


average1 = calculateAverage(2, 3, 4, 5)
average2 = calculateAverage(-3, 5.2, 15, 1000.8)
average3 = calculateAverage(1.4, -2.5, 14.3, 200.5)
print("The three averages are:", average1, average2, average3)
separateRuns()

yardsOnRun1 = 4
yardsOnRun2 = 6.5
yardsOnRun3 = 2.5
yardsOnRun4 = -2
averageYardsPerRun = calculateAverage(
    yardsOnRun1, yardsOnRun2, yardsOnRun3, yardsOnRun4
)
print("Average yards per run is:", averageYardsPerRun)
separateRuns()

yardsOnPass1 = 0
yardsOnPass2 = 25.5
yardsOnPass3 = 0
yardsOnPass4 = 12
averageYardsPerPass = calculateAverage(
    yardsOnPass1, yardsOnPass2, yardsOnPass3, yardsOnPass4
)
print("Average yards per pass is:", averageYardsPerPass)
separateRuns()
