import os
import time
import pandas as pd
from src.pipelines.shots.utils import calculateCosineSimilarity, initShotsFolder, mergePacketsIntoDataFrame

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
        try:
            # Variables
            packetCounter = 0
            startTime = time.time()
            folderName = os.path.basename(featuresFolder)
            packetIndex = 1  # Holds the name of the packet, e.g. Packet0001
            shotsDataFrame = pd.DataFrame(columns=['frameId', 'features'])
            # Explore the folder containing JSON files (packets) of extracted visual features
            totalPackets = len(os.listdir(featuresFolder))
            print(f'- Processing {totalPackets} packets of movie "{folderName}" ...')
            # Iterate over the packet files to collect them all in a single dataframe
            featuresDF = mergePacketsIntoDataFrame(featuresFolder)
            # Check if the features dataframe is empty
            if featuresDF.empty:
                print(f'- The DataFrame containing packets data of "{folderName}" is empty! Skipping ...')
                continue
            # Cosine Similarity Calculation
            similarityDF = calculateCosineSimilarity(folderName, featuresDF)
            # Print the number of frames in the features dataframe
            print(f'- {len(featuresDF)} packets combined into a single DataFrame for processing!')
            # Inform the user
            elapsedTime = '{:.2f}'.format(time.time() - startTime)
            print(
                f'- Extracted {packetIndex-1} shot packets from {totalPackets} packets of "{folderName}" in {elapsedTime} seconds!')
        except Exception as error:
            print(f'- Error while picking the shots of "{folderName}" in "{featuresFolder}": {str(error)}')
            continue


#             # Find shot boundaries and select the middle frame of each shot
#             boundaryFrames, avgShotLength = shotBoundaryDetection(similarityDF)
#             avgShotLength = round(avgShotLength, 2)
#             # Create a dataframe with the middle frames
#             keyframesDF = featuresDF[featuresDF.index.isin(boundaryFrames)]
#             remainingNumberOfFrames = len(keyframesDF)
#             # Save the keyframes
#             movieBoundaryCountDF = movieBoundaryCountDF.append(
#                 {'movieId': movieId, 'framesCount': len(featuresDF), 'avgShotLength': avgShotLength, 'shotBoundaryCount': len(keyframesDF)}, ignore_index=True)
#             # Iterate over the keyframes to save them in packets
#             for index, row in keyframesDF.iterrows():
#                 # Append rows to dataFrame
#                 dataFrame = dataFrame.append(
#                     {'frameId': row['frameId'], 'features': row['features']}, ignore_index=True)
#                 packetCounter += 1
#                 # Reset the counter only if packetCounter reaches the limit (packetSize) and there is no more frames for process
#                 remainingNumberOfFrames -= 1
#                 resetCounter = (packetCounter == packetSize) or (
#                     remainingNumberOfFrames == 0)
#                 if (resetCounter):
#                     # Save dataFrame as packet in a file
#                     packetManager(packetIndex, dataFrame,
#                                   movieId, shotFolder)
#                     # Clear dataFrame rows
#                     dataFrame.drop(dataFrame.index, inplace=True)
#                     packetCounter = 0
#                     packetIndex += 1