#!/usr/bin/env python3

from moviefex.utils import loadJsonFromUrl
from moviefex.pipelines.frames.utils import initMovieVideos
from moviefex.pipelines.downloaders.utils import filterMovieList
from moviefex.pipelines.frames.frameExtractor import extractMovieFrames
from moviefex.pipelines.visual_features.utils import initMovieFramesFolders
from moviefex.pipelines.shots.utils import initFramesFoldersForShotDetection
from moviefex.pipelines.shots.utils import initFeaturesFoldersForShotDetection
from moviefex.pipelines.visual_features.featureExtractor import extractMovieFeatures
from moviefex.pipelines.downloaders.movieTrailerDownloader import downloadMovieTrailers
from moviefex.pipelines.visual_features.featureAggregator import aggregateMovieFeatures
from moviefex.pipelines.shots.shotDetection import extractShotsFromMovieFrames, extractShotsFromMovieFeatures

def runTrailerDownloader(configs: dict, datasetInfo: dict):
    """
    Runs the trailer downloader pipeline

    Parameters
    ----------
    configs :dict
        The configurations dictionary
    datasetInfo :dict
        The dataset information dictionary
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

def runMoviesFrameExtractor(configs: dict):
    """
    Runs the movies frame extractor pipeline

    Parameters
    ----------
    configs :dict
        The configurations dictionary
    """
    print("Running the movies frame extractor pipeline ...")
    # Pre-check the input directory
    fetchedMoviesPaths = initMovieVideos(configs)
    if not fetchedMoviesPaths:
        return
    # Extract frames from the fetched movies
    extractMovieFrames(configs, fetchedMoviesPaths)

def runMoviesFramesFeatureExtractor(configs: dict):
    """
    Runs the feature extractor pipeline from the movie frames

    Parameters
    ----------
    configs :dict
        The configurations dictionary
    """
    print("Running the movies frames visual feature extractor pipeline ...")
    # Pre-check the input directory
    fetchedMovieFramesPaths = initMovieFramesFolders(configs)
    if not fetchedMovieFramesPaths:
        return
    # Extract visual features from the fetched frames
    extractMovieFeatures(configs, fetchedMovieFramesPaths)

def runShotDetectionFromFrames(configs: dict):
    """
    Runs the shot detection pipeline from the movie frames

    Parameters
    ----------
    configs :dict
        The configurations dictionary
    """
    print("Running the pipeline for shot detection from given movie frames ...")
    # Pre-check the input directory
    movieFramesPaths = initFramesFoldersForShotDetection(configs)
    if not movieFramesPaths:
        return
    # Extract shots from the fetched frames
    extractShotsFromMovieFrames(configs, movieFramesPaths)

def runShotDetectionFromFeatures(configs: dict):
    """
    Runs the shot detection pipeline from the extracted movie features

    Parameters
    ----------
    configs :dict
        The configurations dictionary
    """
    print("Running the pipeline for shot detection from extracted movie features ...")
    # Pre-check the input directory
    movieFeaturesPaths = initFeaturesFoldersForShotDetection(configs)
    if not movieFeaturesPaths:
        return
    # Extract shots from the fetched features
    extractShotsFromMovieFeatures(configs, movieFeaturesPaths)

def runAggFeatures(configs: dict):
    """
    Runs the feature aggregation pipeline

    Parameters
    ----------
    configs: dict
        The configurations dictionary
    """
    print("Running the feature aggregation pipeline ...")
    # Aggregate features from the given set of extracted movie features
    aggregateMovieFeatures(configs)