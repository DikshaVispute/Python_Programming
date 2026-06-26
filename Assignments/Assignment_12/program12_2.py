# Write a program which accepts one number and prints its factors.
# Input: 12
# Output: 1 2 3 4 6 12

def PrintFactors(No):
    print("Factors are : ")

    for i in range(1,No+1):
        if No % i == 0:
            print(i)
    
def main():
    Value = int(input("Enter the Number : "))

    PrintFactors(Value)
    
if __name__ == "__main__":
    main()