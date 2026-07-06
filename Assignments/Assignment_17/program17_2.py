# Write a program which accept one number and display below pattern.
# Input : 5
# Output : 
# * * * * *
# * * * * *
# * * * * *
# * * * * *
# * * * * *

def Display(No):
    for i in range(No):
        for i in range(No):
            print("*",end = "\t")
        print()

def main():
    Value = int(input("Enter the number : "))
    Display(Value)
    
if __name__ == "__main__":
    main()

