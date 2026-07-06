# Write a program which accept number from user and return number of digits in that number.
# Input : 5187934 Output : 7

def CountDigit(No):
    Count = 0
    while(No != 0):
        No = No // 10
        Count = Count + 1

    return Count


def main():
    Value = int(input("Enter the number : "))
    
    Ret = CountDigit(Value)

    print(f"Number of digits in {Value} is {Ret}")
    
if __name__ == "__main__":
    main()

