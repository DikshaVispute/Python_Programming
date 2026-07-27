# Compare Two Files (Command Line)
# Problem Statement:
# Write a program which accepts two file names through command line arguments and compares the contents of
# both files.
# • If both files contain the same contents, display Success
# • Otherwise display Failure
# Input (Command Line):
# Demo.txt Hello.txt
# Expected Output:
# Success OR Failure

import sys
import os

def Compare(FileName1, FileName2):

    Ret = os.path.isfile(FileName1)

    if(Ret == False):
        print(f"There is no such file named as {FileName1} in the current directory")
        return

    Ret = os.path.isfile(FileName2)

    if(Ret == False):
        print(f"There is no such file named as {FileName2} in the current directory")
        return

    fobj1 = open(FileName1,"r")
    fobj2 = open(FileName2,"r")

    Data1 = fobj1.read()
    Data2 = fobj2.read()

    if(Data1 == Data2):
        print(f"Contents from file {FileName1} and {FileName2} are same")

    else:
        print(f"Contents from file {FileName1} and {FileName2} are different")

    fobj1.close()
    fobj2.close()

def main():
    if(len(sys.argv) == 3):
        Compare(sys.argv[1],sys.argv[2])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program29_4.py filename1, filename2")

if __name__ == "__main__":
    main()