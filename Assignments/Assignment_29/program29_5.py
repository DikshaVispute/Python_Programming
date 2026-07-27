# Frequency of a String in File
# Problem Statement:
# Write a program which accepts a file name and one string from the user and returns the frequency (count of
# occurrences) of that string in the file.
# Input:
# Demo.txt Marvellous
# Expected Output:
# Count how many times "Marvellous" appears in Demo.txt.

import sys
import os

def Compare(FileName, Str):

    Ret = os.path.isfile(FileName)

    if(Ret == False):
        print(f"There is no such file named as {FileName} in the current directory")
        return

    fobj = open(FileName,"r")

    Count = 0

    for line in fobj:
        for word in (line.split()):
            if(word == Str):
                Count = Count + 1

    fobj.close()
    
    print(f"Count of word {Str} in the file {FileName} is : {Count}")
    
    
def main():
    if(len(sys.argv) == 3):
        Compare(sys.argv[1],sys.argv[2])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program29_5.py filename, string")

if __name__ == "__main__":
    main()