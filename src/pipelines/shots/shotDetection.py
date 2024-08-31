import os
import time
import pandas as pd
from src.pipelines.shots.utils import initShotsFolder

def extractShotsFromMovieFrames(configs: dict, movieFramesPaths: list):
    """
    Extracts shots from the given set of extracted movie frames

    Parameters
    ----------
    configs: dict
        The configurations dictionary
    movieFramesPaths: list
        The list of movie frames paths
    """
    print("Extracting movie shots from the given set of movie frames ...")
    # Iterate on all frames folders in the given directory
    for framesFolder in movieFramesPaths:
        # Preparing the output shots frames directory
        framesFolder = os.path.normpath(framesFolder)
        outputDir = initShotsFolder(framesFolder, configs['shot_frames_path'])
        if not outputDir:
            continue
        # Picking shot features from the given features folder

def extractShotsFromMovieFeatures(configs: dict, movieFeaturesFolders: list):
    """
    Extracts shots from the given set of extracted movie features

    Parameters
    ----------
    configs: dict
        The configurations dictionary
    movieFeaturesFolders: list
        The list of movie features paths
    """
    print("Extracting movie shots from the given set of movie features ...")
    # Iterate on all features folders in the given directory
    for featuresFolder in movieFeaturesFolders:
        # Preparing the output shots features directory
        featuresFolder = os.path.normpath(featuresFolder)
        outputDir = initShotsFolder(featuresFolder, configs['shot_features_path'])
        if not outputDir:
            continue
        # Picking shot features from the given features folder
        # try:
        #     # Variables
        #     packetCounter = 0
        #     startTime = time.time()
        #     packetIndex = 1  # Holds the name of the packet, e.g. Packet0001
        #     shotsDataFrame = pd.DataFrame(columns=['frameId', 'features'])
        #     # Read packet JSON files
        #     packetCount = len(os.listdir(movieFeaturesPaths))
        #     print(f'Processing {packetCount} packets of movie "{videoName}" ...')