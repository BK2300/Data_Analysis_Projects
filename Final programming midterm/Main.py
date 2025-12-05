import pandas as pd
import plotly_express as px

df = pd.read_csv("supply_chain_dataset1.csv")

    # Supplychain
#Starting out with finding out some information about our dataframe and their datatypes:
    # we have 91250 rows/entries
    # we have 15 columns
        #There is 3 floats. 7 int. 5 categorical datatypes.

print(df.head())

"""

print(df.info())
print(df.isnull().sum())
print(df.describe())
"""
















