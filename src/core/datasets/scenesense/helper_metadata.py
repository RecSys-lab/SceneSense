#!/usr/bin/env python3
import json
import random
import requests


def loadJsonFromUrl(url):
    """
    Load `stats.json` data from a given URL and return it.

    Parameters:
        url (str): The URL to load JSON data from.

    Returns:
        dict: The JSON data loaded from the URL.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad status codes
        data = response.json()  # Parse JSON data'
        print("JSON data loaded successfully!")
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from {url}: {e}")
        return None
    except json.JSONDecodeError as e:
        print(f"Error parsing JSON data: {e}")
        return None


def countNumberOfMovies(data):
    """
    Counts the number of movies in the given data.

    Parameters:
        data (dict): The JSON data containing the movies.

    Returns:
        int: The number of movies in the dataset.
    """
    if data:
        moviesCount = len(data)
        print(f"The dataset contains {moviesCount} movies!")
    else:
        print("Data is empty or not loaded.")


def fetchRandomMovie(data):
    """
    Fetches a random movie from the given data.

    Parameters:
        data (dict): The JSON data containing the movies.

    Returns:
        dict: A random movie from the dataset.
    """
    if data:
        randomMovie = random.choice(data)
        print("Randomly fetched movie:")
        print(json.dumps(randomMovie, indent=4))
    else:
        print("Data is empty or not loaded.")
