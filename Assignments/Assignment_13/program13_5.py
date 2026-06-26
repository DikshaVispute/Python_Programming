# Write a program which accepts marks and displays grade.
# Condition Example:
# • ≥ 75 → Distinction
# • ≥ 60 → First Class
# • ≥ 50 → Second Class
# • < 50 → Fail

def Grades(Marks):
    if Marks >= 75:
        print("Student passed with Distinction")
    elif Marks >= 60:
        print("Student passed with First Class")
    elif Marks >= 50:
        print("Student passed with Second Class")
    elif Marks < 50:
        print("Student is failed")
    else:
        print("Invalid Marks")

def main():
    Value = int(input("Enter the marks of the student : "))

    Grades(Value)

if __name__ == "__main__":
    main()

