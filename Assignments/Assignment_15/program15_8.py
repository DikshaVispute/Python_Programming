# Write a lambda function using filter() which accepts a list of numbers and returns a list of numbers
# divisible by both 3 and 5.

from functools import reduce

ChkDivisible = lambda No : No % 3 == 0 and No % 5 == 0

def main():
    Size = 0
    Data = list()

    print("Enter the number of elements")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        no = int(input())
        Data.append(no)

    print("Input Data is : ",Data)

    FData = list(filter(ChkDivisible,Data))
    print("Elements divisible by 3 and 5 are : ",FData)

if __name__ == "__main__":
    main()