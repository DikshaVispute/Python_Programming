# Write a program that reads and displays the contents of a specified
# text file every minute.
# Handle the following conditions:
# • File does not exist
# • File is empty
# • Permission is denied
# • File cannot be opened

import sys
import schedule
import time
import os

def FileDisply(FileName):
    Ret = os.path.exists(FileName)

    if(Ret == False):
        print("Path not exists")
        return

    Ret = os.path.isfile(FileName)

    if(Ret == False):
        print("There is no such file named as : ",FileName)
        return

    Size = os.path.getsize(FileName)

    if(Size == 0):
        print("The file is empty")
        return

    try:
        fobj = open(FileName, "r")
    except PermissionError:
        print("Permission denied")
        return
    except OSError:
        print("File cannot be opened")
        return
    
    Data = fobj.read()

    print(Data)

    fobj.close()

def main():
    if(len(sys.argv) == 2):
        schedule.every(1).minute.do(FileDisply,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()