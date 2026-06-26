# Write a program which accepts one number and prints that many numbers in reverse order.
# Input: 5
# Output: 5 4 3 2 1

def DisplayRev(No):
    for i in range(No,0,-1):
        print(i)
    
def main():
    Value  = int(input("Enter the number : "))

    DisplayRev(Value)
    
if __name__ == "__main__":
    main()