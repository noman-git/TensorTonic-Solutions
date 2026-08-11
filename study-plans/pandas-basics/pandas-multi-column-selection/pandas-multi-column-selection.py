import pandas as pd

def select_columns(data, columns):
    """
    Returns: dict mapping selected column names to value lists
    """
    df = pd.DataFrame.from_dict(data)
    df = df[columns]
    return df.to_dict("list")