# Write a program which accept one number for user and check whether number is prime or not.
# Input : 5 Output : It is Prime Number

def ChkPrime(No):
    Count = 0
    for i  in range(2,No//2 + 1):
        if(No % i == 0):
            Count = Count + 1

    if(Count == 0):
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))
    
    Ret = ChkPrime(Value)

    if(Ret == True):
        print(f"{Value} is a prime number")
    else:
        print(f"{Value} is not a prime number")
    
if __name__ == "__main__":
    main()

