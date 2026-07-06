# Write a program which accept N numbers from user and store it into List. Return Minimum
# number from that List.
# Input : Number of elements : 4
# Input Elements : 13 5 45 7
# Output : 5

def Minimum(Brr):
    Min = Brr[0]

    for no in Brr:
        if(no < Min):
            Min = no

    return Min

def main():
    Size = int(input("Enter the number of elements : "))
    Arr = list()

    for i in range(1,Size+1):
        No = int(input())
        Arr.append(No)
    
    Ret = Minimum(Arr)

    print("Minimum from all elements of the list is : ",Ret)
    
if __name__ == "__main__":
    main()

