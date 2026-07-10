# Write a Python program using multiprocessing.Pool to calculate the
# sum of all even numbers from 1 to N for every number from the given
# list.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task
# For each number N, calculate:
# 2 + 4 + 6 + ... + N
# Expected Output Format
# Process ID : 1234
# Input Number : 1000000
# Sum of Even Numbers : 250000500000

import multiprocessing
import os 

def SumEven(No):
    Sum = 0

    for i in range(2,No+1,2):
        Sum = Sum + i

    print(f"PID : {os.getpid()} | Input Number : {No} | Sum : {Sum}")

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    pobj.map(SumEven,Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()