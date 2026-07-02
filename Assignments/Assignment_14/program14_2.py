# Write a lambda function which accepts one number and returns cube of that number.

Cube = lambda No : No * No * No

def main():
    Value = int(input("Enter the number : "))

    Ret = Cube(Value)

    print("Cube of the number : ",Ret)

if __name__ == "__main__":
    main()