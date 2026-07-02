# write a lambda function using reduce() which accepts a list of numbers and returns the minimum
# element.

from functools import reduce

Minimum  = lambda No1, No2 : No1 if No1 < No2 else No2

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

    RData = reduce(Minimum,Data)
    print("Minimum element is : ",RData)

if __name__ == "__main__":
    main()