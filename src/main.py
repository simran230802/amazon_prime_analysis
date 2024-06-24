import pandas as pd
from data_cleaning import load_and_clean_data
from data_visualization import visualize_data

def main():
    # Load and clean the data
    file_path = '../data/amazon_prime_titles.csv'
    df = load_and_clean_data(file_path)

    # Visualize the data
    visualize_data(df)

if __name__ == "__main__":
    main()
