import os

def aggregateMovieFeatures(configs: dict):
    """
    Aggregates features from the given set of extracted movie features

    Parameters
    ----------
    configs: dict
        The configurations dictionary
    """
    print("Aggregating visual features from the given set of extracted movie features ...")
    # Variables
    rootDir = configs['features_path']
    aggFeaturesDir = configs['agg_features_path']
    # Iterate on all feature folders in the given root directory
    for featureFolder in os.listdir(rootDir):
        # Preparing the output features directory
        featureFolder = os.path.normpath(os.path.join(rootDir, featureFolder))
        print(f"- Aggregating features from the features in '{featureFolder}' ...")
        outputDir = os.path.join(aggFeaturesDir, os.path.basename(featureFolder))
        outputDir = os.path.normpath(outputDir)
        # Skip if the output directory already exists
        if os.path.exists(outputDir):
            print(f"-- The output directory '{outputDir}' already exists! Skipping ...")
            continue
        # Otherwise, create the output directory
        os.makedirs(outputDir)