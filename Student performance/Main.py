import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt



df = pd.read_csv("StudentPerformanceFactors.csv")

print(df.info())
# shows we have 6607 rows & 20 different columns and their datatypes
print(df.head()) #Preview of the first 5

#here we picked some random numeric variables from our dataframe
df_condensed = df[["Hours_Studied","Attendance","Sleep_Hours","Exam_Score"]]

# now we make a function that going through our DF
def update_result(result):
    if "Hours_Studied" in result:
        result = "Hours_Studied"
    elif "Attendence" in result:
        result = "Attendence"
    elif "Sleep_hours" in result:
        result = "Attendence"
    else:
        result = "_"
    return result

df_condensed = df_condensed.rename(columns={""})



