# Write a program which contains one lambda function which accepts two parameters and return
# its multiplication.
# Input : 4 3 Output : 12
# Input : 6 3 Output : 18

Mult = lambda No1,No2 : (No1 * No2)

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Mult(Value1, Value2)

    print(f"Multiplication of {Value1} & {Value2} is {Ret}")

if __name__ == "__main__":
    main()