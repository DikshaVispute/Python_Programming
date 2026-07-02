# Write a lambda function which accepts one number and returns True if divisible by 5.

ChkDivisible = lambda No : (No % 5 == 0)

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkDivisible(Value)

    if Ret == True:
        print("The number is divisible by 5")
    else:
        print("The number is not divisible by 5")

if __name__ == "__main__":
    main()