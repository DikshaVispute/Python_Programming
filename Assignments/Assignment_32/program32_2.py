# Write a Python program that monitors the size of a specified file
# every 30 seconds.
# Write the following details into:
# FileSizeLog.txt
# • File path
# • File size in bytes
# • Date and time
# Handle the situation where the file does not exist.

import sys
import schedule
import time
import os

def FileMonitor(FileName):
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("Path not exists")
        return

    Ret = os.path.isfile(FileName)

    if(Ret == False):
        print("There is no such file named as : ",FileName)
        return

    fobj = open("FileSizeLog.txt","a")


    fobj.write("--------------------------------------------------\n")
    fobj.write("File Path : "+os.path.abspath(FileName)+"\n")
    fobj.write("File Size : "+str(os.path.getsize(FileName))+" bytes\n")
    fobj.write("Date and Time : "+time.strftime("%d-%m-%Y %H:%M:%S %p")+"\n")
    fobj.write("--------------------------------------------------\n")

    fobj.close()

def main():
    if(len(sys.argv) == 2):
        schedule.every(30).seconds.do(FileMonitor,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()