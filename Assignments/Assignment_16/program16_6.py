# Write a program which accept number from user and check whether that number is positive or
# negative or zero.
# Input : 11 Output : Positive Number
# Input : -8 Output : Negative Number
# Input : 0 Output : Zero

def ChkNum(No):
    if(No > 0):
        print("positive number")
    elif(No < 0):
        print("Negative number")
    else:
        print("Zero")

def main():
    Value = int(input("Enter the number : "))

    ChkNum(Value)

if __name__ == "__main__":
    main()