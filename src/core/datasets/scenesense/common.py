#!/usr/bin/env python3

import json
import requests

def loadJsonFromUrl(jsonUrl: str):
    """
    Load `json` data from a given URL and return it.

    Parameters:
        jsonUrl (str): The root address to load JSON data from.

    Returns:
        dict: The JSON data loaded from the URL.
    """
    try:
        # Load JSON data from the URL
        response = requests.get(jsonUrl)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()  # Parse JSON data'
        print("JSON data loaded successfully!\n")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {jsonUrl}: {e}\n")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")
        return None