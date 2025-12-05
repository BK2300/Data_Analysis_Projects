# main.py
import pandas as pd
from Dataclean import SodaCleaner
from EDA import SodaEDA
from Virz import SodaVisualizer

def main():
    # 1) load data
    df_raw = pd.read_csv("data/Sodacan DF.csv")

    # 2) cleaning
    cleaner = SodaCleaner(df_raw)
    df_clean = (
        cleaner
        .basic_clean()
        .clean_angles()
        .get_df()
    )

    # 3) EDA
    eda = SodaEDA(df_clean)
    eda.summary().angle_stats()

    # 4) visualisering
    viz = SodaVisualizer(df_clean)
    viz.angle_histogram()

if __name__ == "__main__":
    main()
