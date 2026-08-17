# Using pandas functions, calculate and display:
# • Average StudyHours
# • Average Attendance
# • Maximum PreviousScore
# • Minimum SleepHours

import pandas as pd

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    print("Average StudyHours : ",df["StudyHours"].mean())

    print("Average Attendance : ",df["Attendance"].mean())

    print("Maximum PreviousScore : ",df["PreviousScore"].max())

    print("Minimum SleepHours : ",df["SleepHours"].min())

def main():
    Student_Performance()

if __name__ == "__main__":
    main()