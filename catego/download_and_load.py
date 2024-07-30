# download_and_load.py
import pandas as pd

def load_dataset(file_path):
    """Load dataset from the specified file path."""
    if file_path.endswith('.csv'):
        df = pd.read_csv(file_path)
    elif file_path.endswith('.xlsx'):
        df = pd.read_excel(file_path)
    else:
        raise ValueError("Unsupported file format.")
    
    return df
