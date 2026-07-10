# Write a program that counts how many odd numbers exist between
# 1 and N.
# Input
# Data = [1000000, 2000000, 3000000, 4000000]
# Expected Output Format
# Process ID : 1237
# Input Number : 1000000
# Odd Number Count : 500000

import multiprocessing
import os 

def CountOdd(No):
    Count = 0

    for i in range(1,No,2):
        Count = Count + 1

    print(f"PID : {os.getpid()} | Input Number : {No} | Count : {Count}")

def main():
    Data = [1000000, 2000000, 3000000, 4000000]

    pobj = multiprocessing.Pool()

    pobj.map(CountOdd,Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()