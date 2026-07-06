# Write a program which contains one lambda function which accepts one parameter and return
# power of two.
# Input : 4 Output : 16
# Input : 6 Output : 64

PowerTwo = lambda No : (No ** 2)

def main():
    Value = int(input("Enter the number : "))

    Ret = PowerTwo(Value)

    print(f"second power of {Value} is {Ret}")

if __name__ == "__main__":
    main()