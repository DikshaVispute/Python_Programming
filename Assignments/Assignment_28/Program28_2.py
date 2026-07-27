# Count Words in a File
# Problem Statement:
# Write a program which accepts a file name from the user and counts the total number of words in that file.
# Input:
# Demo.txt
# Expected Output:
# Total number of words in Demo.txt.

import sys
import os

def CountWords(FileName):

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
        Count = Count + len(line.split())

    fobj.close()

    print(f"Number of words in the file {FileName} are : {Count}")

def main():
    if(len(sys.argv) == 2):
        CountWords(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program28_2.py file_name")

if __name__ == "__main__":
    main()