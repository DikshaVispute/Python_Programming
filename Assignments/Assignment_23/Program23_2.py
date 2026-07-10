# Write a Python program using multiprocessing.Pool to calculate the
# sum of all odd numbers from 1 to N.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Task
# For each number N, calculate:

# 1 + 3 + 5 + ... + N
# Expected Output Format

# Process ID : 1235
# Input Number : 1000000
# Sum of Odd Numbers : 250000000000

import multiprocessing
import os 

def SumOdd(No):
    Sum = 0

    for i in range(1,No,2):
        Sum = Sum + i

    print(f"PID : {os.getpid()} | Input Number : {No} | Sum : {Sum}")

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    pobj.map(SumOdd,Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()