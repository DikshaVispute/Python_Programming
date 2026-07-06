# Write a program which accept N numbers from user and store it into List. Return Maximum
# number from that List.
# Input : Number of elements : 7
# Input Elements : 13 5 45 7 4 56 34
# Output : 56

def Maximum(Brr):
    Max = 0

    for no in Brr:
        if(no > Max):
            Max = no

    return Max

def main():
    Size = int(input("Enter the number of elements : "))
    Arr = list()

    for i in range(1,Size+1):
        No = int(input())
        Arr.append(No)
    
    Ret = Maximum(Arr)

    print("Maximum from all elements of the list is : ",Ret)
    
if __name__ == "__main__":
    main()

