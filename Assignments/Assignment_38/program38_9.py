# Create a plot showing relationship between AssignmentsCompleted and FinalResult.
# Explain your observation.

import pandas as pd
import matplotlib.pyplot as plt

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    plt.scatter(
        df["AssignmentsCompleted"],
        df["FinalResult"]
    )

    plt.title("AssignmentsCompleted vs FinalResult")
    plt.xlabel("Assignments Completed")
    plt.ylabel("Final Result")

    plt.grid(True)

    plt.show()

    print("Observation : ")
    print("Students who completed more assignments generally have a better FinalResult.")
    print("Students completing less assignments are more likely to have FinalResult 0 (Fail).")
    print("Most students who completed 5 or more assignments have FinalResult 1 (Pass).")
    print("Therefore, completing more assignments shows a positive relationship with passing.")
    
def main():
    Student_Performance()

if __name__ == "__main__":
    main()