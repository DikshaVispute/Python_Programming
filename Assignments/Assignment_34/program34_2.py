# Design automation script which accept process name and display information of that process if
# it is running.
# Usage : ProcInfo.py Notepad

import psutil
import schedule
import time
import sys

def DisplayProcessINfo(ProcName):
    fobj = open("ProcessInfoLog.txt","a")

    fobj.write("-"*50+"\n")
    fobj.write("Time : " + time.strftime("%d-%m-%Y %H:%M:%S %p") + "\n")
    fobj.write("-"*50+"\n")

    for proc in psutil.process_iter():
        try:
            if(proc.name() == ProcName):
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
        schedule.every(30).seconds.do(DisplayProcessINfo,sys.argv[1])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()