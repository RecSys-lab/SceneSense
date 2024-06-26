#!/usr/bin/env python3

from scenesense.helper_metadata import loadJsonFromUrl, countNumberOfMovies, fetchRandomMovie, fetchMovieById
from scenesense.helper_metadata import classifyYearsByCount, fetchMoviesByGenre, classifyMoviesByGenre

# Sample variables
datasetName = "SceneSense-visual"
featureModels = ["incp3", "vgg19"]
featureSources = ["full_movies", "movie_shots", "movie_trailers"]
datasetUrl = "https://huggingface.co/datasets/alitourani/moviefeats_visual/resolve/main"

def main():
    print(f"Hi! This is an example provided for you to work with the '{datasetName}' dataset ... \n")
    # Fetch JSON data from the URL
    print(f"- Fetching URL from '{datasetUrl}' ...")
    jsonData = loadJsonFromUrl(datasetUrl)
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
    # End of the example
    print(f"End of the example for the '{datasetName}' dataset ...")

main()