# Write a program which accepts one number and prints all even numbers till that number.
# Input: 10
# Output: 2 4 6 8 10

def PrintEven(No):
    print("Even numbers in",No," are : ")

    for i in range(1,No+1):
        if i % 2 == 0:
            print(i)

def main():
    Value = int(input("Enter the number : "))

    PrintEven(Value)

if __name__ == "__main__":
    main()
