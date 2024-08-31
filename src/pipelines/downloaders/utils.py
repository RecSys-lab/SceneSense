#!/usr/bin/env python3

def filterMovieList(jsonData: list):
    """
    Filters the movie list from the given JSON data to have only the `id`, `title`, and `year` fields
    
    Parameters
    ----------
    jsonData: list
        The JSON data containing the movies
    """
    # Check json file
    if jsonData is None:
        return None
    # Initialize an empty list
    filteredMovies = []
    # Iterate through the JSON data
    for item in jsonData:
        filteredMovies.append({'id': item['id'],
                                'title': item['title'],
                                'year': item['year']
                                })
    # Prepare a log message
    print(f"Processed {len(filteredMovies)} movies from the JSON data to query YouTube ...\n")
    # Return
    return filteredMovies