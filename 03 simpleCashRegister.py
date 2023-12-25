# Simple cash register
cost = input("Please enter the cost of the item: ")
cost = float(cost)
cash = input("Please enter the cash given: ")
cash = float(cash)
change = cash - cost
print(
    "Your item costs $" + str(cost) + " and you gave me $" + str(cash) + ". Your change is $" + str(change)
)
