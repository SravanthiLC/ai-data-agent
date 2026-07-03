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