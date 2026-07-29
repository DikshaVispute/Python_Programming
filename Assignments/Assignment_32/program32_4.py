# Write a program that copies all .txt files from one directory to
# another every ten minutes.
# The program should:
# • Accept source and destination directories
# • Validate both directories
# • Copy only .txt files
# • Maintain a log of copied files
# • Avoid terminating if one file cannot be copied

import sys
import schedule
import time
import os
import shutil

def DirCopy(Source, Dest):
    Ret = os.path.isdir(Source)

    if(Ret == False):
        print(f"There is no directory named as {Source}")
        return

    Ret = os.path.exists(Dest)

    if(Ret == False):
        os.mkdir(Dest)

    fobj = open("CopyLog.txt", "a")

    fobj.write("-------------------------------------------------------------\n")
    fobj.write("Copy Time : "+time.strftime("%d-%m-%Y %H:%M:%S %p")+"\n")

    for FolderName, SubFolder, FileName in os.walk(Source):
        for fname in FileName:
            if(fname.endswith(".txt")):

                SourceFile = os.path.join(FolderName, fname)
                DestFile = os.path.join(Dest,fname)

                try:
                    shutil.copy(SourceFile,DestFile)

                    print(f"Copied : {fname}")
                    fobj.write(f"Copied : {SourceFile} -> {DestFile}\n")

                except Exception as e:
                    print(f"Unable to Copy {fname} : {e}")
                    fobj.write(f"Unable to copy {SourceFile} : {e}\n")

            else:
                print(f"File {fname} does not end with .txt")
                fobj.write(f"File {fname} does not end with .txt\n")

    fobj.write("-------------------------------------------------------------\n")
    
    fobj.close()
    
def main():
    if(len(sys.argv) == 3):
        schedule.every(10).minutes.do(DirCopy,sys.argv[1],sys.argv[2])

        while(True):
            schedule.run_pending()
            time.sleep(1)

    else:
        print("Invalid number of arguments")

if __name__ == "__main__":
    main()