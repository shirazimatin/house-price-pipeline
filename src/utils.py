from pathlib import Path


def create_directory(directory_path):
    """
    Create a directory if it does not exist.
    """

    Path(directory_path).mkdir(
        parents=True,
        exist_ok=True
    )


def print_separator():
    """
    Print a separator line.
    """

    print("-" * 50)