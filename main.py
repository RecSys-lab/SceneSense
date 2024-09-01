#!/usr/bin/env python3

from src.utils import readConfigs
from src.runCore import runShotDetectionFromFrames, runShotDetectionFromFeatures
from src.datasets.example_scenesense import testMetadataProcess, testVisualDataProcess
from src.runCore import runTrailerDownloader, runMoviesFrameExtractor, runMoviesFramesFeatureExtractor

def main():
    print("Welcome! Starting 'SceneSense'!\n")
    # Read the configuration file
    configs = {}
    configs = readConfigs("config/config.yml")
    # If properly read, print the configurations
    if not configs:
        print("Error reading the configurations!")
        return
    # Get common configurations
    cfgGeneral = configs['config']['general']
    cfgDatasets = configs['config']['datasets']
    cfgPipeline = configs['config']['pipelines']
    # Check which mode to run
    mode = cfgGeneral['mode']
    if (mode == 'pipeline'):
        # Get the selected sub-mode
        subMode = cfgGeneral['sub_mode_pipeline']
        if (subMode == 'dl_trailers'):
            # Run the trailer downloader pipeline
            datasetInfo = {'name': cfgDatasets['visual_dataset']['name'],
                           'jsonPath': cfgDatasets['visual_dataset']['path_metadata']}
            runTrailerDownloader(cfgPipeline['movie_trailers'], datasetInfo)
        elif (subMode == 'frame_extractor'):
            # Run the movies frame extractor pipeline
            runMoviesFrameExtractor(cfgPipeline['movie_frames'])
        elif (subMode == 'feat_extractor'):
            # Run the movies features extractor pipeline
            runMoviesFramesFeatureExtractor(cfgPipeline['movie_frames_visual_features'])
        elif (subMode == 'shot_from_feat'):
            # Run the shot detection pipeline from the extracted features
            runShotDetectionFromFeatures(cfgPipeline['movie_shots']['variants']['from_features'])
        elif (subMode == 'shot_from_frame'):
            # Run the shot detection pipeline from the extracted frames
            runShotDetectionFromFrames(cfgPipeline['movie_shots']['variants']['from_frames'])
        else:
            print(f"Unsupported sub-mode '{subMode}' selected! Exiting ...")
    elif (mode == 'ds'):
        # Get the selected sub-mode
        subMode = cfgGeneral['sub_mode_ds']
        if (subMode == 'scenesense_meta'):
            testMetadataProcess()
        elif (subMode == 'scenesense_visual'):
            testVisualDataProcess()
        else:
            print(f"Unsupported sub-mode '{subMode}' selected! Exiting ...")
    elif (mode == 'recsys'):
        # Get the selected sub-mode
        subMode = cfgGeneral['sub_mode_recsys']
    else:
        print(f"Unsupported mode '{mode}' selected! Exiting ...")
    # Finish the program
    print("\nStopping 'SceneSense'!")

if __name__ == "__main__":
    main()