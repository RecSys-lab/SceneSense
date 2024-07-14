#!/usr/bin/env python3

from scenesense.common import loadJsonFromUrl
from scenesense.visualizer_metadata import visualizeGenresDictionary
from scenesense.helper_metadata import countNumberOfMovies, fetchRandomMovie, fetchMovieById
from scenesense.helper_metadata import classifyYearsByCount, fetchMoviesByGenre, classifyMoviesByGenre, calculateAverageGenrePerMovie

# Sample variables
datasetName = "SceneSense-visual"
featureModels = ["incp3", "vgg19"]
featureSources = ["full_movies", "movie_shots", "movie_trailers"]
datasetMetadataUrl = "https://huggingface.co/datasets/alitourani/moviefeats_visual/resolve/main/stats.json"

def testMetadataProcess():
    print(f"Hi! This is an example provided for you to work with the '{datasetName}' dataset ... \n")
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

# Run
testMetadataProcess()