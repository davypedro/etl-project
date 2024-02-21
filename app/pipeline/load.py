"""
Module to load data.
"""

import os

import pandas as pd


def load_csv(
    data_frame: pd.DataFrame, output_path: str, file_name: str
) -> str:
    """
    Saves a given pandas DataFrame to a CSV file at the specified output path with the given file name.
    If the output directory does not exist, it is created.

    Parameters:
    - data_frame (pd.DataFrame): The pandas DataFrame to be saved to CSV.
    - output_path (str): The directory path where the CSV file will be saved. If the directory does not exist, it will be created.
    - file_name (str): The name of the CSV file without the extension.

    Returns:
    - str: A confirmation message indicating successful file saving.

    Notes:
    - The function saves the CSV file with the index included.
    - The check for the existence of the output directory and its creation if it does not exist helps prevent errors related to non-existent paths.
    """

    if not os.path.exists(output_path):
        os.makedirs(output_path)

    data_frame.to_csv(f'{output_path}/{file_name}.csv', index=True)
    return 'File saved successfully.'
