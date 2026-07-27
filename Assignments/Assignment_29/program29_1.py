# Check File Exists in Current Directory
# Problem Statement:
# Write a program which accepts a file name from the user and checks whether that file exists in the current
# directory or not.
# Input:
# Demo.txt
# Expected Output:
# Display whether Demo.txt exists or not.

import sys
import os

def CheckExist(FileName):

    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("Path not exist")
        return

    Ret = os.path.isfile(FileName)

    if(Ret == False):
        print(f"There is no such file named as {FileName} in the current directory")
    else:
        print(f"File named as {FileName} exist in current directory")

def main():
    if(len(sys.argv) == 2):
        CheckExist(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program29_1.py file_name")

if __name__ == "__main__":
    main()