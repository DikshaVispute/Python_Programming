# Write a program which accept N numbers from user and store it into List. Return addition of all
# elements from that List.
# Input : Number of elements : 6
# Input Elements : 13 5 45 7 4 56
# Output : 130

def Addition(Brr):
    Sum = 0

    for no in Brr:
        Sum = Sum + no

    return Sum

def main():
    Size = int(input("Enter the number of elements : "))
    Arr = list()

    for i in range(1,Size+1):
        No = int(input())
        Arr.append(No)
    
    Ret = Addition(Arr)

    print("Sum of elements of list is : ",Ret)
    
if __name__ == "__main__":
    main()

