import os
import glob
import pandas as pd
from typing import List

def extract_from_csv(input_path: str) -> List[pd.DataFrame]:
    """
    Reads all CSV files from the specified folder and returns a list of pandas DataFrames.

    Args:
    - input_path (str): Path to the folder containing CSV files.

    Returns:
    - List[pd.DataFrame]: A list containing a DataFrame for each CSV file in the specified folder.

    Notes:
    - The function uses glob to find all files with a '.csv' extension within the specified folder.
    - Each CSV file is read into a DataFrame, which is then appended to the list of DataFrames.
    - The function assumes all files in the folder with a '.csv' extension are valid CSV files to be read.
    """

    all_files = glob.glob(os.path.join(input_path, "*.csv"))

    dataframe_list = [] 
    for file in all_files:
        dataframe_list.append(pd.read_csv(file))

    return dataframe_list

if __name__ == "__main__":
    dataframe_list = extract_from_csv("data/input")
    print(dataframe_list)