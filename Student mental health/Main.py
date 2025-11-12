import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

#importing the dataset
df = pd.read_csv("Student Mental health.csv")
#see all columns
pd.set_option('display.max_columns', None)
    # print(df.head(10)) #Preview of the data set. deleting it later.

        ### overview ###
print(f"The Number of Rows = {df.shape[0]}, \n and columns = {df.shape[1]}.\n") #Overview of the amount of rows & Columns
print(df.columns) #Overview of the amount of Columns(Variables)
print(df.info()) #Datatypes used (We could also just have used this instead. To get a more cleaner code for our overview)
# How many null values do we have?
print(df.isnull().sum()) #only a single person answered 0 in age
# Lets change the value to 0, instead of been empty
# df['age'] = df['age'].str.replace("",'0')

        ### Statistics ###
# we only have Age as a discrete variable
print(df.describe())


        ### EDA ###
print('Summary statistics for numeric columns:')
print(df.describe())

# Visualize missing values via a heatmap
plt.figure(figsize=(10,6))
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title('Missing Values Heatmap')
plt.tight_layout()
plt.show()

# Distribution of Age using histogram
if 'Age' in df.columns:
    plt.figure(figsize=(8,5))
    sns.histplot(df['Age'].dropna(), kde=True, bins=20)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.tight_layout()
    plt.show()

# Count plot for 'Do you have Depression?'
if 'Do you have Depression?' in df.columns:
    plt.figure(figsize=(6,4))
    sns.countplot(x='Do you have Depression?', data=df)
    plt.title('Count of Depression Responses')
    plt.tight_layout()
    plt.show()

# Pair Plot for a subset of columns (only if enough numeric columns exist)
numeric_df = df.select_dtypes(include=[np.number])
if numeric_df.shape[1] >= 4:
    sns.pairplot(numeric_df)
    plt.suptitle('Pair Plot for Numeric Columns', y=1.02)
    plt.show()



