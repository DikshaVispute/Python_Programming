# Write a program which accepts length and width of rectangle and prints area.  

def Area(len,br):
    area = len * br
    return area

def main():
    length = int(input("Enter length of a rectangle : "))
    breadth = int(input("Enter breadth of a rectangle : "))

    Ret = Area(length,breadth)

    print("Area of rectangle is : ", Ret)

if __name__ == "__main__":
    main()

