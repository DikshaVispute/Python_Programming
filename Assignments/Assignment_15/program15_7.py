# Write a lambda function using filter() which accepts a list of strings and returns a list of strings
# having length greater than 5.

from functools import reduce

checklen = lambda val : len(val) > 5

def main():
    Size = 0
    Data = list()

    print("Enter the number of elements")
    Size = int(input())

    print("Enter the elements : ")

    for i in range(Size):
        str = input()
        Data.append(str)

    print("Input Data is : ",Data)

    FData = list(filter(checklen,Data))
    print("Strings having length greater than 5 are : ",FData)

if __name__ == "__main__":
    main()