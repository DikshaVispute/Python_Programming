# User Defined Module

def ChkPrime(Brr):
    Sum = 0

    for no in Brr:
        if no <= 1:
            continue

        for i in range(2,no):
            if(no % i == 0):
                break
        else:
            Sum = Sum + no 

    return Sum