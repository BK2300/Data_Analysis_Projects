# viz.py
import matplotlib.pyplot as plt
import pandas as pd

class SodaVisualizer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def angle_histogram(self):
        counts = self.df["Angle"].dropna().value_counts().sort_index()

        ax = counts.plot(kind="bar")
        ax.set_title("Distribution of Angle")
        ax.set_xlabel("Angle")
        ax.set_ylabel("Count")

        # skriv tal oven på søjlerne
        for i, v in enumerate(counts.values):
            ax.text(i, v, str(v), ha="center", va="bottom")

        plt.tight_layout()
        plt.show()
        return self
