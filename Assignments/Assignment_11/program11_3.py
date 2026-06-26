# Write a program which accepts one number and prints sum of digits.
# Input: 123
# Output: 6

def SumDigit(No):
    Sum = 0
    while(No != 0):
        Digit = No % 10
        No = No // 10
        Sum = Sum + Digit

    return Sum

def main():
    Value = int(input("Enter the number : "))

    Ret = SumDigit(Value)

    print("Sum of digits : ",Ret)

if __name__ == "__main__":
    main()