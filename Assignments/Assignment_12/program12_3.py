# Write a program which accepts two numbers and prints addition, subtraction,
# multiplication and division.

def Arithmetic(No1, No2):
    Add = No1 + No2
    Sub = No1 - No2
    Mult = No1 * No2
    Div = No1 / No2

    return Add, Sub, Mult, Div
    
    
def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret1, Ret2, Ret3, Ret4 = Arithmetic(Value1, Value2)

    print("Addition is : ",Ret1)
    print("Substraction is : ",Ret2)
    print("Multiplication is : ",Ret3)
    print("Division is : ",Ret4)
    
if __name__ == "__main__":
    main()