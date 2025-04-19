import re

def ping():
    print("pong")

def dataframe_info(df):
    """
    Displays basic information about a DataFrame, including its shape, columns, and data types.
    
    :param df: The DataFrame to analyze.
    """
    print("\nDataFrame Information:")
    print(f"\nShape: {df.shape}")
    print(f"\nColumns: {df.columns.tolist()}")
    print(f"\nData Types:\n{df.dtypes}")
    print(f"\nMissing Values:\n{df.isnull().sum()}")
    print(f"\nDataFrame Memory Usage: {df.memory_usage(deep=True).sum() / 1024**2:.2f} MB")
    print(f"\nDataFrame Size: {df.size} elements")
    
    print(f"\n\n>DataFrame describe:\n {df.describe()}")