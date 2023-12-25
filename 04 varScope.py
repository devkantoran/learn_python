def myFunction():
    global someVariable  # tell Python that you are using a global variable
    someVariable = someVariable + 1


someVariable = 20
myFunction()
print(someVariable)


def myFunction2(aVariable):
    aVariable = aVariable + 1  # change a local (parameter) variable
    return aVariable  # and return it


someVariable = 20
someVariable = myFunction2(someVariable)  # pass in global, and re-assign the answer
print(someVariable)
