import pandas as pd

def data_types_overview(data):
    """
    Returns: dict with 'dtypes', 'type_counts', 'num_columns'
    """
    df = pd.DataFrame.from_dict(data)
    dtypes = {}
    type_counts = {}
    for col, dtype in df.dtypes.items():
        dtypes[col] = str(dtype)
        type_counts[str(dtype)] = type_counts.get(str(dtype), 0) + 1

    num_columns = sum(type_counts.values())

    return {"dtypes": dtypes, "type_counts": type_counts, "num_columns": num_columns}
        

        