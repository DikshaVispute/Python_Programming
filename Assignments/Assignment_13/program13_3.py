# Write a program which accepts one number and checks whether it is perfect number or not.
# Input: 6
# Output: Perfect Number

def ChkPerfect(No):
    Sum = 0

    for i in range(1,No):
        if No % i == 0:
            Sum = Sum + i

    if Sum == No:
        return True
    else:
        return False

def main():
    Value = int(input("Enter the number : "))

    Ret = ChkPerfect(Value)

    if Ret == True:
        print("The number is perfect")
    else:
        print("The number is not perfect")

if __name__ == "__main__":
    main()

