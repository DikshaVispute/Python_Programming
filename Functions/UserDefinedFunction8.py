def  BigBazar():
    print("Inside BigBazar")

    def Amul():
        print("Inside Amul Icecream Parlour")

def main():
    BigBazar()
    Amul()              # NameError
    BigBazar.Amul()     # AttributeError    

if __name__ == "__main__":
    main()
        