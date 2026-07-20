# Write a Python program to implement a class named Arithmetic with the following
# characteristics:
# • The class should contain two instance variables: Value1 and Value2.
# • Define a constructor (__init__) that initializes all instance variables to 0.
# • Implement the following instance methods:
# ◦ Accept() – accepts values for Value1 and Value2 from the user.
# ◦ Addition() – returns the addition of Value1 and Value2.
# ◦ Subtraction() – returns the subtraction of Value1 and Value2.
# ◦ Multiplication() – returns the multiplication of Value1 and Value2.
# ◦ Division() – returns the division of Value1 and Value2 (handle division by zero
# properly).
# • Create multiple objects of the Arithmetic class and invoke all the instance methods.

class Arithmetic:

    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        print("Enter the first number : ")
        self.Value1 = int(input())

        print("Enter the second number : ")
        self.Value2 = int(input())

    def Addition(self):
        return self.Value1 + self.Value2
    
    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Multiplication(self):
        return self.Value1 * self.Value2
    
    def Division(self):
        try:
            return self.Value1 / self.Value2
        
        except ZeroDivisionError as zobj:
            print("Exception occured due to second operand is zero : ",zobj)
    
obj = Arithmetic()

obj.Accept()

Ret = obj.Addition()
print("Addition is : ",Ret)

Ret = obj.Substraction()
print("Substraction is : ",Ret)

Ret = obj.Multiplication()
print("Multiplication is : ",Ret)

Ret = obj.Division()
print("Division is : ",Ret)


