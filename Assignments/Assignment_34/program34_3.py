# Design automation script which accept directory name from user and create log file in that
# directory which contains information of running processes as its name, PID, Username.
# Usage : ProcInfoLog.py Demo
# Demo is name of Directory.

import psutil
import schedule
import time
import sys
import os

def DisplayProcessINfo(DirectoryName):
    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        os.mkdir(DirectoryName)

    File = "File"+ time.strftime("%d_%m_%Y_%H_%M_%S") + ".txt"
    FileName = os.path.join(DirectoryName,File)

    fobj = open(FileName,"w")

    fobj.write("-"*50+"\n")
    fobj.write("Time : " + time.strftime("%d-%m-%Y %H:%M:%S %p") + "\n")
    fobj.write("-"*50+"\n")

    for proc in psutil.process_iter():
        try:
            fobj.write("Process Name : "+proc.name()+"\n")
            fobj.write("PID : "+str(proc.pid)+"\n")
            fobj.write("Username : "+proc.username()+"\n")
            fobj.write("Status : "+proc.status()+"\n")
            fobj.write("Memory : "+str(proc.memory_info())+"\n")
            fobj.write("-"*50+"\n")

        except(psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    print("Process Information stored in logfile")

    fobj.close()

def main():
    if(len(sys.argv) == 2):
        schedule.every(3).seconds.do(DisplayProcessINfo,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()