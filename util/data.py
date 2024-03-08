"""
util/data.py

This utility module is responsible for providing functions that can be used to
interact with the data that we have collected and processed from our research.

This includes getting data, writing data, and manipulating data.

"""

# Imports
import os
import pandas as pd
from numpy import bool_

# Utilities
from util.constants import NON_GENE_COLUMNS


def get_csv_file(path: str) -> pd.DataFrame | None:
    """
    Retrieves a csv file at the specified path if it exists, otherwise
    throws an error.

    :param path:
    :return:
    """

    try:
        return pd.read_csv(path, header=0, float_precision='high', index_col=0)
    except FileNotFoundError:
        print(f"File not found at {path}")
        return None
    

def save_csv_file(data: pd.DataFrame, path: str) -> None:
    """
    Saves the data to a csv file at the specified path.

    :param data:
    :param path:
    :return:
    """

    # Create the directory if it doesn't exist
    new_path = path.split("/")
    new_path.pop()
    new_path = "/".join(new_path)
    os.makedirs(new_path, exist_ok=True)

    data.to_csv(path)


def column_is_gene_data(column: str) -> bool:
    """
    Returns True if the column is gene data, otherwise False.

    :param data:
    :param column:
    :return:
    """

    return column not in NON_GENE_COLUMNS


def combine_data(data: pd.DataFrame, other_data: pd.DataFrame) -> pd.DataFrame:
    """
    Combines two dataframes together.

    :param data:
    :param other_data:
    :return:
    """

    return pd.concat([data, other_data], axis=1)


def remove_non_gene_columns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Removes non-gene columns from the data.

    :param data:
    :return:
    """

    return data.drop(columns=NON_GENE_COLUMNS)


def contains_non_gene_columns(data: pd.DataFrame) -> bool:
    """
    Returns True if the data contains non-gene columns, otherwise False.

    :param data:
    :return:
    """

    return all(column in data.columns for column in NON_GENE_COLUMNS)


# Data properties

"""
- Contains NaN
- Contains XYZ
- Contains Structure-IDs
- Contains Gene Data
- Can be clustered with K-Means
- Can be visualized
- Ways to visualize [3D Scatter, 3D Scatter with Color]
- Can be quantitatively analyzed
- Contains indices
"""

def contains_nan(data: pd.DataFrame) -> bool_:
    """
    Returns True if the data contains NaN values, otherwise False.

    :param data:
    :return:
    """

    return data.isnull().values.any()


def contains_xyz_column(data: pd.DataFrame) -> bool:
    """
    Returns True if the data contains XYZ coordinates, otherwise False
    :param data:
    :return:
    """

    return ("x" in data.columns and "y" in data.columns and "z" in data.columns) or \
        ("X" in data.columns and "Y" in data.columns and "Z" in data.columns)