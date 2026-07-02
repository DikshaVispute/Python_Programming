# Write a lambda function using reduce() which accepts a list of numbers and returns the addition of
# all elements.

from functools import reduce

Addition  = lambda No1, No2 : No1 + No2

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

    RData = reduce(Addition,Data)
    print("Addition is : ",RData)

if __name__ == "__main__":
    main()