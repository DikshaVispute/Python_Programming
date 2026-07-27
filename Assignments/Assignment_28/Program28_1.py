# Count Lines in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts how many lines are present in the file.
# Input:
# Demo.txt
# Expected Output:
# Total number of lines in Demo.txt.

import sys
import os

def CountLines(FileName):

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("Path not exist")
        return

    Ret = os.path.isfile(FileName)

    if(Ret == False):
        print(f"There is no such file named as {FileName}")
        return

    fobj = open(FileName,"r")

    Count = 0

    for line in fobj:
        Count = Count + 1

    fobj.close()

    print(f"Number of lines in the file {FileName} are : {Count}")

def main():
    if(len(sys.argv) == 2):
        CountLines(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program28_1.py file_name")

if __name__ == "__main__":
    main()