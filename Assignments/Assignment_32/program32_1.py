# Write a program that creates a new text file every minute.
# The filename should contain the current timestamp.
# Example:
# File_25_07_2026_16_30_00.txt
# Write the following information into the file:
# • Filename
# • Creation date
# • Creation time

import sys
import schedule
import time

def Display(FileName):
    timestamp = time.strftime("%d_%m_%Y_%H_%M_%S")

    FileName = FileName + "_" + timestamp + ".txt"

    fobj = open(FileName,"w")

    fobj.write("---------------------------------------------------------------------\n")
    fobj.write("File Name : "+FileName+ "\n")
    fobj.write("Creation Date : "+time.strftime("%d-%m-%Y")+ "\n")
    fobj.write("Creation Time : "+time.strftime("%H:%M:%S %p")+ "\n")
    fobj.write("---------------------------------------------------------------------\n")

    fobj.close()

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