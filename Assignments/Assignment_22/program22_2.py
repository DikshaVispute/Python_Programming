# Write a program that calculates factorials of multiple numbers
# simultaneously using Pool.map().
# Input
# [10,15,20,25]
# Display
# • Process ID
# • Input Number
# • Factorial

import multiprocessing
import os

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i
    
    print(f"PID : {os.getpid()} | Number : {No} | Factorial : {Fact}")

def main():
    Data = [10,15,20,25]

    pobj = multiprocessing.Pool()

    pobj.map(Factorial,Data)

    pobj.close()
    pobj.join()

if __name__ == "__main__":
    main()