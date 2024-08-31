#!/usr/bin/env python3

from src.utils import readConfigs
from src.runCore import runShotDetectionFromFrames, runShotDetectionFromFeatures
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
        # Run the movies frame extractor pipeline
        # runShotDetectionFromFrames(cfgPipeline['movie_shots']['variants']['from_frames'])
        runShotDetectionFromFeatures(cfgPipeline['movie_shots']['variants']['from_features'])
        # Run the movies frame extractor pipeline
        # runMoviesFramesFeatureExtractor(cfgPipeline['movie_frames_visual_features'])
        # Run the movies frame extractor pipeline
        # runMoviesFrameExtractor(cfgPipeline['movie_frames'])
        # Run the trailer downloader pipeline
        # datasetInfo = {'name': cfgDatasets['visual_dataset']['name'],
        #                'jsonPath': cfgDatasets['visual_dataset']['path_metadata']}
        # runTrailerDownloader(cfgPipeline['movie_trailers'], datasetInfo)
    elif (mode == 'ds'):
        pass
    elif (mode == 'recsys'):
        pass
    else:
        print(f"Unsupported mode '{mode}' selected! Exiting ...")
    # Finish the program
    print("\nStopping 'SceneSense'!")

if __name__ == "__main__":
    main()