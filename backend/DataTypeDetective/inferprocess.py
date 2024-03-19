import pandas as pd

def main_infer(df):
    """
    Infer and convert data types in a DataFrame.
    
    Parameters:
        df (DataFrame): Input DataFrame.
        
    Returns:
        DataFrame: DataFrame with inferred and converted data types.
    """
    for col in df.columns:
        try:
            numeric_values = pd.to_numeric(df[col], errors='coerce')
            if not numeric_values.isna().all():
                df[col] = numeric_values
                continue
        except ValueError:
            pass
        
        try:
            datetime_values = pd.to_datetime(df[col], errors='coerce')
            if not datetime_values.isna().all():
                df[col] = datetime_values
                continue
        except ValueError:
            pass
        
        if df[col].apply(lambda x: isinstance(x, str)).all():
            unique_ratio = len(df[col].unique()) / len(df[col])
            if unique_ratio < 0.5:
                df[col] = pd.Categorical(df[col])
    
    return df

def main_read(file, chunksize=10000):
    """
    Read a file and infer data types from its contents.
    
    Parameters:
        file (File): File object to read.
        chunksize (int): Number of rows to read into memory at once.
        
    Returns:
        DataFrame: DataFrame with inferred data types.
    """
    file_extension = file.name.split('.')[-1].lower()
    if file.content_type == 'text/csv' or file_extension == 'csv':
        reader = pd.read_csv(file, chunksize=chunksize)
    elif file.content_type in ['application/vnd.ms-excel', 'application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'] or file_extension in ['xls', 'xlsx']:
        reader = pd.read_excel(file, chunksize=chunksize)
    else:
        raise ValueError("Unsupported file format. Only CSV and Excel files are supported.")

    # Initialize an empty DataFrame to store the results
    chunk_list = []

    # Iterate over chunks and infer data types
    for chunk in reader:
        chunk = main_infer(chunk)
        chunk_list.append(chunk)

    # Concatenate all chunks into a single DataFrame
    df = pd.concat(chunk_list)

    return df
