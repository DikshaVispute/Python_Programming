# Write a Python program that performs a file backup every hour.
# The program should:
# 1. Accept the source file path.
# 2. Accept the destination directory path.
# 3. Copy the source file to the destination directory.
# 4. Add the current date and time to the backup filename.
# 5. Write the backup operation details into:
# backup_log.txt
# Example backup filename:
# Data_25_07_2026_16_30_00.txt
# Example log entry:
# Backup completed successfully at 25-07-2026 04:30:00 PM
# Use the shutil module for file copying.
    
import schedule
import time
import datetime
import sys
import shutil
import os

def CopyData(Source,Dest):
    TimeStamp = datetime.datetime.now()
    TimeStamp = TimeStamp.strftime("%d_%m_%Y_%H_%M_%S")

    BackupFile =  "Data_" + TimeStamp + ".txt"
    BackupFile = os.path.join(Dest, BackupFile)

    shutil.copy(Source,BackupFile)

    fobj = open("backup_log.txt", "a")

    fobj.write("Backup completed successfully at : "+datetime.datetime.now().strftime("%d-%m-%Y %I:%M:%S %p")+"\n")

    fobj.close()

    print("Backup completed successfully")

def main():
    if(len(sys.argv) == 3):
        schedule.every(1).second.do(CopyData,sys.argv[1], sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")
            
if __name__ == "__main__":
    main()