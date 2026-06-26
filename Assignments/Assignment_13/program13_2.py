# Write a program which accepts radius of circle and prints area of circle.

def Area(rad):
    area = 3.14 * rad * rad
    return area

def main():
    radius = int(input("Enter radius of a circle : "))

    Ret = Area(radius)

    print("Area of circle is : ", Ret)

if __name__ == "__main__":
    main()

