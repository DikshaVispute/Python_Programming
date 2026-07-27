# Copy File Contents into Another File
# Problem Statement:
# Write a program which accepts two file names from the user.
# • First file is an existing file
# • Second file is a new file
# Copy all contents from the first file into the second file.
# Input:
# ABC.txt Demo.txt
# Expected Output:
# Contents of ABC.txt copied into Demo.txt.

import sys
import os

def CopyFile(Source, Dest):

    Ret = os.path.exists(Source)

    if(Ret == False):
        print("Path not exist")
        return

    Ret = os.path.isfile(Source)

    if(Ret == False):
        print(f"There is no such file named as {Source}")
        return

    fobj1 = open(Source,"r")
    fobj2 = open(Dest, "w")

    Data = fobj1.read()
    fobj2.write(Data)

    fobj1.close()
    fobj2.close()

    print("The data gets copied successfully")

def main():
    if(len(sys.argv) == 3):
        CopyFile(sys.argv[1], sys.argv[2])

    else:
        print("Invalid number of arguments")
        print("Run the code as : ")
        print("Program28_4.py Source_filename, Dest_filename")

if __name__ == "__main__":
    main()