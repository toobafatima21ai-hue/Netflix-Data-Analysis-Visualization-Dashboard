# ==========================================================
# NETFLIX DATA ANALYSIS PROJECT
# ==========================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os

# ==========================================================
# CREATE PLOTS FOLDER
# ==========================================================

os.makedirs("plots", exist_ok=True)

sns.set_style("whitegrid")

# ==========================================================
# PART 1 - DATA LOADING
# ==========================================================

df = pd.read_csv("netflix_titles.csv")

print("=" * 60)
print("FIRST 5 RECORDS")
print(df.head())

print("\n" + "=" * 60)
print("LAST 5 RECORDS")
print(df.tail())

print("\n" + "=" * 60)
print("DATASET INFORMATION")
print(df.info())

print("\n" + "=" * 60)
print("COLUMN NAMES")
print(df.columns.tolist())

print("\n" + "=" * 60)
print("DATASET SHAPE")
print(df.shape)

# ==========================================================
# PART 2 - DATA CLEANING
# ==========================================================

print("\n" + "=" * 60)
print("MISSING VALUES")
print(df.isnull().sum())

# Fill Missing Values

df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Unknown")
df["country"] = df["country"].fillna("Unknown")
df["rating"] = df["rating"].fillna("Unknown")

# Remove duplicates

duplicates_before = df.duplicated().sum()
df.drop_duplicates(inplace=True)

print("\nDuplicates Removed:", duplicates_before)

# Convert date column

df["date_added"] = pd.to_datetime(
    df["date_added"],
    errors="coerce"
)

# Create new columns

df["year_added"] = df["date_added"].dt.year
df["month_added"] = df["date_added"].dt.month

# Extract numeric duration

df["duration_num"] = (
    df["duration"]
    .astype(str)
    .str.extract(r"(\d+)")
)

df["duration_num"] = pd.to_numeric(
    df["duration_num"],
    errors="coerce"
)

# Rename columns

df.columns = (
    df.columns
    .str.lower()
    .str.replace(" ", "_")
)

print("\nCLEANING COMPLETED")

# ==========================================================
# PART 3 - STATISTICAL ANALYSIS
# ==========================================================

print("\n" + "=" * 60)
print("STATISTICAL SUMMARY")
print(df.describe())

numeric_cols = [
    "release_year",
    "year_added",
    "duration_num"
]

for col in numeric_cols:

    print("\n" + "-" * 40)
    print(f"Column: {col}")

    print("Mean:", df[col].mean())
    print("Median:", df[col].median())

    try:
        print("Mode:", df[col].mode()[0])
    except:
        print("Mode: N/A")

    print("Standard Deviation:", df[col].std())

# Correlation Matrix

corr = df[numeric_cols].corr()

print("\nCORRELATION MATRIX")
print(corr)

# ==========================================================
# PART 4 - DATA VISUALIZATION
# ==========================================================

# ----------------------------------------------------------
# 1 Movies vs TV Shows
# ----------------------------------------------------------

plt.figure(figsize=(8,5))
sns.countplot(data=df, x="type")
plt.title("Movies vs TV Shows")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.savefig("plots/01_movies_vs_tvshows.png")
plt.close()

# ----------------------------------------------------------
# 2 Release Year Distribution
# ----------------------------------------------------------

plt.figure(figsize=(10,5))
sns.histplot(df["release_year"], bins=30)
plt.title("Release Year Distribution")
plt.xlabel("Release Year")
plt.ylabel("Count")
plt.savefig("plots/02_release_year_distribution.png")
plt.close()

# ----------------------------------------------------------
# 3 Content Added by Year
# ----------------------------------------------------------

plt.figure(figsize=(10,5))
df["year_added"].value_counts().sort_index().plot()
plt.title("Content Added to Netflix By Year")
plt.xlabel("Year")
plt.ylabel("Count")
plt.savefig("plots/03_content_added_by_year.png")
plt.close()

# ----------------------------------------------------------
# 4 Pie Chart
# ----------------------------------------------------------

plt.figure(figsize=(7,7))
df["type"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)
plt.title("Content Distribution")
plt.ylabel("")
plt.savefig("plots/04_content_distribution_pie.png")
plt.close()

# ----------------------------------------------------------
# 5 Top 10 Countries
# ----------------------------------------------------------

countries = df["country"].str.split(",").explode()

plt.figure(figsize=(12,6))
countries.value_counts().head(10).plot(
    kind="bar"
)

plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")
plt.savefig("plots/05_top_countries.png")
plt.close()

# ----------------------------------------------------------
# 6 Top Ratings
# ----------------------------------------------------------

plt.figure(figsize=(10,6))
sns.countplot(
    y=df["rating"],
    order=df["rating"].value_counts().index
)

plt.title("Rating Distribution")
plt.savefig("plots/06_rating_distribution.png")
plt.close()

# ----------------------------------------------------------
# 7 Top Genres
# ----------------------------------------------------------

genres = df["listed_in"].str.split(",").explode()

plt.figure(figsize=(12,6))
genres.value_counts().head(10).plot(
    kind="barh"
)

plt.title("Top Genres")
plt.xlabel("Count")
plt.savefig("plots/07_top_genres.png")
plt.close()

# ----------------------------------------------------------
# 8 Movie Duration Distribution
# ----------------------------------------------------------

movies = df[df["type"] == "Movie"]

plt.figure(figsize=(10,5))
sns.histplot(movies["duration_num"])
plt.title("Movie Duration Distribution")
plt.xlabel("Minutes")
plt.savefig("plots/08_movie_duration_distribution.png")
plt.close()

# ----------------------------------------------------------
# 9 TV Show Seasons Distribution
# ----------------------------------------------------------

tvshows = df[df["type"] == "TV Show"]

plt.figure(figsize=(10,5))
sns.histplot(tvshows["duration_num"])
plt.title("TV Show Seasons Distribution")
plt.xlabel("Number of Seasons")
plt.savefig("plots/09_tvshow_seasons_distribution.png")
plt.close()

# ----------------------------------------------------------
# 10 Top Directors
# ----------------------------------------------------------

directors = df[df["director"] != "Unknown"]

plt.figure(figsize=(12,6))
directors["director"].value_counts().head(10).plot(
    kind="bar"
)

plt.title("Top Directors")
plt.xlabel("Director")
plt.ylabel("Count")
plt.savefig("plots/10_top_directors.png")
plt.close()

# ----------------------------------------------------------
# 11 Top Actors
# ----------------------------------------------------------

actors = df["cast"].str.split(",").explode()

plt.figure(figsize=(12,6))
actors.value_counts().head(10).plot(
    kind="barh"
)

plt.title("Top Actors")
plt.xlabel("Count")
plt.savefig("plots/11_top_actors.png")
plt.close()

# ----------------------------------------------------------
# 12 Scatter Plot
# ----------------------------------------------------------

plt.figure(figsize=(8,5))
sns.scatterplot(
    x="release_year",
    y="duration_num",
    data=df
)

plt.title("Release Year vs Duration")
plt.savefig("plots/12_scatter_release_vs_duration.png")
plt.close()

# ----------------------------------------------------------
# 13 Correlation Heatmap
# ----------------------------------------------------------

plt.figure(figsize=(6,4))

sns.heatmap(
    corr,
    annot=True,
    cmap="coolwarm"
)

plt.title("Correlation Heatmap")
plt.savefig("plots/13_correlation_heatmap.png")
plt.close()

# ----------------------------------------------------------
# 14 Box Plot
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

sns.boxplot(
    x="type",
    y="duration_num",
    data=df
)

plt.title("Duration by Content Type")
plt.savefig("plots/14_boxplot_duration.png")
plt.close()

# ----------------------------------------------------------
# 15 Violin Plot
# ----------------------------------------------------------

plt.figure(figsize=(8,5))

sns.violinplot(
    x="type",
    y="duration_num",
    data=df
)

plt.title("Violin Plot of Duration")
plt.savefig("plots/15_violin_duration.png")
plt.close()

# ==========================================================
# PART 5 - INSIGHTS
# ==========================================================

print("\n" + "=" * 60)
print("KEY INSIGHTS")

print("1. Netflix contains more Movies than TV Shows.")
print("2. Most content was released after 2010.")
print("3. United States contributes the highest number of titles.")
print("4. TV-MA is one of the most common ratings.")
print("5. Content additions increased significantly after 2015.")
print("6. Drama and International genres dominate the platform.")
print("7. Movie durations are concentrated around standard feature lengths.")
print("8. Netflix content comes from a diverse set of countries.")
print("9. Some directors and actors appear frequently across titles.")
print("10. The platform experienced rapid growth between 2016 and 2020.")

print("\nAll visualizations saved successfully in the 'plots' folder.")
print("PROJECT COMPLETED SUCCESSFULLY")