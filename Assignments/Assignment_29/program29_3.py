# Copy File Contents into a New File (Command Line)
# Problem Statement:
# Write a program which accepts an existing file name through command line arguments, creates a new file
# named Demo.txt, and copies all contents from the given file into Demo.txt.
# Input (Command Line):
# ABC.txt
# Expected Output:
# Create Demo.txt and copy contents of ABC.txt into Demo.txt.

import sys
import os

def CopyContents(Source, Dest):

    Ret = os.path.exists(Source)

    if(Ret == False):
        print("Path not exist")
        return

    Ret = os.path.isfile(Source)

    if(Ret == False):
        print(f"There is no such file named as {Source} in the current directory")
        return

    fobj1 = open(Source,"r")
    fobj2 = open(Dest,"w")

    Data = fobj1.read()

    fobj2.write(Data)

    fobj1.close()
    fobj2.close()

    print(f"Data from file {Source} gets copied into file {Dest}")

def main():
    if(len(sys.argv) == 3):
        CopyContents(sys.argv[1],sys.argv[2])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program29_3.py Source_filename, Dest_filename")

if __name__ == "__main__":
    main()