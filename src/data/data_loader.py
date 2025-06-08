import pandas as pd
from pathlib import Path

def load_house_csv():
    """
    Loads the raw, unprocessed housing data from the CSV file
    The function assumes the file is located at 'data/raw/house.csv',
    relative to the project root.

    Returns:
        pd.DataFrame: A DataFrame containing the raw housing data.
    """

    #Adjust if this file is moved
    BASE_DIR = Path(__file__).resolve().parent.parent.parent

    file_path = BASE_DIR / 'data' / 'raw' / 'house.csv'
    return pd.read_csv(file_path)