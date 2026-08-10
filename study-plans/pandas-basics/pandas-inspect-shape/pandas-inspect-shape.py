import pandas as pd

def inspect_dataframe(data):
    df = pd.DataFrame.from_dict(data)
    rows, cols = df.shape
    columns = df.columns.tolist()
    dtypes = {col: str(dtype) for col, dtype in df.dtypes.items()}

    return {
        "rows": rows,
        "cols": cols,
        "columns": columns,
        "dtypes": dtypes,
        "total_values": int(df.size),
    }
