import os
import string
# import cv2
# import numpy as np
from glob import glob

def initMovieVideos(configs: dict):
    """
    Pre-checks the given directory for movies and prepares it for further processing

    Parameters
    ----------
    configs: dict
        The configurations dictionary
    
    Returns
    -------
    videoFiles :list
        A list of fetched video files
    """
    # Variables
    videoFiles = []
    videoTypes = configs['video_formats']
    moviesDir, framesDir = configs['movies_path'], configs['frames_path']
    # Check if the given directory exists
    if not os.path.exists(moviesDir):
        print(f"Input movie videos directory '{moviesDir}' does not exist! Exiting ...")
        return False
    print(f"Movie videos will be processed from '{moviesDir}' ...")
    # Check if the output directory exists and create it if not
    if not os.path.exists(framesDir):
        os.mkdir(framesDir)
        print(f"Output frames will be saved in '{framesDir}' ...")
    # Check the supported video types
    print(f"Processing the input movies directory. Supported video formats are {videoTypes} ...")
    # Get the list of videos in the movies directory
    for type in videoTypes:
        videoFiles.extend(glob(f'{moviesDir}/*.{type}'))
    # Inform the user about the number of videos to process
    if len(videoFiles) == 0:
        print(f"No video files found in the given directory '{moviesDir}'! Exiting ...")
        return False
    print(f"Found {len(videoFiles)} videos to process! (e.g., {videoFiles[0]})")
    # Return the list of video files
    return videoFiles

def initFramesFolder(videoFileAddress: str, framesDir: str):
    """
    Pre-checks and generates the output frames folder

    Parameters
    ----------
    videoFileAddress: str
        The video file address to extract frames from
    framesDir: str
        The frames directory to save the extracted frames
    
    Returns
    -------
    videoFiles :list
        A list of fetched video files
    """
    # Accessing video file
    videoName = os.path.basename(videoFileAddress)
    # Normalizing the video name to assign it to the output folder
    videoName = string.capwords(
        videoName.split('.')[0].replace("_", "")).replace(" ", "")
    # Creating output folder
    if not os.path.exists(framesDir):
        os.mkdir(framesDir)
    generatedPath = framesDir + '/' + videoName
    # Do not re-generate frames for movies if there is a folder with their normalized name
    if os.path.exists(generatedPath):
        print(
            f'- Skipping movie {videoName} due to finding an output folder with the same name!')
        return
    else:
        os.mkdir(generatedPath)
        return generatedPath

# # This module receives a frame and generates aresized one while keeping the aspect ratio
# def frameResize(image, networkInputSize):
#     # Calculating frame dimensions
#     frameHeight, frameWidth = image.shape[:2]
#     aspectRatio = frameWidth / frameHeight
#     # Resize frame's width, while keeping its aspect ratio
#     generatedImageW = networkInputSize
#     generatedImageH = int(generatedImageW / aspectRatio)
#     # Scale the frame
#     scaledImage = cv2.resize(
#         image, (generatedImageW, generatedImageH), interpolation=cv2.INTER_AREA)
#     return scaledImage


# def squareFrameGenerator(image, networkInputSize):
#     finalImageDimensions = (networkInputSize, networkInputSize)
#     # Calculating frame dimensions
#     frameHeight, frameWidth = image.shape[:2]
#     aspectRatio = frameWidth / frameHeight
#     # Choosing proper interpolation
#     dimensionH, dimensionW = finalImageDimensions
#     interpolation = cv2.INTER_CUBIC  # Stretch the image
#     if (frameHeight > dimensionH or frameWidth > dimensionW):
#         interpolation = cv2.INTER_AREA  # Shrink the image
#     # Add paddings to the image
#     paddingColor = [0, 0, 0]
#     if aspectRatio > 1:  # Image is horizontal
#         generatedImageW = dimensionW
#         generatedImageH = np.round(generatedImageW / aspectRatio).astype(int)
#         verticalPadding = (dimensionH - generatedImageH) / 2
#         paddingTop, paddingBottom = np.floor(verticalPadding).astype(
#             int), np.ceil(verticalPadding).astype(int)
#         paddingLeft, paddingRight = 0, 0
#     elif aspectRatio < 1:  # Image is vertical
#         generatedImageH = dimensionH
#         generatedImageW = np.round(generatedImageH * aspectRatio).astype(int)
#         horizontalPadding = (dimensionW - generatedImageW) / 2
#         paddingLeft, paddingRight = np.floor(horizontalPadding).astype(
#             int), np.ceil(horizontalPadding).astype(int)
#         paddingTop, paddingBottom = 0, 0
#     else:  # image is square, so no changes is needed
#         generatedImageH, generatedImageW = dimensionH, dimensionW
#         paddingLeft, paddingRight, paddingTop, paddingBottom = 0, 0, 0, 0
#     # Scale the frame
#     scaledImage = cv2.resize(
#         image, (generatedImageW, generatedImageH), interpolation=interpolation)
#     scaledImage = cv2.copyMakeBorder(scaledImage, paddingTop, paddingBottom,
#                                      paddingLeft, paddingRight, borderType=cv2.BORDER_CONSTANT, value=paddingColor)
#     return scaledImage
