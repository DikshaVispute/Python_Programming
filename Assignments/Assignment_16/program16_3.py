# Write a program which contains one function named as Add() which accepts two numbers
# from user and return addition of that two numbers.
# Input : 11 5 Output : 16

def Add(No1, No2):
    Ans = No1 + No2
    return Ans

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    iRet = Add(Value1, Value2)

    print("Addition is : ",iRet)

if __name__ == "__main__":
    main()