import psutil
import sys
import os
import time
import schedule

def ProcessScan():
    listprocess = []

    for proc in psutil.process_iter():
        info = proc.as_dict(attrs= ["pid","name","username","status"])
        info["cpu_percent"] = proc.cpu_percent(None)
        info["memory_percent"] = proc.memory_percent()

        listprocess.append(info)

    return listprocess

def PlatformSurvillance(FolderName):
    Border = "-"*50

    Ret = False

    Ret = os.path.exists(FolderName)

    if(Ret == True):
        Ret = os.path.isdir(FolderName)

        if(Ret == False):
            print("Unable to proceed as foldername is existing but it is not a directory")
            return

    else:
        os.mkdir(FolderName)
        print("Directory for the logfile gets created successfully")

    timestamp = time.strftime("%Y-%m-%d_%H-%M-%S")

    FileName = os.path.join(FolderName,"Marvellous_%s.log" %timestamp)

    fobj = open(FileName,"w")

    print(f"LogFile gets successfully created with name : {FileName}")

    fobj.write(Border+"\n")
    fobj.write("----- Marvellous Platform Survillance System -----\n")
    fobj.write("Log file gets created at : "+timestamp+"\n")
    fobj.write(Border+"\n\n")

    fobj.write("--------------------- System Report -----------------------\n")

    # CPU Innformation
    fobj.write("Number of active CPU cores : %s\n" %psutil.cpu_count())
    fobj.write("CPU Usage : %s %%\n" %psutil.cpu_percent())
    fobj.write(Border+"\n")

    # RAM Information
    memory = psutil.virtual_memory()
    
    fobj.write("RAM Usage : %s %%\n" %memory.percent)
    fobj.write("Total RAM available : %s\n" %memory.total)
    fobj.write(Border+"\n")

    # Network Usage
    netobj = psutil.net_io_counters()

    fobj.write("Network Usage Report :\n")
    fobj.write("Sent : %.2f MB\n" %(netobj.bytes_sent /(1024 * 1024)))
    fobj.write("Receive : %.2f MB\n" %(netobj.bytes_recv /(1024 * 1024)))
    fobj.write(Border+"\n")

    # Process Log
    Data = ProcessScan()

    for info in Data:
        #fobj.write(f"{info}\n")
        fobj.write("PID : %s\n" %info.get("pid"))
        fobj.write("Name : %s\n" %info.get("name"))
        fobj.write("User Name : %s\n" %info.get("username"))
        fobj.write("Status : %s\n" %info.get("status"))
        fobj.write("CPU Usage : %.4f\n" %info.get("cpu_percent"))
        fobj.write("RAM Usage : %.2f\n" %info.get("memory_percent"))

        fobj.write(Border+"\n")

    fobj.write(Border+"\n")
    fobj.write("-------------------- End of Log File ----------------------\n")
    fobj.write(Border+"\n")

    fobj.close()

def main():
    Border = "-"*50
    print(Border)
    print("----- Marvellous Platform Survillance System -----")
    print(Border)

    # --u and --u handeling
    if(len(sys.argv) == 2):
        if(sys.argv[1] == "--h" or sys.argv[1] == "--H"):
            print("This automation script is used to perform : ")
            print("1 : It fetch the information of running processes")
            print("2 : It fetch information about the Primary Storage as RAM")
            print("3 : It fetch information about the Secondary Storage as HDD")
            print("4 : It fetch the information the microprocessor")
            print("5 : It gets auto schedule periodically")
            print("6 : It maintains all record into the log file")
            print("7 : It sends the log file through the mail periodically")

        elif(sys.argv[1] == "--u" or sys.argv[1] == "--U"):
            print("Use the automation script as : ")
            print(f"python {sys.argv[0]} Time_Interval Folder_Name")
            print("Time_Interval : Time in minutes for periodic execution")
            print("Folder_Name : Name of folder for the log file creation")

        else:
            print("Unable to proceed as there is no matching arguments")
            print("please use --h or --u flag for getting more details")

    # Acual project code
    elif(len(sys.argv) == 3):

        #print("CPU Usage : ",psutil.cpu_percent())
        print("Schedular started successfully")
        print("Press ctrl + c to abort the automation script")

        schedule.every(int(sys.argv[1])).minutes.do(PlatformSurvillance, sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    # invalid
    else:
        print("Invalid number of arguments")
        print("Unable to proceed as arguments are not matching")
        print("please use --h or --u flag for getting more details")

    print(Border)
    print("--- Thank You for using our Automation System ---")
    print(Border)


if __name__ == "__main__":
    main()