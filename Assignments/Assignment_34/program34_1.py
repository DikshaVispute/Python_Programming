# Design automation script which display information of running processes as its name, PID,
# Username.
# Usage : ProcInfo.py

import psutil
import schedule
import time

def DisplayProcessINfo():
    fobj = open("ProcessInfoLog.txt","a")

    fobj.write("-"*50+"\n")
    fobj.write("Time : " + time.strftime("%d-%m-%Y %H:%M:%S %p") + "\n")
    fobj.write("-"*50+"\n")

    for proc in psutil.process_iter():
        try:
            fobj.write("Process Name : "+proc.name()+"\n")
            fobj.write("PID : "+str(proc.pid)+"\n")
            fobj.write("Username : "+proc.username()+"\n")
            fobj.write("-"*50+"\n")

        except(psutil.NoSuchProcess, psutil.AccessDenied):
            pass

    print("Process Information stored in logfile")

    fobj.close()

def main():
    schedule.every(30).seconds.do(DisplayProcessINfo)

    while(True):
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()