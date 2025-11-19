import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("pokemonData.csv")

#Data cleaning. Lets fill out the missing values with none
df["Type2"] = df["Type2"].fillna("None")


print(f"The Number of Rows = {df.shape[0]}, \n and columns = {df.shape[1]}.\n")
print(df.columns, "\n")  # Overview of the Columns (Variables)
print(df.info())
print()
print(df.describe())  # Where we see mean, std, range and quantiles.



#Since we work with some numeric values. I would like to start out with a correlation plot.
    # maybe it can generate some ideas along the way
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()



# Histogram counting the amount of type1 pokemon in order
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x="Type1",
              order=df["Type1"].value_counts().index)
plt.xticks(rotation=45)
plt.xlabel("Primary Type (Type1)")
plt.ylabel("Count")
plt.title("Distribution of Pokémon by Primary Type")
plt.tight_layout()
plt.show()



# Correlation heatmap on type 1 vs type 2 combinations
type_crosstab = pd.crosstab(df["Type1"], df["Type2"])

plt.figure(figsize=(12, 8))
sns.heatmap(type_crosstab, annot=False)
plt.xlabel("Secondary Type (Type2)")
plt.ylabel("Primary Type (Type1)")
plt.title("Heatmap of Pokémon Type Combinations (Type1 vs Type2)")
plt.tight_layout()
plt.show()














