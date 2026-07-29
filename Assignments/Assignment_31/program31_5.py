# Write a program that accepts a directory name from the user and
# counts the number of files inside it every five minutes.
# Write the result into:
# DirectoryCountLog.txt
# Each entry should contain:
# • Directory path
# • Number of files
# • Date and time

import sys
import schedule
import time
import os

def Display(DirectoryName):
    FileCnt = 0

    print("Directory Scanned : ",DirectoryName)

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
    
        for fname in FileName:
            FileCnt = FileCnt + 1

    fobj = open("DirectoryCountLog.txt","a")

    fobj.write("---------------------------------------------------------------------\n")
    fobj.write("Directory Path : "+DirectoryName+ "\n")
    fobj.write("Total number of files : "+str(FileCnt)+"\n")
    fobj.write("Date and Time : "+time.strftime("%d-%m-%Y %H:%M:%S %p")+ "\n")
    fobj.write("---------------------------------------------------------------------\n")

    fobj.close()

def main():
    if(len(sys.argv) == 2):
        
        schedule.every(5).seconds.do(Display,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()