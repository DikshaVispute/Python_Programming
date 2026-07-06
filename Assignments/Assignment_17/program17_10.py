# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7

def SumDigit(No):
    Sum = 0
    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum

def main():
    Value = int(input("Enter the number : "))
    
    Ret = SumDigit(Value)

    print(f"Sum of digits in {Value} is {Ret}")
    
if __name__ == "__main__":
    main()

