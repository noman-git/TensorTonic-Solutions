import pandas as pd

def boolean_filter(data, column, threshold):
    """
    Returns: dict with 'filtered_data' (dict) and 'count' (int)
    """
    df = pd.DataFrame.from_dict(data)
    filtered_data = df[df[column] > threshold]
    count = filtered_data.shape[0]

    output = {"filtered_data": filtered_data.to_dict("list"), "count": count}

    return output