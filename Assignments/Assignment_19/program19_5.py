# Write a program which contains filter(), map() and reduce() in it. Python application which
# contains one list of numbers. List contains the numbers which are accepted from user. Filter
# should filter out all prime numbers. Map function will multiply each number by 2. Reduce will
# return Maximum number from that numbers. (You can also use normal functions instead of
# lambda functions).
# Input List = [2, 70 , 11, 10, 17, 23, 31, 77]
# List after filter = [2, 11, 17, 23, 31]
# List after map = [4, 22, 34, 46, 62]
# Output of reduce = 62

from functools import reduce 

ChkPrime = lambda No : all(No % i for i in range(2,No))

MultByTwo = lambda No : (No * 2)

Maximum = lambda No1, No2 : No1 if (No1 > No2) else No2 

def main():
    Size = int(input("Enter the number of elements : "))

    Data = list()

    for i in range(Size):
        No = int(input())
        Data.append(No)
    
    FData = list(filter(ChkPrime,Data))

    print(f"Filtered elements : {FData}")

    MData = list(map(MultByTwo,FData))

    print(f"Mapped elements : {MData}")

    RData = reduce(Maximum,MData)

    print(f"Reduced data : {RData}")

if __name__ == "__main__":
    main()