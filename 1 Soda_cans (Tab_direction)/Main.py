import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sodacan DF.csv")


print(df.describe())                      # shows the summary of numerical data
print(df.describe(include=["object"]))    # shows the summary of categorical data

def visualize_histogram(df):
    # I wanted to start out seen the distribution of the sodacan angle.
    counts = df["Angle"].dropna().value_counts().sort_index()

    # Draw histogram
    ax = counts.plot(kind="bar")

    # Labels & titles
    ax.set_title("Distribution of Angle")
    ax.set_xlabel("Angle")
    ax.set_ylabel("Count")

    # access the number on top of the histogram
    for i, v in enumerate(counts.values):
        ax.text(i, v, str(v), ha="center", va="bottom")

    plt.show()
    return plt

visualize_histogram(df)




""" df["Angle"].value_counts().sort_index().plot(kind="bar", edgecolor="black")
plt.title("Distribution of Angle")
plt.xlabel("Angle")
plt.ylabel("Count")
plt.show()
"""










