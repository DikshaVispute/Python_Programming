# Write a program which accepts one number and prints reverse of that number.
# Input: 123
# Output: 321

def RevDigit(No):
    Sum = 0
    while(No != 0):
        Digit = No % 10
        No = No // 10
        print(Digit)

def main():
    Value = int(input("Enter the number : "))

    RevDigit(Value)

if __name__ == "__main__":
    main()