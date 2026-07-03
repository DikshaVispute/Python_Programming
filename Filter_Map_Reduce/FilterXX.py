CheckEven = lambda No : (No % 2 == 0)

def main():
    Data = [13,12,8,10,11,20]

    print("Input data i : ",Data)

    FData = list(filter(CheckEven, Data))  # (Data,CheckEven) wrong sequence

    print("Data after filter : ",FData)

if __name__ == "__main__":
    main()