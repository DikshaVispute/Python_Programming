# pattern for all application

# change
def Addition(A, B):
    return A+B

#fixed
def main():
    print("Inside main function")
    Ret = Addition(10,11)
    print("Addition is : ",Ret)

#fixed
if __name__ == "__main__":
    main()