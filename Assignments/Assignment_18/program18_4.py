# Write a program which accept N numbers from user and store it into List. Accept one another
# number from user and return frequency of that number from List.
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 5 34 2 5 65
# Element to search : 5
# Output : 3

def Frequency(Brr,Val):
    Freq = 0

    for no in Brr:
        if(no == Val):
            Freq = Freq + 1

    return Freq

def main():
    Size = int(input("Enter the number of elements : "))
    Value = int(input("Enter an element to search : "))

    Arr = list()

    for i in range(1,Size+1):
        No = int(input())
        Arr.append(No)
    
    Ret = Frequency(Arr,Value)

    print(f"Frequency of {Value} in the list is : {Ret} ")
    
if __name__ == "__main__":
    main()

