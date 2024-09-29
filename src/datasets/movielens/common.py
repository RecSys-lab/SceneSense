#!/usr/bin/env python3

import os
import pandas as pd

def loadDataFromCSV(csvPath: str):
    """
    Load `CSV` data from a given local CSV file and return it.

    Parameters:
        csvPath (str): The path to the local CSV file.

    Returns:
        dict: The loaded CSV data.
    """
    try:
        # Check if the file exists
        if not os.path.exists(csvPath):
            raise FileNotFoundError(f"File '{csvPath}' not found! Exiting ...")
        # Load the CSV data
        csvData = pd.read_csv(csvPath)
        return csvData
    except Exception as e:
        print(f"An error occurred while loading the CSV data: {e}")
        return None
