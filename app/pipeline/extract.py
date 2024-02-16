import os
import glob
import pandas as pd
from typing import List

"""
Funciton to read files from a folder 
data/input and return a dataframes list

args: input_path (str): local path with files

return: dataframes list
"""

path = "data/input"

def extract_from_csv(path: str) -> List[pd.DataFrame]:
    all_files = glob.glob(os.path.join(path, "*csv"))

    dataframe_list = []
    for file in all_files:
        dataframe_list.append(pd.read_csv(file))

    return dataframe_list

if __name__ == "__main__":
    dataframe_list = extract_from_csv("data/input")
    print(dataframe_list)