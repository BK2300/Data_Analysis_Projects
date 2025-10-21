import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("Sodacan DF.csv")


print(df.describe())                  # shows the summary of numerical data
print(df.describe(include=["object"]))# shows the summary of categorical data


# 2: I wanted to start out seen the distribution of the sodacan angle.
counts = df["Angle"].dropna().value_counts().sort_index()

# 2) Tegn søjlediagram
ax = counts.plot(kind="bar")

# 3) Labels og titel
ax.set_title("Distribution of Angle")
ax.set_xlabel("Angle")
ax.set_ylabel("Count")

# 4) Skriv tallet oven på hver søjle
for i, v in enumerate(counts.values):
    ax.text(i, v, str(v), ha="center", va="bottom")

plt.show()

df["Angle"].value_counts().sort_index().plot(kind="bar", edgecolor="black")
plt.title("Distribution of Angle")
plt.xlabel("Angle")
plt.ylabel("Count")
plt.show()











