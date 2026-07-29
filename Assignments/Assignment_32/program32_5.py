# Write a program that deletes all empty files from a specified
# directory every hour.
# The program should:
# • Scan the directory recursively
# • Detect files whose size is zero bytes
# • Delete the empty files
# • Store deleted file paths in a log file
# • Handle permission errors
# Test the program only on a sample directory.

import sys
import schedule
import time
import os

def DirCopy(DirectoryName, LogName):
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print(f"There is no directory named as {DirectoryName}")
        return

    fobj = open(LogName, "a")

    fobj.write("-------------------------------------------------------------\n")
    fobj.write("Copy Time : "+time.strftime("%d-%m-%Y %H:%M:%S %p")+"\n")

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
        for fname in FileName:

            FilePath = os.path.join(FolderName,fname)

            if(os.path.getsize(FilePath) == 0):
                try:
                    os.remove(FilePath)

                    fobj.write(f"{FilePath} is removed successfully\n")
                    fobj.write(f"File Path : {os.path.abspath(fname)}\n")
                    print(f"{fname} is removed successfully")

                except PermissionError:
                    print(f"Permission denied : {FilePath}")
                    fobj.write(f"Permission denied : {FilePath}\n")

    fobj.write("-------------------------------------------------------------\n")
    
    fobj.close()
    
def main():
    if(len(sys.argv) == 3):
        schedule.every(5).seconds.do(DirCopy,sys.argv[1],sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()