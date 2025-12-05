# eda.py
import pandas as pd

class SodaEDA:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def summary(self):
        print("Numeric summary:")
        print(self.df.describe())
        print("\nCategorical summary:")
        print(self.df.describe(include="object"))
        return self

    def angle_stats(self):
        print("Angle describe:")
        print(self.df["Angle"].describe())
        return self
