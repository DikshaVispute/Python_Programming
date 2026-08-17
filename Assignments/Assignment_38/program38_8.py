# Draw a boxplot for Attendance.
# Identify if any outliers are present.

import pandas as pd
import matplotlib.pyplot as plt

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    plt.boxplot(
        df["Attendance"]
    )

    plt.title("Box Plot of Attendance")
    plt.ylabel("Attendance")

    plt.grid(True)

    plt.show()
    
def main():
    Student_Performance()

if __name__ == "__main__":
    main()