# Write a Python program to implement a class named Numbers with the following
# specifications:
# • The class should contain one instance variable:
# ◦ Value
# • Define a constructor (__init__) that accepts a number from the user and initializes Value.
# • Implement the following instance methods:
# ◦ ChkPrime() – returns True if the number is prime, otherwise returns False
# ◦ ChkPerfect() – returns True if the number is perfect, otherwise returns False
# ◦ Factors() – displays all factors of the number
# ◦ SumFactors() – returns the sum of all factors
# • Create multiple objects and call all methods.

class Numbers:
    
    def __init__(self, A):
        self.Value = A

    def ChkPrime(self):
        if self.Value <= 1:
            return False

        for i in range(2, self.Value):
            if self.Value % i == 0:
                return False

        return True
            
    def ChkPerfect(self):
        Sum = 0
        for i in range(1,self.Value):
            if(self.Value % i == 0):
                Sum = Sum  + i

        if(Sum == self.Value):
            return True
        else:
            return False
        
    def Factors(self):
        print(f"Factors of {self.Value} :")
        for i in range(1,self.Value + 1):
            if(self.Value % i == 0):
                print(i)

    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value + 1):
            if(self.Value % i == 0):
                Sum = Sum + i

        return Sum
    
Value = int(input("Enter the value : "))
obj = Numbers(Value)

Ret = obj.ChkPrime()

if(Ret == True):
    print(f"{Value} is a prime number")
else:
    print(f"{Value} is not a prime number")

Ret = obj.ChkPerfect()

if(Ret == True):
    print(f"{Value} is a perfect number")
else:
    print(f"{Value} is not a perfect number")

obj.Factors()

Ret = obj.SumFactors()
print(f"Sum of factors of {Value} is {Ret}")

