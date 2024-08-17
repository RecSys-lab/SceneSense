import os
from src.core.pipeline.visual_features.utils import initFeaturesFolder
from src.core.pipeline.visual_features.models.vgg19 import InitModelVgg19
from src.core.pipeline.visual_features.models.inception3 import InitModelInception3

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
    # Check the feature extraction model
    model = None
    modelName = configs['feature_extractor_model']
    if modelName == 'incp3':
        model = InitModelInception3(configs)
    elif modelName == 'vgg19':
        model = InitModelVgg19(configs)
    else:
        print(f"Feature extraction model '{modelName}' is not supported! Exiting ...")
        return
    # Iterate on all frame folders in the given root directory
    for framesFolder in movieFramesPaths:
        # Preparing the output frames directory
        framesFolder = os.path.normpath(framesFolder)
        print(f"- Extracting features from the frames in '{framesFolder}' ...")
        outputDir = initFeaturesFolder(framesFolder, configs['features_path'])
        if not outputDir:
            continue
