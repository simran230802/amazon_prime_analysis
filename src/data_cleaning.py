import pandas as pd

def load_and_clean_data(filepath):
    # Load the dataset
    df = pd.read_csv(filepath)

    # Fill missing values
    df['director'].fillna('Unknown', inplace=True)
    df['cast'].fillna('Unknown', inplace=True)
    df['country'].fillna('Unknown', inplace=True)
    df['date_added'].fillna('Unknown', inplace=True)
    df['rating'].fillna('Unknown', inplace=True)

    # Convert 'date_added' to datetime
    df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')

    # Convert 'release_year' to integer
    df['release_year'] = df['release_year'].astype(int)

    return df
