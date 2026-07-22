# Write a Python program to implement a class named BankAccount with the following
# requirements:
# • The class should contain two instance variables:
# ◦ Name (Account holder name)
# ◦ Amount (Account balance)
# • The class should contain one class variable:
# ◦ ROI (Rate of Interest), initialized to 10.5
# • Define a constructor (__init__) that accepts Name and initial Amount.
# • Implement the following instance methods:
# ◦ Display() – displays account holder name and current balance
# ◦ Deposit() – accepts an amount from the user and adds it to balance
# ◦ Withdraw() – accepts an amount from the user and subtracts it from balance
# (Ensure withdrawal is allowed only if sufficient balance exists)
# ◦ CalculateInterest() – calculates and returns interest using formula:
# Interest = (Amount * ROI) / 100
# • Create multiple objects and demonstrate all methods.

class BankAccount:

    ROI = 10.5

    def __init__(self, A, B):
        self.Name = A
        self.Amount = B

    def Display(self):
        print(f"{self.Name} have bank balance of {self.Amount} rupees")

    def Deposit(self,A):
        self.Amount = self.Amount + A
        return self.Amount

    def Withdraw(self,A):
        if(A <= self.Amount):
            self.Amount = self.Amount - A
            return self.Amount

        else:
            print("There is no sufficient balance in your accont. Current balance : ",self.Amount)

    def CalculateInterest(self):
        return ((self.Amount * BankAccount.ROI) / 100)
    

Value = int(input("Enter the amount : "))

obj1 = BankAccount("Diksha",20000)

obj1.Display()

Ret = obj1.Deposit(Value)
print("Amount after deposit : ",Ret)

Ret = obj1.Withdraw(Value)
print("Amount after Withdrawal : ",Ret)

Ret = obj1.CalculateInterest()
print("Interest : ",Ret)
 
    