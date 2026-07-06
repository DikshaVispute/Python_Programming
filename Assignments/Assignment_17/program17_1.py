# Create on module named as Arithmetic which contains 4 functions as Add() for addition, Sub()
# for subtraction, Mult() for multiplication and Div() for division. All functions accepts two
# parameters as number and perform the operation. Write on python program which call all the
# functions from Arithmetic module by accepting the parameters from user.
 
from Arithmetic import *

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Addition(Value1, Value2)
    print("Addition is : ", Ret)

    Ret = Substraction(Value1, Value2)
    print("Substraction is : ", Ret)

    Ret = Multiplication(Value1, Value2)
    print("Multiplication is : ", Ret)

    Ret = Division(Value1, Value2)
    print("Division is : ", Ret)

if __name__ == "__main__":
    main()

