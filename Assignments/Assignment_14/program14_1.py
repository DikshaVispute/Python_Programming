# Write a lambda function which accepts one number and returns square of that number.

Square = lambda No : No * No

def main():
    Value = int(input("Enter the number : "))

    Ret = Square(Value)

    print("Suare of the number : ",Ret)

if __name__ == "__main__":
    main()