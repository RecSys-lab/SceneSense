#!/usr/bin/env python3

import os
from moviefex.utils import loadDataFromCSV, loadJsonFromUrl
from moviefex.datasets.movielens.downloader import downloadMovielens25m
from moviefex.datasets.scenesense.visualizer_metadata import visualizeGenresDictionary
from moviefex.datasets.movielens.helper_ratings import mergeMainGenreMoviesDFWithRatingsDF
from moviefex.datasets.scenesense.helper_visualfeats import packetAddressGenerator, fetchAllPackets
from moviefex.datasets.scenesense.helper_metadata import countNumberOfMovies, fetchRandomMovie, fetchMovieById
from moviefex.datasets.movielens.helper_movies import fetchAllUniqueGenres, fetchMoviesByGenre as fetchMoviesByGenreMovielens
from moviefex.datasets.movielens.helper_movies import augmentMoviesDFWithBinarizedGenres, binarizeMovieGenres, filterMoviesWithMainGenres, mainGenres
from moviefex.datasets.scenesense.helper_metadata import classifyYearsByCount, fetchMoviesByGenre, classifyMoviesByGenre, calculateAverageGenrePerMovie

# Sample variables
datasetName = "SceneSense-visual"
featureModels = ["incp3", "vgg19"]
featureSources = ["full_movies", "movie_shots", "movie_trailers"]
datasetRawFilesUrl = "https://huggingface.co/datasets/alitourani/moviefeats_visual/raw/main/"
datasetMetadataUrl = "https://huggingface.co/datasets/alitourani/moviefeats_visual/resolve/main/stats.json"

def testMetadataProcess():
    print(f"This is an example provided for you to work with the metadata (json) file of the '{datasetName}' dataset ... \n")
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
    print(f"This is an example provided for you to work with the visual packets of the '{datasetName}' dataset ... \n")
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
    # Else, the dataset is already downloaded
    print(f"The dataset is already downloaded! Trying to read from '{datasetPath}' ...")
    # Some test functions
    print(f"\nLet's test some functionalities supported by the framework for the '{configs['name']}' dataset ...")
    # Reading movies data
    print(f"- Reading dataset's movies and fetching them into a DataFrame ...")
    moviesDataFrame = loadDataFromCSV(os.path.join(datasetPath, "movies.csv"))
    if moviesDataFrame is None:
        return
    # Counting the number of movies
    moviesCount = len(moviesDataFrame)
    print(f"- The dataset contains {moviesCount} movies!")
    # Some samples of the movies
    print(f"- The structure of the movies data is as below:")
    print(moviesDataFrame.head(3))
    # Get all genres from the dataset in a list
    print(f"\n- Fetching all genres from the dataset ...")
    allGenres = fetchAllUniqueGenres(moviesDataFrame)
    print(f"- The dataset contains {len(allGenres)} genres, including: {allGenres}")
    # Get movies by a specific genre
    givenGenre = "Action"
    print(f"\n- Fetching movies by a specific genre ({givenGenre}) ...")
    moviesByGenre = fetchMoviesByGenreMovielens(moviesDataFrame, givenGenre)
    print(f"- The dataset contains {len(moviesByGenre)} movies with the genre '{givenGenre}'!")
    # Get movies by the main genres
    print(f"\n- Fetching movies by the main genres {mainGenres} ...")
    mainGenresMoviesDataFrame = filterMoviesWithMainGenres(moviesDataFrame)
    print(f"- The dataset contains {len(mainGenresMoviesDataFrame)} movies with the main genres!")
    print(f"- A sample of the movies with the main genres: \n{mainGenresMoviesDataFrame.head(3)}")
    # Model movies data with binarized genres
    moviesDFBinarizedGenres = binarizeMovieGenres(moviesDataFrame)
    print(f"\n- The movies data with binarized genres is as below: \n{moviesDFBinarizedGenres.head(3)}")
    # Augment the movies data with the binarized genres
    augmentedMoviesDataFrame = augmentMoviesDFWithBinarizedGenres(moviesDataFrame, moviesDFBinarizedGenres)
    print(f"\n- The augmented dataframe is as below: \n{augmentedMoviesDataFrame.head(3)}")
    # Reading user-driven data
    print(f"\n- Reading dataset's user-driven data and fetching them into a DataFrame ...")
    ratingsDataFrame = loadDataFromCSV(os.path.join(datasetPath, "ratings.csv"))
    if ratingsDataFrame is None:
        return
    # Counting the number of ratings
    ratingsCount = len(ratingsDataFrame)
    print(f"- The dataset contains {ratingsCount} ratings!")
    # Some samples of the movies
    print(f"- The structure of the user-ratings data is as below:\n{ratingsDataFrame.head(3)}")
    # Merging the movies and ratings DataFrames
    print(f"\n- Merging the movies (of the main genres) and ratings DataFrames ...")
    mergedDataFrame = mergeMainGenreMoviesDFWithRatingsDF(augmentedMoviesDataFrame, ratingsDataFrame)
    print(f"- The merged DataFrame has {len(mergedDataFrame)} items, such as:\n{mergedDataFrame.head(3)}")
