import pandas as pd


def analyze_csv(file_path):
    try:
        df = pd.read_csv(file_path)
        print("Dataset Preview:")
        print(df.head())

        print("\nSummary Statistics:")
        print(df.describe())

        print("\nMissing Values:")
        print(df.isnull().sum())

    except FileNotFoundError:
        print("Error: File not found.")
    except pd.errors.EmptyDataError:
        print("Error: The file is empty.")
    except Exception as e:
        print(f"Unexpected error: {e}")


file_path = "woofwoof.csv"
analyze_csv(file_path)
