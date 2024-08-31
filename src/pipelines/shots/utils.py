import os
import json
import string
import pandas as pd
from glob import glob

def initFramesFoldersForShotDetection(configs: dict):
    """
    Pre-checks the given directory for movie frames and prepares it for shot detection

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
    movieFramesRootDir, shotFramesRootDir = configs['frames_path'], configs['shot_frames_path']
    # Check if the given directory exists
    if not os.path.exists(movieFramesRootDir):
        print(f"Input movie frames root directory '{movieFramesRootDir}' does not exist! Exiting ...")
        return False
    print(f"Movie frames will be processed from the root directory '{movieFramesRootDir}' ...")
    # Check if the output directory exists and create it if not
    if not os.path.exists(shotFramesRootDir):
        os.mkdir(shotFramesRootDir)
        print(f"Selected shot frames will be saved in '{shotFramesRootDir}' ...")
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

def initFeaturesFoldersForShotDetection(configs: dict):
    """
    Pre-checks the given directory for extracted movie features and prepares it for shot detection

    Parameters
    ----------
    configs: dict
        The configurations dictionary
    
    Returns
    -------
    featuresFolders :list
        A list of fetched features folders
    """
    # Variables
    featuresFolders = []
    movieFeaturesRootDir, shotFeaturesRootDir = configs['features_path'], configs['shot_features_path']
    # Check if the given directory exists
    if not os.path.exists(movieFeaturesRootDir):
        print(f"Input movie features root directory '{movieFeaturesRootDir}' does not exist! Exiting ...")
        return False
    print(f"Movie features will be processed from the root directory '{movieFeaturesRootDir}' ...")
    # Check if the output directory exists and create it if not
    if not os.path.exists(shotFeaturesRootDir):
        os.mkdir(shotFeaturesRootDir)
        print(f"Selected shot features will be saved in '{shotFeaturesRootDir}' ...")
    # Check the supported feature types
    print(f"Processing the input features directory. Supported feature format is 'json' ...")
    # Get the list of movie folders in the root directory
    for featureFolder in glob(f'{movieFeaturesRootDir}/*/'):
        if glob(f'{featureFolder}*.json'):
            featuresFolders.append(featureFolder)
            break  # Exit inner loop if at least one json is found in this folder
    # Inform the user about the number of feature folders to process
    if len(featuresFolders) == 0:
        print(f"No movie feature folders found in the given directory '{movieFeaturesRootDir}'! Exiting ...")
        return False
    print(f"Found {len(featuresFolders)} folders containing features to process! (e.g., {featuresFolders[0]})\n")
    # Return the list of video files
    return featuresFolders

def initShotsFolder(featuresDir: str, outputDir: str):
    """
    Pre-checks and generates the output shots visual features folder

    Parameters
    ----------
    featuresDir: str
        The features folder address to pick shots visual features from
    outputDir: str
        The shots visual features directory to save the extracted features packets
    
    Returns
    -------
    generatedPath: str
        The generated shots visual features directory path
    """
    # Take the last part of the frames directory
    folderName = os.path.basename(featuresDir)
    # Normalizing the frames folder name to assign it to the output feature folder
    folderName = string.capwords(folderName.replace("_", "")).replace(" ", "")
    # Creating output folder
    generatedPath = os.path.join(outputDir, folderName)
    # Do not re-generate feature packets for movie features if there is a folder with their normalized name
    if os.path.exists(generatedPath):
        print(
            f'- Skipping "{folderName}" due to finding an output folder with the same name!')
        return
    else:
        os.mkdir(generatedPath)
        return generatedPath

def mergePacketsIntoDataFrame(packetsFolder: str):
    """
    Merges all the visual features in JSON files into a single DataFrame

    Parameters
    ----------
    packetsFolder : str
        Path to the folder containing the JSON files (packets) of extracted visual features

    Returns
    -------
    mergedDataFrame : DataFrame
        DataFrame containing all the visual features in JSON files

    """
    # Variables
    mergedDataFrame = pd.DataFrame(columns=['frameId', 'features'])
    # Iterate over the packet files to collect them all in a single dataframe
    for packetIdx, packetFile in enumerate(glob(f'{packetsFolder}/*.json')):
        # Inform the user about the processing packet
        if (packetIdx % 50 == 0):
            print(f'-- Fetching packet #{packetIdx} ...')
        # Reading each packet's data
        jsonFile = open(packetFile,)
        # Load the JSON data
        packetData = json.load(jsonFile)
        # Iterate on each frames of array
        for frameData in packetData:
            mergedDataFrame = pd.concat([mergedDataFrame, pd.DataFrame([{'frameId': frameData['frameId'], 'features': frameData['features']}])],
                                           ignore_index=True)
        # Close the JSON file
        jsonFile.close()
    return mergedDataFrame