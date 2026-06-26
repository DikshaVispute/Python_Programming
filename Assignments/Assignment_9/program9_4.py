def Cube(No):
    cube = No * No * No
    return cube
    
def main():
    Value = int(input("Enter the number : "))

    Ret = Cube(Value)

    print("Cube of the number is : ",Ret)

if __name__ == "__main__":
    main()
