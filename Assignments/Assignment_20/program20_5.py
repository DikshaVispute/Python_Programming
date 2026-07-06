# Design a Python application that creates two threads named Thread1 and Thread2.
# • Thread1 should display numbers from 1 to 50.
# • Thread2 should display numbers from 50 to 1 in reverse order.
# • Ensure that:
# ◦ Thread2 starts execution only after Thread1 has completed.
# • Use appropriate thread synchronization

import threading

def Thread1(No):
    for no in range(1,No + 1):
        print(no,end="\t")
    print()
    
def Thread2(No):
    for no in range(No, 0, -1):
        print(no,end="\t")
    print()
    
def main():
    Value = int(input("Enter the number : "))

    t1 = threading.Thread(target = Thread1, args = (Value,))
    t2 = threading.Thread(target = Thread2, args = (Value,))

    t1.start()
    t1.join()
    
    t2.start()
    t2.join()

if __name__ == "__main__":
    main()