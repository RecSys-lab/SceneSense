#!/usr/bin/env python3

from src.utils import readConfigs
from src.multimodal.fused.overlap_checker import runVisualTextualDatasetsOverlapChecker
from src.datasets.runDataset import testMetadataProcess, testVisualDataProcess, runMovieLens25
from src.runCore import runShotDetectionFromFrames, runShotDetectionFromFeatures, runAggFeatures
from src.multimodal.fused.fuse_visual_textual import fuseTextualWithMMTF, fuseTextualWithSceneSense
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
    cfgRecSys = configs['config']['multimodal']
    cfgPipeline = configs['config']['pipelines']
    # Check which mode to run
    mode = cfgGeneral['mode']
    if (mode == 'pipeline'):
        # Get the selected sub-mode
        subMode = cfgGeneral['sub_mode_pipeline']
        if (subMode == 'dl_trailers'):
            # Run the trailer downloader pipeline
            datasetInfo = {'name': cfgDatasets['visual_dataset']['scenesense']['name'],
                           'jsonPath': cfgDatasets['visual_dataset']['scenesense']['path_metadata']}
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
        elif (subMode == 'agg_features'):
            # Run the feature aggregation pipeline
            runAggFeatures(cfgPipeline['feature_aggregation'])
        else:
            print(f"Unsupported sub-mode '{subMode}' selected! Exiting ...")
    elif (mode == 'ds'):
        # Get the selected sub-mode
        subMode = cfgGeneral['sub_mode_ds']
        if (subMode == 'scenesense_meta'):
            testMetadataProcess()
        elif (subMode == 'scenesense_visual'):
            testVisualDataProcess()
        elif (subMode == 'movielens_25m'):
            runMovieLens25(cfgDatasets['text_dataset'])
        else:
            print(f"Unsupported sub-mode '{subMode}' selected! Exiting ...")
    elif (mode == 'recsys'):
        # Get the selected sub-mode
        subMode = cfgGeneral['sub_mode_recsys']
        if (subMode == 'overlap_checker'):
            # Check the overlap between the SceneSense, MMTF, and the LLM-enriched dataset for recommendation
            runVisualTextualDatasetsOverlapChecker(cfgRecSys, cfgDatasets)
        elif (subMode == 'visual_text_fusion'):
            # Fusion of the visual (MMTF) and textual features for recommendation
            # fuseTextualWithMMTF(cfgRecSys, cfgDatasets)
            # Fusion of the visual (SceneSense) and textual features for recommendation
            fuseTextualWithSceneSense(cfgRecSys, cfgDatasets)
    else:
        print(f"Unsupported mode '{mode}' selected! Exiting ...")
    # Finish the program
    print("\nStopping 'SceneSense'!")

if __name__ == "__main__":
    main()