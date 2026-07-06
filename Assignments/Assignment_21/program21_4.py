# Design a Python application that creates two threads.
# • Thread 1 should compute the sum of elements from a list.
# • Thread 2 should compute the product of elements from the same list.
# • Return the results to the main thread and display them.

import threading

Sum = 0
Mult = 1

def Summation(Brr):
    global Sum

    for no in Brr: 
        Sum = Sum + no
            
def Product(Brr):
    global Mult
    
    for no in Brr: 
        Mult = Mult * no
    
def main():
    Size = int(input("Enter number of elements : "))

    Arr = list()

    for i in range(Size):
        No = int(input())
        Arr.append(No)

    t1 = threading.Thread(target = Summation, args = (Arr,))
    t2 = threading.Thread(target = Product, args = (Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Sum of all elements is : ",Sum)
    print("product of all elements is : ",Mult)

if __name__ == "__main__":
    main()