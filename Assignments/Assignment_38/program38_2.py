# Write a program to:
# • Display total number of students in the dataset
# • Count how many students Passed (FinalResult = 1)
# • Count how many students Failed (FinalResult = 0)

import pandas as pd

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    print("Total number of students in the dataset : ",len(df))

    passed = (df["FinalResult"] == 1).sum()
    print("Count of passed students : ",passed)

    Failed = (df["FinalResult"] == 0).sum()
    print("Count of Failed students : ",Failed)

def main():
    Student_Performance()

if __name__ == "__main__":
    main()