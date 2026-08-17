# Use value_counts() to analyze the distribution of FinalResult.
# Calculate the percentage of Pass and Fail students.
# Is the dataset balanced? Justify your answer.

import pandas as pd

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    print("Distribution of Finalresult : ",df["FinalResult"].value_counts())

    percentage = df["FinalResult"].value_counts(normalize=True) * 100
    print(percentage)

    print("Dataset is reasonably balanced because the distribution of Pass and Fail students is 60% and 40%")

def main():
    Student_Performance()

if __name__ == "__main__":
    main()