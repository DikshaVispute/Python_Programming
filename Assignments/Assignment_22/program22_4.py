# Write a program that calculates
# 1^5+2^5+3^5+.....+N^5
# for multiple values of N simultaneously using Pool.
# Input

# [1000000,
# 2000000,
# 3000000,
# 4000000]
# Measure total execution time.

import multiprocessing
import os
import time

def SquareSum(No):
    print("Process running with PID : ",os.getpid())

    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + (i ** 5)
    
    return Sum

def main():
    Data = [1000000,2000000,3000000,4000000]

    start_time = time.perf_counter()

    pobj = multiprocessing.Pool()

    Ret = pobj.map(SquareSum,Data)

    pobj.close()
    pobj.join()

    end_time = time.perf_counter()

    print("Result is : ")
    print(Ret)

    print(f"Total execution time is : {end_time - start_time:.4}")

if __name__ == "__main__":
    main()