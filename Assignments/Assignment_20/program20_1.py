# Design a Python application that creates two separate threads named Even and Odd.
# • The Even thread should display the first 10 even numbers.
# • The Odd thread should display the first 10 odd numbers.
# • Both threads should execute independently using the threading module.
# • Ensure proper thread creation and execution.

import threading

def DisplayEven(No):
    for i in range(2,No*2+1,2):
        print(i)

def DisplayOdd(No):
    for i in range(1,No*2+1,2):
        print(i)

def main():
    Value = int(input("Enter the number : "))

    Even = threading.Thread(target = DisplayEven, args = (Value,))
    Odd = threading.Thread(target = DisplayOdd, args = (Value,))

    Even.start()
    Odd.start()

    Even.join()
    Odd.join()

if __name__ == "__main__":
    main()