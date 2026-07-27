# Display File Contents
# Problem Statement:
# Write a program which accepts a file name from the user, opens that file, and displays the entire contents on the
# console.
# Input:
# Demo.txt
# Expected Output:
# Display contents of Demo.txt on console.

import sys
import os

def DisplayContents(Source):

    Ret = os.path.exists(Source)

    if(Ret == False):
        print("Path not exist")
        return

    Ret = os.path.isfile(Source)

    if(Ret == False):
        print(f"There is no such file named as {Source} in the current directory")
        return

    fobj = open(Source,"r")
    
    Data = fobj.read()

    print(Data)

    fobj.close()
    
def main():
    if(len(sys.argv) == 2):
        DisplayContents(sys.argv[1])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program29_2.py filename")

if __name__ == "__main__":
    main()