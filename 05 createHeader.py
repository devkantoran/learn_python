def createHeader(fullName, gender):
    if gender == 'm':
        title = 'Mr.'
    elif gender == 'f':
        title = 'Ms.'
    else:
        title = 'Mr. or Ms.'
    header = 'Dear ' + title + ' ' + fullName + ','
    return header


print(createHeader('John Doe', 'm'))
print(createHeader('Jane Doe', 'f'))
print(createHeader('Sam Smith', 'x'))

