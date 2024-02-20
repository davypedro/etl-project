import pandas as pd
from app.pipeline.transform import concat_dataframes

df1 = pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]})
df2 = pd.DataFrame({'col1': [5, 6], 'col2': [7, 8]})

def test_dataframes_concat():
    """
    Test function to verify the functionality of the concat_dataframes function.

    This function creates a list of two DataFrames, concatenates them using the concat_dataframes function,
    and then asserts that the shape of the resulting DataFrame is as expected (4 rows, 2 columns).

    Notes:
    - The test assumes that the concat_dataframes function is designed to concatenate DataFrames vertically.
    - The assert statement checks if the concatenated DataFrame has 4 rows and 2 columns, indicating that the
      concatenation was performed correctly and that no columns were unexpectedly added or removed.
    """

    # arrange
    dataframe_list = [df1, df2]
    data_frame = pd.concat(dataframe_list, ignore_index=True)

    
    # act
    df = concat_dataframes(dataframe_list)

    # assert
    assert df.shape == (4, 2)
    assert data_frame.equals(df)