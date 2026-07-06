# Design a Python application that creates three threads named Small, Capital, and
# Digits.
# • All threads should accept a string as input.
# • The Small thread should count and display the number of lowercase characters.
# • The Capital thread should count and display the number of uppercase characters.
# • The Digits thread should count and display the number of numeric digits.
# • Each thread must also display:
# ◦ Thread ID
# ◦ Thread Name

import threading

def Small(Data):
    print("Thread Id of small is : ",threading.get_ident())
    print("Thread name of Small is : ",threading.current_thread().name)

    Count = 0

    for ch in Data:
        if ch.islower():
            Count = Count + 1

    print("number of lowercase character : ",Count)
    
def Capital(Data):
    print("Thread Id of Capitl is : ",threading.get_ident())
    print("Thread name of Capital is : ",threading.current_thread().name)

    Count = 0

    for ch in Data:
        if ch.isupper():
            Count = Count + 1

    print("number of uppercase character : ",Count)

def Digits(Data):
    print("Thread Id of Digits is : ",threading.get_ident())
    print("Thread name of Digit is : ",threading.current_thread().name)

    Count = 0

    for ch in Data:
        if ch.isdigit():
            Count = Count + 1

    print("number of Digits : ",Count)
    
def main():
    Str = input("Enter the string : ")

    t1 = threading.Thread(target = Small, args = (Str,))
    t2 = threading.Thread(target = Capital, args = (Str,))
    t3 = threading.Thread(target = Digits, args = (Str,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()