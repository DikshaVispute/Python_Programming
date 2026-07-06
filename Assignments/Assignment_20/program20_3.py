# Design a Python application that creates two threads named EvenList and OddList.
# • Both threads should accept a list of integers as input.
# • The EvenList thread should:
# ◦ Extract all even elements from the list.
# ◦ Calculate and display their sum.
# • The OddList thread should:
# ◦ Extract all odd elements from the list.
# ◦ Calculate and display their sum.
# • Threads should run concurrently.

import threading

def EvenList(Brr):
    Sum = 0

    for no in Brr:
        if(no % 2 == 0):
            Sum = Sum + no
    
    print(f"Sum of all even numbers is : {Sum}")

def OddList(Brr):
    Sum = 0
    
    for no in Brr:
        if(no % 2 != 0):
            Sum = Sum + no
    
    print(f"Sum of all odd numbers is : {Sum}")

def main():
    Size = int(input("Enter number of elements : "))

    Arr = list()

    for i in range(Size):
        No = int(input())
        Arr.append(No)

    t1 = threading.Thread(target = EvenList, args = (Arr,))
    t2 = threading.Thread(target = OddList, args = (Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    print("Exit from main")

if __name__ == "__main__":
    main()