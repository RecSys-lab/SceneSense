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

def initFeaturesFolder(framesDir: str, featuresDir: str):
    """
    Pre-checks and generates the output visual features folder

    Parameters
    ----------
    framesDir: str
        The frames folder address to extract visual features from
    featuresDir: str
        The visual features directory to save the extracted features
    
    Returns
    -------
    videoFiles: list
        A list of fetched video files
    """
    # Take the last part of the frames directory
    folderName = os.path.basename(framesDir)
    # Normalizing the frames folder name to assign it to the output feature folder
    folderName = string.capwords(folderName.replace("_", "")).replace(" ", "")
    # Creating output folder
    generatedPath = os.path.join(featuresDir, folderName)
    # Do not re-generate features for movie frames if there is a folder with their normalized name
    if os.path.exists(generatedPath):
        print(
            f'- Skipping {folderName} due to finding an output folder with the same name!')
        return
    else:
        os.mkdir(generatedPath)
        return generatedPath