# Write a program which accepts one number and prints multiplication table of that number.
# Input: 4
# Output: 4 8 12 16 20 24 28 32 36 40

def Multiplication(No):
    for i in range(1,11):
        Mult = No * i
        print(Mult)

def main():
    Value = int(input("Enter the number : "))

    Multiplication(Value)

if __name__ == "__main__":
    main()
