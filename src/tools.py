from smolagents import tool
import pandas as pd

@tool
def list_csv_files() -> str:
    """
    Lists all CSV files available in the data directory.
    """
    import os

    files = [f for f in os.listdir("data") if f.endswith(".csv")]
    return "\n".join(files)

@tool
def get_csv_columns(filename: str) -> str:
    """
    Returns the column names of a CSV file.

    Args:
        filename: Name of the CSV file inside the data folder.
    """
    import pandas as pd

    df = pd.read_csv(f"data/{filename}", nrows=5)
    return ", ".join(df.columns)