# FileReadWrite.py
# Functions for checking if a file exists, read from a file, write to a file

import os


def fileExists(filePath):
    exists = os.path.exists(filePath)
    return exists


def writeFile(filePath, textToWrite):
    fileHandle = open(filePath, "w")
    fileHandle.write(textToWrite)
    fileHandle.close()


def readFile(filePath):
    if not fileExists(filePath):
        print("The file, " + filePath + " does not exist - cannot read it.")
        return ""
    fileHandle = open(filePath, "r")
    data = fileHandle.read()
    fileHandle.close()
    return data


DATA_FILE_PATH = 'TestData.txt' # path to the file as a constant
stringToWriteOutToFile = 'abcdefghijklmnopqrstuvwxyz' # contents could be anything, this is just a test
writeFile(DATA_FILE_PATH, stringToWriteOutToFile)
stringReadInFromFile = readFile(DATA_FILE_PATH)
print('Read in:', stringReadInFromFile)
