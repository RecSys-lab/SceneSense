import os
import string
import cv2 as cv
import numpy as np
from glob import glob

def initMovieFramesFolders(configs: dict):
    """
    Pre-checks the given directory for movie frames and prepares it for further processing

    Parameters
    ----------
    configs: dict
        The configurations dictionary
    
    Returns
    -------
    framesFolders :list
        A list of fetched frames folders
    """
    # Variables
    framesFolders = []
    imageTypes = configs['image_formats']
    movieFramesRootDir, vFeaturesDir = configs['movies_frames_path'], configs['features_path']
    # Check if the given directory exists
    if not os.path.exists(movieFramesRootDir):
        print(f"Input movie frames root directory '{movieFramesRootDir}' does not exist! Exiting ...")
        return False
    print(f"Movie frames will be processed from the root directory '{movieFramesRootDir}' ...")
    # Check if the output directory exists and create it if not
    if not os.path.exists(vFeaturesDir):
        os.mkdir(vFeaturesDir)
        print(f"Output visual features will be saved in '{vFeaturesDir}' ...")
    # Check the supported frame types
    print(f"Processing the input frames directory. Supported frame formats are {imageTypes} ...")
    # Get the list of movie folders in the root directory
    for frameFolder in glob(f'{movieFramesRootDir}/*/'):
        for imageType in imageTypes:
            if glob(f'{frameFolder}*.{imageType}'):
                framesFolders.append(frameFolder)
                break  # Exit inner loop if at least one frame is found in this folder
    # Inform the user about the number of frame folders to process
    if len(framesFolders) == 0:
        print(f"No movie frame folders found in the given directory '{movieFramesRootDir}'! Exiting ...")
        return False
    print(f"Found {len(framesFolders)} folders containing frames to process! (e.g., {framesFolders[0]})\n")
    # Return the list of video files
    return framesFolders