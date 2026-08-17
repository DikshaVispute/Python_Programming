# Create a scatter plot of:
# StudyHours vs PreviousScore
# Use different colors for Pass and Fail students.

import pandas as pd
import matplotlib.pyplot as plt

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    passed = df[df["FinalResult"] == 1]
    failed = df[df["FinalResult"] == 0]

    plt.scatter(
        passed["StudyHours"],
        passed["PreviousScore"],
        label = "Pass"
    )

    plt.scatter(
        failed["StudyHours"],
        failed["PreviousScore"],
        label = "Fail"
    )

    plt.title("StudyHours vs PreviousScore")
    plt.xlabel("Study Hours")
    plt.ylabel("Previous Score")

    plt.legend()
    plt.grid(True)

    plt.show()
    
def main():
    Student_Performance()

if __name__ == "__main__":
    main()