# Design a Python application that creates two threads.
# • Thread 1 should calculate and display the maximum element from an list.
# • Thread 2 should calculate and display the minimum element from the same list.
# • The list should be accepted from the user.

import threading

def Maximum(Brr):
    Max = 0

    for no in Brr: 
        if no > Max:
            Max = no
            
    print("Maximum element is : ",Max)

def Minimum(Brr):
    Min = Brr[0]
    
    for no in Brr: 
        if no < Min:
            Min = no

    print("Minimum element is : ",Min)
    
def main():
    Size = int(input("Enter number of elements : "))

    Arr = list()

    for i in range(Size):
        No = int(input())
        Arr.append(No)

    t1 = threading.Thread(target = Maximum, args = (Arr,))
    t2 = threading.Thread(target = Minimum, args = (Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()