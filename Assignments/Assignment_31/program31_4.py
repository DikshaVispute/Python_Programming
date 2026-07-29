# Write a program that creates a new log file after every ten minutes.
# The filename should contain the current date and time.
# Example:
# MarvellousLog_25_07_2026_16_30_00.txt
# The file should contain:
# Log file created successfully.
# Creation Time: 25-07-2026 04:30:00 PM  ("%d-%m-%Y %H:%M:%S %p")

import sys
import schedule
import time

def CreateLog(FileName):
    TimeStamp = time.strftime("%d_%m_%Y_%H_%M_%S")

    FileName = FileName + "_" + TimeStamp + ".txt"

    fobj = open(FileName,"w")

    fobj.write("Log File created successfully\n")
    fobj.write("Creation Time : "+time.strftime("%d-%m-%Y %H:%M:%S %p"))

    print(f"Log file gets created at ",time.strftime("%d-%m-%Y %H:%M:%S %p"))

def main():
    if(len(sys.argv) == 2):
        
        schedule.every(10).minutes.do(CreateLog,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()