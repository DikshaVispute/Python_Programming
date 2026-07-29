# Write a program that scans a specified directory every minute.
# The task should display:
# • Directory name
# • Number of files
# • Number of subdirectories
# • Date and time of scanning
# Use the os module.
# Example output:
# Directory Scanned: E:/Data
# Total Files: 15
# Total Subdirectories: 4
# Scan Time: 25-07-2026 04:30:00 PM

import sys
import schedule
import time
import os

def Display(DirectoryName):
    FileCnt = 0
    SubDirCnt = 0

    print("Directory Scanned : ",DirectoryName)

    for FolderName, SubFolder, FileName in os.walk(DirectoryName):
    
        for fname in FileName:
            FileCnt = FileCnt + 1

        for subFol in SubFolder:
            SubDirCnt = SubDirCnt + 1

    print("Total number of files : ",FileCnt)
    print("Total number of subdirectories : ",SubDirCnt)
    print("Scan Time : ",time.strftime("%d-%m-%Y %H:%M:%S %p"))

def main():
    if(len(sys.argv) == 2):
        
        schedule.every(1).minute.do(Display,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()