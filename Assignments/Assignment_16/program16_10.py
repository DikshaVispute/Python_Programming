# Write a program which accept name from user and display length of its name.
# Input : Marvellous Output : 10

def DisplayLen(Name):
    return len(Name)

def main():
    Str = input("Enter your name : ")

    Ret = DisplayLen(Str)

    print("Length : ",Ret)

if __name__ == "__main__":
    main()