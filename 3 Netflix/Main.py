import pandas as pd
import dash
from dash import dcc, html, Input, Output
import dash_bootstrap_components as dbc
import Data_modelling as dm

import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("netflix_titles.csv")

# Clean & Prepare the data








print(f"The Number of Rows = {df.shape[0]}, \n and columns = {df.shape[1]}.\n")
print(df.columns, "\n")  # Overview of the Columns (Variables)
print(df.info())
print()

netflix_shows = df[df['type'] == 'TV Show']
netflix_movies = df[df['type'] == 'Movie']

labels = ['TV Show', 'Movie']
counts = [len(netflix_shows), len(netflix_movies)]
colors = ['blue', 'orange']

plt.figure(figsize=(6,4))
bars = plt.bar(labels, counts, color=colors)

for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width()/2,
        height,
        str(height),
        ha='center',
        va='bottom',
        fontsize=12
    )

plt.title("TV-shows vs Movies split")
plt.xlabel("Type")
plt.ylabel("Quantity")
plt.show()

plt.figure(figsize=(12,10))
sns.set(style="darkgrid")
ax = sns.countplot(x="rating", data=netflix_movies, palette="Set2", order=netflix_movies['rating'].value_counts().index[0:15])

















