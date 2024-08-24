import os
import time
import string
import cv2 as cv
import numpy as np
import pandas as pd
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

def featureExtractor(imageFile, model, preProcess, inputSize: int):
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
    # Imports
    from tensorflow.keras.preprocessing.image import load_img, img_to_array
    # Variables
    features = None
    try:
        # Extracting the content of the image
        imageContent = load_img(imageFile, target_size=(inputSize, inputSize))
        # Convert the image pixels to a numpy array
        frameData = img_to_array(imageContent)
        frameData = np.expand_dims(frameData, axis=0)
        # Preprocessing
        frameData = preProcess(frameData)
        # Get extracted features
        features = model.predict(frameData)
        # Return the extracted features
        return features
    except Exception as error:
        print(f'- Error while extracting the features of "{imageFile}": {str(error)}')
        return None

def modelRunner(model, framesFolder, outputDir, configs: dict):
    """
    Pre-checks the given directory for movie frames and prepares it for further processing

    Parameters
    ----------
    model: Model
        The initialized model for feature extraction
    framesFolder: str
        The frames folder address to extract visual features from
    outputDir: str
        The visual features directory to save the extracted features
    configs: dict
        The configurations dictionary
    
    Returns
    -------
    framesFolders :list
        A list of fetched frames folders
    """
    # Variables
    packetIndex = 1  # Holds the name of the packet, e.g. Packet0001
    packetCounter = 0
    modelInputSize = 0
    modelPreprocess = None
    startTime = time.time()
    imageTypes = configs['image_formats']
    totalFrames = len(os.listdir(framesFolder))
    modelName = configs['feature_extractor_model']
    remainingFrames = len(os.listdir(framesFolder))
    frameFeatureDF = pd.DataFrame(columns=['frameId', 'features'])
    # Prepare the model-specific variables
    if modelName == 'incp3':
        # Load proper imports
        from tensorflow.keras.applications.inception_v3 import preprocess_input
        # Load Inception-v3 model variables
        modelInputSize = 299  # Default input size for Inception-v3 model
        modelPreprocess = preprocess_input
    elif modelName == 'vgg19':
        # Load proper imports
        from tensorflow.keras.applications.vgg19 import preprocess_input
        # Load VGG-19 model variables
        modelInputSize = 224 # Default input size for Inception-v3 model
        modelPreprocess = preprocess_input
    else:
        print(f"Feature extraction model '{modelName}' is not supported! Exiting ...")
        return
    # Loop over the frames in the folder
    for imageType in imageTypes:
        for frameFile in glob(f'{framesFolder}/*.{imageType}'):
            # Variables
            frameFileName = os.path.basename(frameFile)
            framesFolder = os.path.basename(os.path.dirname(frameFile))
            try:
                # Finding frameId by removing .jpg from the name
                frameId = ('frame' + frameFile.rsplit('frame', 1)[1])[:-4]
                # Get the extracted features
                features = featureExtractor(frameFile, model, modelPreprocess, modelInputSize)
                # Check the extracted features
                if features is None:
                    print(f'- No features extracted! Skipping "{frameFileName}" in "{framesFolder}" ...')
                    continue
            except Exception as error:
                print(f'- Error while extracting the features of "{frameFileName}" in "{framesFolder}": {str(error)}')
                continue
    # Inform the user about the extraction process
    elapsedTime = '{:.2f}'.format(time.time() - startTime)
    print(
        f'- Extracted {totalFrames} features ({packetIndex-1} packets) of "{framesFolder}" in {elapsedTime} seconds!')