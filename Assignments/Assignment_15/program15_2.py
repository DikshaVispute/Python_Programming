# Write a lambda function using filter() which accepts a list of numbers and returns a list of even
# numbers.

ChkEven = lambda No : (No % 2 == 0)

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

    FData = list(filter(ChkEven,Data))
    print("Data after filter : ",FData)

if __name__ == "__main__":
    main()