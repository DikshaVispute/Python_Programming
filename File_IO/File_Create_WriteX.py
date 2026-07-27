def main():
    try:
        fobj = open("Demo.txt","w")
        print("File gets opened")

        fobj.write("Marvellous Infosyatems")
        
        fobj.close()
        
    except FileNotFoundError as fobj:
        print("File is not present at current directory")

if __name__== "__main__":
    main()