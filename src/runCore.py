#!/usr/bin/env python3

from src.core.datasets.scenesense.common import loadJsonFromUrl
from src.core.pipeline.downloaders.utils import filterMovieList
from src.core.pipeline.downloaders.movieTrailerDownloader import downloadMovieTrailers

def runTrailerDownloader(configs: dict, datasetInfo: dict):
    """
    Runs the trailer downloader pipeline
    """
    print("Running the trailer downloader pipeline ...")
    # Fetch JSON data from the URL
    print(f"- Fetching URL from '{datasetInfo['name']}' ...")
    jsonData = loadJsonFromUrl(datasetInfo['jsonPath'])
    # Filter the movie list
    print(f"- Preparing data to make proper queries for movie finding ...")
    filteredMovies = filterMovieList(jsonData)
    # Fetch and download the movie trailers of the given list
    downloadMovieTrailers(configs, filteredMovies)