def CountCapital(Brr):

    iCount = 0

    for ch in Brr:
        if(Brr[ch] >= 65 and Brr[ch] <= 90):      # Issue
            iCount = iCount + 1

    return iCount

def main():
    print("Enter string : ")
    Arr = input()

    Ret = CountCapital(Arr)

    print("Number of capital characters are : ",Ret)
main()