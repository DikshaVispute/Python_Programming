# Write a lambda function which accepts three numbers and returns largest number.

Largest = lambda No1, No2, No3 : No1 if(No1 > No2 and No1 > No3) else(No2 if No2 > No3 and No2 > No1 else No3)

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))
    Value3 = int(input("Enter the third number : "))

    Ret = Largest(Value1, Value2, Value3)

    print("Largest number is : ",Ret)
if __name__ == "__main__":
    main()