# Design automation script which accept directory name and mail id from user and create log
# file in that directory which contains information of running processes as its name, PID,
# Username. After creating log file send that log file to the specified mail.
# Usage : ProcInfoLog.py Demo Marvellousinfosystem@gmail.com
# Demo is name of Directory.
# marvellousinfosystem@gmail.com is the mail id.

import psutil
import schedule
import time
import sys
import os
import smtplib
from email.message import EmailMessage

def SendMail(ReceiverMail, FileName):
    SenderMail = "contact.dikshav@gmail.com"
    AppPassword = "XXXX XXXX XXXX XXXX"

    msg = EmailMessage()

    msg["From"] = SenderMail
    msg["To"] = ReceiverMail
    msg["subject"] = "Process Log File"

    msg.set_content("Please find the atteached process log file.")

    fobj = open(FileName,"rb")
    FileData = fobj.read()
    fobj.close()

    msg.add_attachment(FileData,
                       maintype = "application",
                       subtype = "octet-stream",
                       filename = os.path.basename(FileName))

    smtp = smtplib.SMTP_SSL("smtp.gmail.com",465)

    smtp.login(SenderMail,AppPassword)

    smtp.send_message(msg)

    smtp.quit()

def DisplayProcessINfo(DirectoryName,MailId):
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

    SendMail(MailId, FileName)

def main():
    if(len(sys.argv) == 3):
        schedule.every(3).seconds.do(DisplayProcessINfo,sys.argv[1],sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()