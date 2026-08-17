# Plot a histogram of StudyHours.
# Explain what the distribution tells you.

import pandas as pd
import matplotlib.pyplot as plt

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    plt.hist(
        df["StudyHours"],
        bins= 5,
        edgecolor = "black",
        alpha = 0.8,
        rwidth= 0.9
    )

    plt.title("Distribution of StudyHours")
    plt.xlabel("Study Hours")
    plt.ylabel("Number of students")

    plt.show()

    print("Observation : ")
    print("The histogram shows the distribution of students based on their study hours")
    print("StudyHours are in the range 1 to 8.5")
    print("Students are evenly distributed in this range")
    print("Thus highest numbers of students has study hoirs between 8 to 8.5")
    
def main():
    Student_Performance()

if __name__ == "__main__":
    main()