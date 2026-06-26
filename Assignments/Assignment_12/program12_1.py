# Write a program which accepts one character and checks whether it is vowel or consonant.
# Input: a
# Output: Vowel

def CheckChar(ch):
    ch = ch.lower()
    
    if ch == "a" or ch == "e" or ch == "i" or ch == "o" or ch == "u":
        return True
    else:
        return False
    
def main():
    char = (input("Enter the character : "))

    Ret = CheckChar(char)

    if(Ret == True):
        print("The character is Vovel")
    else:
        print("The character is Consonent")
    
if __name__ == "__main__":
    main()