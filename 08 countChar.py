# Count a single char in another string
def countCharInString(findChar, targetString):
    count = 0
    for letter in targetString: # for each letter in the target string
        if findChar == letter: # if there is a match
            # increment the count
            count = count + 1
    return count

print(countCharInString ('s', 'Mississippi')) # expect 4
print(countCharInString ('p', 'Mississippi')) # expect 2
print(countCharInString ('q', 'Mississippi')) # expect 0
