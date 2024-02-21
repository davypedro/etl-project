"""
Module to transform data.
"""

from typing import List

import pandas as pd


def concat_dataframes(dataframe_list: List[pd.DataFrame]) -> pd.DataFrame:
    """
    Concatenates a list of pandas DataFrames into a single DataFrame.

    Parameters:
    - dataframe_list (List[pd.DataFrame]): List of pandas DataFrames to be concatenated.

    Returns:
    - pd.DataFrame: A DataFrame resulting from the concatenation of the provided list of DataFrames.

    Notes:
    - The original indexes of the DataFrames are ignored, creating a new integer index for the resulting DataFrame.
    - Concatenation is performed vertically (along axis 0), stacking the DataFrames in the list.
    - The function uses the union of indexes ('outer' behavior) for the axes not being concatenated, including all columns from the DataFrames.
    """
    return pd.concat(dataframe_list, ignore_index=True)
