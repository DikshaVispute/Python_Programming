# Write a program which accepts one number and checks whether it is prime or not.
# Input: 11
# Output: Prime Number

def CheckPrime(No):
    Count = 0

    for i in range(2, No):
        if No % i == 0:
            Count = Count + 1

    if Count == 0:
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = CheckPrime(Value)

    if(Ret == True):
        print("The number is prime")
    else:
        print("The number is not prime")

if __name__ == "__main__":
    main()