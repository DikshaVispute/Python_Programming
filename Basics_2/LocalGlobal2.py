
no = 11     # global variable

def Display():
    a = 21      # local variable
    print("From Display: ",no)
    print("From Display value of a is : ", a)

def Demo():
    print("From Demo value of a is : ",a)   # NameError
    print("From Demo: ",no)

Display()
Demo()