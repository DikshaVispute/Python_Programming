# Write a Python program to load the file student_performance_ml.csv using pandas.
# Display:
# • First 5 records
# • Last 5 records
# • Total number of rows and columns
# • List of column names
# • Data types of each column

import pandas as pd

def Student_Performance():

    df = pd.read_csv("student_performance_ml.csv")

    print("First 5 records from the dataset : ")
    print(df.head())

    print("Last 5 records from the dataset : ")
    print(df.tail())

    print("Total numbers of rows and columns from the dataset : ",df.shape)

    print("Columns from the dataset : ",list(df.columns))

    print("Datatype of each column is : ",df.dtypes)

def main():
    Student_Performance()

if __name__ == "__main__":
    main()