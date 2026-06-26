# Write a program which accepts one number and prints sum of first N natural numbers.
# Input: 5
# Output: 15

def Sum(No):
    Sum = 0
    for i in range(1,No+1):
        Sum = Sum + i

    return Sum

def main():
    Value = int(input("Enter the number : "))

    Ret = Sum(Value)
    print("Sum is : ",Ret)

if __name__ == "__main__":
    main()
