import pandas as pd
from pathlib import Path


def load_data(file_path):
    """
    Load CSV file and return DataFrame.
    """

    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(
            f"File '{file_path}' does not exist."
        )

    df = pd.read_csv(file_path)

    return df