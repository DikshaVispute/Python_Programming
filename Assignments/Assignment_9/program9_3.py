def Square(No):
    Sq = No * No
    return Sq
    
def main():
    Value = int(input("Enter the number : "))

    Ret = Square(Value)

    print("Square of the number is : ",Ret)

if __name__ == "__main__":
    main()
