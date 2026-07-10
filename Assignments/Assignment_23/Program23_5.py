# Write a program that calculates factorials of multiple numbers
# simultaneously using multiprocessing.Pool.
# Input

# Data = [10, 15, 20, 25]
# Expected Task
# For every N, calculate:

# N!
# Expected Output Format
# Process ID : 1240
# Input Number : 20
# Factorial : 2432902008176640000

import multiprocessing
import os 

def Factorial(No):
    Fact = 1

    for i in range(2,No+1):
        Fact = Fact * i

    print(f"PID : {os.getpid()} | Input Number : {No} | Factorial : {Fact}")

def main():
    Data = [10, 15, 20, 25]

    pobj = multiprocessing.Pool()

    pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()