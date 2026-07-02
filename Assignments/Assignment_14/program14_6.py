# Write a lambda function which accepts one number and returns True if number is odd
# otherwise False.

ChechOdd = lambda No : (No % 2 != 0)

def main():
    Value = int(input("Enter the number : "))

    Ret = ChechOdd(Value)

    if Ret == True:
        print("The number is Odd")
    else:
        print("The number is Even")

if __name__ == "__main__":
    main()