
# Libraries and modules needed
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import pandas as pd
import Data_modelling as dm
import Analysis_plot as AP



# Load the dataset
df = pd.read_csv("car_price_dataset.csv")



# EDA (To get a overview of the dataset needs cleaning)
print(f"The Number of Rows = {df.shape[0]}, \n and columns = {df.shape[1]}.\n")
print(df.sample(20, random_state=100))
print(df.columns, "\n")  # Overview of the Columns (Variables)
print(df.info())
    # Checking for missing values
print("\nMissing values:\n", df.isna().sum().sort_values(ascending=False).head(12))
print("\nDuplicates:", df.duplicated().sum())



"""

# Data cleaning and prepare it for analysis

def changing_columns_name_values(data: pd.DataFrame) -> pd.DataFrame:

"""




















