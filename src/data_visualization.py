import matplotlib.pyplot as plt
import seaborn as sns

def visualize_data(df):
    # Distribution of release year
    plt.figure(figsize=(10, 6))
    sns.histplot(df['release_year'], bins=30, kde=True)
    plt.title('Distribution of Release Year')
    plt.xlabel('Release Year')
    plt.ylabel('Count')
    plt.show()

    # Count of titles by type (Movie/TV Show)
    plt.figure(figsize=(10, 6))
    sns.countplot(data=df, x='type')
    plt.title('Count of Titles by Type')
    plt.xlabel('Type')
    plt.ylabel('Count')
    plt.show()

    # Top 10 countries with most titles
    plt.figure(figsize=(10, 6))
    top_countries = df['country'].value_counts().head(10)
    sns.barplot(y=top_countries.index, x=top_countries.values)
    plt.title('Top 10 Countries with Most Titles')
    plt.xlabel('Count')
    plt.ylabel('Country')
    plt.show()
