import pandas as pd

def select_column(data, column):
    """
    Returns: dict with 'values' (list) and 'length' (int)
    """
    df = pd.DataFrame.from_dict(data)
    col_arr = df[column].tolist()

    return {"values": col_arr, "length": len(col_arr)}