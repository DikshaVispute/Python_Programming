# Based on the dataset values, analyze whether:
# • Higher StudyHours increase the chance of passing.
# • Higher Attendance improves FinalResult.
# Write your observations in 4–5 lines.

import pandas as pd

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    study_analysis = df.groupby("FinalResult")["StudyHours"].mean()

    print("Average StudyHours based on FinalResult : ")
    print(study_analysis)

    attendance_analysis = df.groupby("FinalResult")["Attendance"].mean()

    print("Average Attendance based on FinalResult : ")
    print(attendance_analysis)

    print("Observation : ")
    print("Students who study for more hours have a higher chance of passing.")
    print("The average StudyHours of passed students is higher than failed students.")
    print("Students with higher attendance have better FinalResult.")
    print("The average Attendance of passed students is higher than failed students.")
    print("Therefore StudyHours and Attendance show a positive relationship with passing.")

def main():
    Student_Performance()

if __name__ == "__main__":
    main()