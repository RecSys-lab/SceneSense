import os

def extractMovieFeatures(configs: dict, movieFramesPaths: list):
    """
    Extracts frames from the given set of fetched movies

    Parameters
    ----------
    configs :dict
        The configurations dictionary
    movieFramesPaths :list
        The list of movie frames paths
    """
    print("Extracting frames from the given set of movie videos ...")