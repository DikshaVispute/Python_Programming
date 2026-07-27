# Search a Word in File
# Problem Statement:
# Write a program which accepts a file name and a word from the user and checks whether that word is present in
# the file or not.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Display whether the word Marvellous is found in Demo.txt or not.

import sys
import os

def SearchWord(FileName, word):

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("Path not exist")
        return

    Ret = os.path.isfile(FileName)

    if(Ret == False):
        print(f"There is no such file named as {FileName}")
        return

    fobj = open(FileName,"r")

    found = False
    
    for line in fobj:
        words = line.split()

        for w in words:
            if(w == word):
                found = True

    if(found == True):
        print(f"The word {word} found in the file {FileName}")

    else:
        print(f"The word {word} found not in the file {FileName}")

    fobj.close()

def main():
    if(len(sys.argv) == 3):
        SearchWord(sys.argv[1], sys.argv[2])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program28_5.py file_name word")

if __name__ == "__main__":
    main()