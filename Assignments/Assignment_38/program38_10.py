# Plot SleepHours against FinalResult.
# Does sleeping more guarantee success? Explain.

import pandas as pd
import matplotlib.pyplot as plt

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    plt.scatter(
        df["SleepHours"],
        df["FinalResult"]
    )

    plt.title("SleepHours vs FinalResult")
    plt.xlabel("SleepHours")
    plt.ylabel("Final Result")

    plt.grid(True)

    plt.show()

    print("Observation : ")
    print("The Scatter plot shows that the studens sleeping around 7-8 hours gennerally have higher tendency to pass.")
    print("But sleeping more does not mean that student will get passed.")
    print("The FinalResult depends upon some oher factors also.")
    
def main():
    Student_Performance()

if __name__ == "__main__":
    main()