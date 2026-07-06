# Design a Python application that creates two threads named Prime and NonPrime.
# • Both threads should accept a list of integers.
# • The Prime thread should display all prime numbers from the list.
# • The NonPrime thread should display all non-prime numbers from the list.

import threading

def Prime(Brr):
    print("prime numbers : ")
    for no in Brr:
        if no > 1:
            for i in range(2,no):
                if no % i == 0:
                    break

            else:
                print(no,end="\t")

    print()
        
def NonPrime(Brr):
    print("non prime numbers : ")

    for no in Brr:
        if no <= 1:
            print(no,end="\t")
        else:
            for i in range(2,no):
                if no % i == 0:
                    print(no,end="\t")
                    break
    print()
    
def main():
    Size = int(input("Enter number of elements : "))

    Arr = list()

    for i in range(Size):
        No = int(input())
        Arr.append(No)

    t1 = threading.Thread(target = Prime, args = (Arr,))
    t2 = threading.Thread(target = NonPrime, args = (Arr,))

    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()