# Write a lambda function which accepts one number and returns True if number is even
# otherwise False.

ChechEven = lambda No : (No % 2 == 0)

def main():
    Value = int(input("Enter the number : "))

    Ret = ChechEven(Value)

    if Ret == True:
        print("The number is Even")
    else:
        print("The number is Odd")

if __name__ == "__main__":
    main()