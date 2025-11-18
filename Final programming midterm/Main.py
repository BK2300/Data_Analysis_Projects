import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv("energy.csv")

#Starting out with finding out some information about our dataframe and their datatypes:
    # we have 91250 rows/entries
    # we have 15 columns
        #There is 3 floats. 7 int. 5 categorical datatypes.
print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())

















