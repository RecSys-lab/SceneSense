#!/usr/bin/env python3

from src.core.datasets.scenesense.common import loadJsonFromUrl
from src.core.pipeline.downloaders.utils import filterMovieList
from src.core.pipeline.frames.utils import initMovieVideos, initFramesFolder
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

def runMoviesFrameExtractor(configs: dict):
    """
    Runs the movies frame extractor pipeline
    """
    print("Running the movies frame extractor pipeline ...")
    # Pre-check the input directory
    fetchedMoviesPaths = initMovieVideos(configs)
    if not fetchedMoviesPaths:
        return
    # Iterate on all video files in the given directory
    for videoFile in fetchedMoviesPaths[:3]:
        # Extract frames from the video
        print(f"- Processing video '{videoFile}' ...")
        # Preparing the output frames directory
        outputDir = initFramesFolder(videoFile, configs['frames_path'])
        if not outputDir:
            continue
        # frameExtractor(videoFile, configs['frames_path'], configs['network_input_size'])
    print("Movies frame extraction pipeline finished ...")
