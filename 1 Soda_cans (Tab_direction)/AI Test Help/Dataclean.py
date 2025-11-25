# cleaning.py
import pandas as pd

class SodaCleaner:
    def __init__(self, df: pd.DataFrame):
        # gem en kopi så du ikke ødelægger originalen
        self.df = df.copy()

    def basic_clean(self):
        """Eksempel: fjern duplikerede rækker og trim whitespace."""
        self.df = self.df.drop_duplicates()
        # evt. flere ting her...
        return self  # så du kan chain'e metoder

    def clean_angles(self):
        """Eksempel: fjern NaN i 'Angle' og evt. outliers."""
        self.df = self.df.dropna(subset=["Angle"])
        # fx: self.df = self.df[self.df["Angle"].between(0, 90)]
        return self

    def get_df(self) -> pd.DataFrame:
        return self.df
