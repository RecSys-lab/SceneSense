#!/usr/bin/env python3

import os
from src.datasets.scenesense.common import loadJsonFromUrl
from src.datasets.movielens.downloader import downloadMovielens25m
from src.datasets.scenesense.visualizer_metadata import visualizeGenresDictionary
from src.datasets.scenesense.helper_visualfeats import packetAddressGenerator, fetchAllPackets
from src.datasets.scenesense.helper_metadata import countNumberOfMovies, fetchRandomMovie, fetchMovieById
from src.datasets.scenesense.helper_metadata import classifyYearsByCount, fetchMoviesByGenre, classifyMoviesByGenre, calculateAverageGenrePerMovie

# Sample variables
datasetName = "SceneSense-visual"
featureModels = ["incp3", "vgg19"]
featureSources = ["full_movies", "movie_shots", "movie_trailers"]
datasetRawFilesUrl = "https://huggingface.co/datasets/alitourani/moviefeats_visual/raw/main/"
datasetMetadataUrl = "https://huggingface.co/datasets/alitourani/moviefeats_visual/resolve/main/stats.json"

def testMetadataProcess():
    print(f"Hi! This is an example provided for you to work with the metadata (json) file of the '{datasetName}' dataset ... \n")
    # Fetch JSON data from the URL
    print(f"- Fetching URL from '{datasetMetadataUrl}' ...")
    jsonData = loadJsonFromUrl(datasetMetadataUrl)
    # Count the number of movies in the dataset
    print(f"\n- Testing Movie Count ...")
    moviesCount = countNumberOfMovies(jsonData)
    print(f"- Returned variable (int): {moviesCount}\n")
    # Fetch a random movie from the dataset
    print(f"\n- Testing Random Movie Fetcher ...")
    randomMovie = fetchRandomMovie(jsonData)
    print(f"- Returned variable (dict): {randomMovie}\n")
    # Fetch a movie by ID
    givenMovieId = 6
    print(f"\n- Testing Movie by ID Fetcher (input: {givenMovieId}) ...")
    movieById = fetchMovieById(jsonData, givenMovieId)
    print(f"- Returned variable (dict): {movieById}\n")
    # Fetch movies by genre
    givenGenre = "Romance"
    print(f"\n- Testing Movie by Genre Fetcher (input: {givenGenre}) ...")
    moviesByGenre = fetchMoviesByGenre(jsonData, givenGenre)
    print(f"- Returned variable (list): {moviesByGenre}\n")
    # Classify release years by count
    print(f"\n- Testing Year Classification ...")
    yearsCount = classifyYearsByCount(jsonData)
    print(f"- Returned variable (dict): {yearsCount}\n")
    # Classify movies by genre
    print(f"\n- Testing Movie Classification by Genre ...")
    moviesByGenre = classifyMoviesByGenre(jsonData)
    print(f"- Returned variable (dict): {moviesByGenre}\n")
    # Calculate the average genre per movie
    print(f"\n- Testing Average Genre per Movie ...")
    averageGenrePerMovie = calculateAverageGenrePerMovie(moviesByGenre, moviesCount)
    print(f"- Returned variable (float): {averageGenrePerMovie}\n")
    # Show the classification results in a bar chart
    print(f"\n- Visualizing Movie Classification by Genre ...")
    visualizeGenresDictionary(moviesByGenre)
    # End of the example
    print(f"End of the example for the '{datasetName}' dataset ...")

def testVisualDataProcess():
    print(f"Hi! This is an example provided for you to work with the visual packets of the '{datasetName}' dataset ... \n")
    # Fetch JSON data from the URL
    givenMovieId = 6
    print(f"- Generating a sample packet address file from '{datasetRawFilesUrl}' ...")
    packetAddress = packetAddressGenerator(datasetRawFilesUrl, featureSources[2], featureModels[0], givenMovieId, 1)
    print(f"- Generated address (str): {packetAddress}\n")
    # Fetch all packets of a movie
    print(f"- Fetching all packets of the movie #{givenMovieId}) ...")
    moviePackets = fetchAllPackets(datasetRawFilesUrl, featureSources[2], featureModels[0], givenMovieId)
    print(f"- Number of packets fetched (list): {len(moviePackets)}")

def runMovieLens25(configs: dict):
    """
    Runs the text dataset pipeline (MovieLens 25M dataset)

    Parameters
    ----------
    configs :dict
        The configurations dictionary
    """
    print(f"Running the text dataset pipeline '{configs['name']}' ...")
    # Variables
    isDownloaded = configs['need_download']
    datasetPath = os.path.normpath(configs['download_path'])
    # Pre-check whether the dataset is already downloaded
    if not isDownloaded:
        print(f"The dataset needs to be downloaded! It will be downloaded in '{datasetPath}' ...")
        isDownloadSuccessful = downloadMovielens25m(configs['url'], datasetPath)
        if not isDownloadSuccessful:
            return
    # else:
    #     print(f"The dataset is already downloaded! Trying to read from '{datasetPath}' ...")
    
    # Pre-check the input directory
    # fetchedMoviesPaths = initMovieVideos(configs)
    # if not fetchedMoviesPaths:
    #     return
    # # Extract frames from the fetched movies
    # extractMovieFrames(configs, fetchedMoviesPaths)