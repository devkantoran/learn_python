def separateRuns():
    print("*****************")
    print(someUndefinedVariable)
    # will cause a run time error
    print()
    # blank line


def getGroceries():
    print("milk")
    print("flour")
    print("sugar")
    print("butter")
    separateRuns()  # call another function


# Main code starts here:
getGroceries()
