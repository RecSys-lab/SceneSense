#!/usr/bin/env python3

from movifex.utils import loadJsonFromUrl
from movifex.pipelines.frames.utils import initMovieVideos
from movifex.pipelines.downloaders.utils import filterMovieList
from movifex.pipelines.frames.frameExtractor import extractMovieFrames
from movifex.pipelines.visual_features.utils import initMovieFramesFolders
from movifex.pipelines.shots.utils import initFramesFoldersForShotDetection
from movifex.pipelines.shots.utils import initFeaturesFoldersForShotDetection
from movifex.pipelines.visual_features.featureExtractor import extractMovieFeatures
from movifex.pipelines.downloaders.movieTrailerDownloader import downloadMovieTrailers
from movifex.pipelines.visual_features.featureAggregator import aggregateMovieFeatures
from movifex.pipelines.shots.shotDetection import extractShotsFromMovieFrames, extractShotsFromMovieFeatures

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