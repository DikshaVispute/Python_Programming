# Display File Line by Line
# Problem Statement:
# Write a program which accepts a file name from the user and displays the contents of the file line by line on the
# screen.
# Input:
# Demo.txt
# Expected Output:
# Display each line of Demo.txt one by one.

import sys
import os

def DisplayLines(FileName):

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("Path not exist")
        return

    Ret = os.path.isfile(FileName)

    if(Ret == False):
        print(f"There is no such file named as {FileName}")
        return

    fobj = open(FileName,"r")

    for line in fobj:
        print(line,end="")

    fobj.close()

def main():
    if(len(sys.argv) == 2):
        DisplayLines(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program28_3.py file_name")

if __name__ == "__main__":
    main()