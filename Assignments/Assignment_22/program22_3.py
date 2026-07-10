# For every number in the given list, count how many prime numbers
# exist between 1 and N using multiprocessing Pool.
# Example
# 10000
# 20000
# 30000
# 40000
# Display total prime count for each number.

import multiprocessing
import os

def CheckPrime(No):
    Count = 0

    for i in range(2,No+1):

        flag = True

        for j in range(2, i):
            if(i % j == 0):
                flag = False
                break

        if(flag == True):
            Count = Count + 1

    print(f"PID : {os.getpid()} | Prime count in {No} is {Count}")

def main():
    Data = [10000,20000,30000,40000]

    pobj = multiprocessing.Pool()

    pobj.map(CheckPrime,Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()