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
print(df[["Height","Weight"]].describe())  # Where we see mean, std, range and quantiles.
print(df[["Type1","Type2"]].describe(include=["object"]))
"""
* The tallest pokemon has a count of 8,8. And the Heaviest one has a Weight count of 460.
* The smallest pokemon has a count of 0,2. And the Lightest one has a Weight count of 0.1.
* The median for pokemon Height has a count of 1. And the median poke Weight has a count of 30.
= so looking at the mean, is the 3 quantile closer. But is really further away from max-value, then the min-value.
    Makes me believe there is some outlier and the distribution is heavily right-skrewed
* We have 15 unique primary type
"""


#Since we work with some numeric values. I would like to start out with a correlation plot.
    # maybe it can generate some ideas along the way
plt.figure(figsize=(10,8))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap="coolwarm")
plt.title("Correlation Heatmap")
plt.show()

Height = df["Height"]
Weight = df["Weight"]
"""plt.hist(Weight,bins=50, #"bins" is the number of bars(bins) in our histogram
                color="orange",
                edgecolor="Navy") #by degault, we dont have any colors and it looks like a big blob
plt.title("Pokemon Weight distribution")
plt.xlabel("Weight Count")
plt.ylabel("number of Pokemon")
"""
plt.hist(Height,bins=50, #"bins" is the number of bars(bins) in our histogram
                color="Cyan",
                edgecolor="Red") #by degault, we dont have any colors and it looks like a big blob
plt.title("Pokemon Height distribution")
plt.xlabel("Height Count")
plt.ylabel("number of Pokemon")
#This confirmed my assumtion with there been some outliers, which ive could have removed. But didnt

# Histogram counting the amount of type1 pokemon in order
plt.figure(figsize=(10, 6))

ax = sns.countplot(
    data=df,
    x="Type1",
    order=df["Type1"].value_counts().index
)
plt.xticks(rotation=45)
plt.xlabel("Primary Type (Type1)")
plt.ylabel("Count")
plt.title("Distribution of Pokémon by Primary Type")
plt.tight_layout()
# writting numbers on top of the bars
for p in ax.patches:
    height = p.get_height()
    ax.text(
        p.get_x() + p.get_width() / 2,
        height,
        str(height),
        ha="center",
        va="bottom"
    )
plt.show()

"""
* There is count=28 water-type pokemon as their primary type.
- 28 / 151 * 100 = 18,54%
= 18,54% of all pokemon in season1 had primary type of water. Which makes them effective to Fire-, Rock-, Ground-types
* Dragon- & Ice-types have a count=2 each
- 2 / 151 * 100 = 1,32%
= Dragon types are effective against steel types (But steel type pokemon wasnt a thing in season1) And are weak effective against Fire-, Water-, Electric- & Grass types. 
    So not a Ideal pick to battle with.
= Ice types is weak against Ice-, Fire-, Water- & steeltypes(But steel type pokemon wasnt a thing in season1) and strong against Grass-, Ground-, Flying- & Dragon.
    So its has its nice in battles.
"""


# Correlation heatmap on type 1 vs type 2 combinations
type_crosstab = pd.crosstab(df["Type1"], df["Type2"])

plt.figure(figsize=(12, 8))
ax = sns.heatmap(
    type_crosstab,
    annot=True,   # <- viser tallene
    fmt="d"       # <- 'd' fordi det er heltal (otherwise får du 1.0, 2.0, ...)
)

plt.xlabel("Secondary Type (Type2)")
plt.ylabel("Primary Type (Type1)")
plt.title("Heatmap of Pokémon Type Combinations (Type1 vs Type2)")
plt.tight_layout()
plt.show()

"""
* the correlation heatmap of type1 and type 2, show that most pokemons in season 1 had no type2.
More specifally did Normal-type pokemon have no second type. on a count of 12 out of 22
- 12 / 22 * 100 = 54,545%
= 54,545% of all normal-type pokemon has no second type. which makes them bad in league matches.

* Looking at Grass-type pokemon, is there 9 pokemon out of 12. That has Poison as their second type.
- 9 / 12 * 100 = 75%
= 75% of all grass-types have poison as their second type

* While Normal-type pokemon have a correlation count of 8 with flying-types
- 8 / 22 * 100 = 36,36%
= 36,36% of normal-type pokemon, has a second type of flying.
    Both normal- & flying types are weak against rock-types. So not ideal for battling.
"""











