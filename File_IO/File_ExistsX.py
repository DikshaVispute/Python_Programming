import os

def main():

    if(os.path.exists("Demo.txt")):
        print("File is present in current directory")
    else:
        print("there is no such file")

if __name__== "__main__":
    main()