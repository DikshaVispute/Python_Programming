# Write a program which accept N numbers from user and store it into List. Return addition of all
# prime numbers from that List. Main python file accepts N numbers from user and pass each
# number to ChkPrime() function which is part of our user defined module named as
# MarvellousNum. Name of the function from main python file should be ListPrime().
# Input : Number of elements : 11
# Input Elements : 13 5 45 7 4 56 10 34 2 5 8
# Output : 54 (13 + 5 + 7 +2 + 5)

import MarvellousNum

def ListPrime():
    Size = int(input("Enter the number of elements : "))

    Arr = list()

    for i in range(1,Size+1):
        No = int(input())
        Arr.append(No)
    
    Ret = MarvellousNum.ChkPrime(Arr)

    print(f"Addition of all prime numbers in the list is : {Ret} ")

def main():
    ListPrime()
    
if __name__ == "__main__":
    main()

