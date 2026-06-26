# Write a program which accepts one number and prints binary equivalent.

def DecimalToBinary(No):

    Binary = 0
    Place = 1

    while No != 0:
        Digit = No % 2
        Binary = Binary + Digit * Place
        Place = Place * 10
        No = No // 2

    return Binary


def main():
    Value = int(input("Enter number : "))

    Ret = DecimalToBinary(Value)

    print("Binary :", Ret)


if __name__ == "__main__":
    main()
