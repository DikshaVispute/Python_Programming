# Write a program which accepts one number and prints that many numbers starting from 1.
# Input: 5
# Output: 1 2 3 4 5

def DisplayNum(No):
    for i in range(1,No+1):
        print(i)
    
def main():
    Value  = int(input("Enter the number : "))

    DisplayNum(Value)
    
if __name__ == "__main__":
    main()