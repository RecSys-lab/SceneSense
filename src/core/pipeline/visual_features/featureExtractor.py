import os
from src.core.pipeline.visual_features.utils import initFeaturesFolder

def extractMovieFeatures(configs: dict, movieFramesPaths: list):
    """
    Extracts features from the given set of extracted movie frames

    Parameters
    ----------
    configs :dict
        The configurations dictionary
    movieFramesPaths :list
        The list of movie frames paths
    """
    print("Extracting frames from the given set of extracted movie frames ...")
    # Iterate on all frame folders in the given root directory
    for framesFolder in movieFramesPaths:
        # Preparing the output frames directory
        framesFolder = os.path.normpath(framesFolder)
        print(f"- Extracting features from the frames in '{framesFolder}' ...")
        outputDir = initFeaturesFolder(framesFolder, configs['features_path'])
        if not outputDir:
            continue