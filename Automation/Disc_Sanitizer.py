#########################################################################
#
#   importing required libraries
#
#########################################################################

import os
import hashlib
import sys
import schedule
import smtplib
import time
from email.message import EmailMessage

#########################################################################
#
#   Function Name : CalculateChecksum
#   Input         : Name of File
#   Output        : MD5 Checksum of the File
#   Description   : Calculates the MD5 checksum of the specified file
#   Date          : 19/07/2026
#   Author        : Diksha Kadu Vispute
#
#########################################################################

def CalculateChecksum(FileName):
    fobj = open(FileName,"rb")

    hobj = hashlib.md5()

    Buffer = fobj.read(1024)

    while(len(Buffer) > 0):
        hobj.update(Buffer)
        Buffer = fobj.read(1024)

    fobj.close()

    return hobj.hexdigest()

#########################################################################
#
#   Function Name : FindDuplicate
#   Input         : Name of Directory
#   Output        : Dictionary of Duplicate Files and Total File Count
#   Description   : Finds duplicate files in the specified directory
#                   using MD5 checksum comparison
#   Date          : 19/07/2026
#   Author        : Diksha Kadu Vispute
#
#########################################################################

def FindDuplicate(DirectoryName):

    Ret = os.path.exists(DirectoryName)

    if(Ret == False):
        print("Path is invalid")
        return None,None

    Ret = os.path.isdir(DirectoryName)

    if(Ret == False):
        print("It is not a directory")
        return None,None

    Duplicate = {}

    TotalFiles = 0

    for FolderName,SubFolder,FileName in os.walk(DirectoryName):

        for fname in FileName:

            fname = os.path.join(FolderName,fname)

            TotalFiles = TotalFiles + 1

            Checksum = CalculateChecksum(fname)

            if Checksum in Duplicate:

                Duplicate[Checksum].append(fname)

            else:

                Duplicate[Checksum] = [fname]

    return Duplicate,TotalFiles

#########################################################################
#
#   Function Name : DeleteDuplicate
#   Input         : Dictionary containing duplicate file groups
#   Output        : Deleted File List, Total Deleted Files,
#                   Total Duplicate Groups
#   Description   : Deletes duplicate files while retaining one copy
#   Date          : 19/07/2026
#   Author        : Diksha Kadu Vispute
#
#########################################################################

def DeleteDuplicate(MyDict):

    Result = list(filter(lambda x : len(x) > 1, MyDict.values()))

    DeletedFiles = []

    Count = 0

    TotalDeleted = 0

    for value in Result:
        for subvalue in value:
            Count = Count + 1

            if(Count > 1):
                try:
                    os.remove(subvalue)
                    DeletedFiles.append(subvalue)
                    TotalDeleted = TotalDeleted + 1

                except Exception:
                    pass

        Count = 0

    return DeletedFiles,TotalDeleted,len(Result)

#########################################################################
#
#   Function Name : SendMail
#   Input         : Receiver Email ID, Log File Name
#   Output        : Email Sent Status
#   Description   : Sends the generated log file as an email attachment
#   Date          : 19/07/2026
#   Author        : Diksha Kadu Vispute
#
#########################################################################

def SendMail(ReceiverMail, FileName):

    SenderMail = "contact.dikshav@gmail.com"

    AppPassword = "XXXX XXXX XXXX XXXX"

    try:

        msg = EmailMessage()

        msg["From"] = SenderMail
        msg["To"] = ReceiverMail
        msg["Subject"] = "Duplicate File Removal Log"

        msg.set_content("Please find the attached Duplicate File Removal log.")

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

        print("Mail sent successfully")

    except Exception as E:

        print("Unable to send mail :",E)

#########################################################################
#
#   Function Name : DuplicateFileRemoval
#   Input         : Log Folder Name, Directory Name, Receiver Email ID
#   Output        : Duplicate File Removal Log File and Email Notification
#   Description   : Finds and deletes duplicate files, generates a log
#                   file, and sends the log through email
#   Date          : 19/07/2026
#   Author        : Diksha Kadu Vispute
#
#########################################################################

def DuplicateFileRemoval(FolderName,DirectoryName,MailID):
    Border = "-" * 50

    Ret = os.path.exists(FolderName)

    if(Ret == True):

        Ret = os.path.isdir(FolderName)

        if(Ret == False):

            print("Folder exists but it is not a directory")

            return

    else:

        os.mkdir(FolderName)

        print("Log directory created successfully")

    TimeStamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    LogFile = os.path.join(FolderName,"DuplicateLog_%s.log"%TimeStamp)

    fobj = open(LogFile,"w")

    print("Log file created :",LogFile)

    fobj.write(Border+"\n")
    fobj.write("----- Duplicate File Removal Log -----\n")
    fobj.write("Log Created : "+TimeStamp+"\n")
    fobj.write(Border+"\n\n")

    DuplicateDict,TotalFiles = FindDuplicate(DirectoryName)

    if(DuplicateDict == None):

        fobj.close()

        return

    DeletedFiles,TotalDeleted,DuplicateGroups = DeleteDuplicate(DuplicateDict)

    fobj.write("Directory Name : %s\n"%DirectoryName)
    fobj.write("Total Files Scanned : %d\n"%TotalFiles)
    fobj.write("Duplicate Groups : %d\n"%DuplicateGroups)
    fobj.write("Total Deleted Files : %d\n"%TotalDeleted)

    fobj.write(Border+"\n")

    fobj.write("Deleted Files :\n\n")

    for File in DeletedFiles:

        fobj.write(File+"\n")

    fobj.write(Border+"\n")

    fobj.write("Log Completed : ")

    fobj.write(time.strftime("%d-%m-%Y %H:%M:%S %p"))

    fobj.write("\n"+Border+"\n")

    fobj.close()

    print("Duplicate files removed successfully")

    SendMail(MailID,LogFile)

#########################################################################
#
#   Function Name : main
#   Input         : Command Line Arguments
#   Output        : Executes the automation script and displays
#                   appropriate messages
#   Description   : Controls the execution of the automation script,
#                   displays help and usage information, and starts
#                   the scheduled duplicate file removal process
#   Date          : 19/07/2026
#   Author        : Diksha Kadu Vispute
#
#########################################################################

def main():
    Border = "-" * 50

    print(Border)
    print("------ Marvellous Duplicate File Removal ------")
    print(Border)

    if(len(sys.argv) == 2):

        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):

            print("This automation script is used to")
            print("1. Find duplicate files")
            print("2. Delete duplicate files")
            print("3. Generate log file")
            print("4. Send log file through email")
            print("5. Execute periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Usage :")
            print("python %s TimeInterval LogFolder DirectoryName EmailID"%sys.argv[0])

            print("Example :")
            print("python %s 10 Logs Test abc@gmail.com"%sys.argv[0])

        else:
            print("Invalid option")
            print("Use --h or --u")

    elif(len(sys.argv) == 5):

        print("Scheduler started successfully")
        print("Press Ctrl + C to stop")

        schedule.every(int(sys.argv[1])).minutes.do(
            DuplicateFileRemoval,
            sys.argv[2],
            sys.argv[3],
            sys.argv[4]
        )

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")
        print("Use --h or --u")

    print(Border)
    print("Thank You For Using Marvellous Automation")
    print(Border)

#########################################################################
#
#   Starter of the automation script
#
#########################################################################

if __name__ == "__main__":
    main()