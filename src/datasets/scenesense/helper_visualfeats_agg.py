#!/usr/bin/env python3

import pandas as pd
from src.utils import loadJsonFromUrl
from src.datasets.scenesense.helper_metadata import fetchAllMovieIds

def allAggregatedFeatureAddresses(datasetUrl: str, featureModels: list, movieIds: list, aggFeatureSources: list):
  """
  Generates a list of addresses for all aggregated features of movies in the dataset.

  Parameters:
      datasetUrl (str): The base URL of the dataset.
      featureModels (list): A list of feature models used for feature extraction.
      movieIds (list): A list of all movie IDs.
      aggFeatureSources (list): A list of aggregated feature sources.

  Returns:
      aggFeatureAddresses (dict): A dictionary of all aggregated feature addresses.
  """
  # Variables
  aggFeatureAddresses = {
    "full_movies_agg": {
      "incp3": [],
      "vgg19": []
    },
    "movie_shots_agg": {
      "incp3": [],
      "vgg19": []
    },
    "movie_trailers_agg": {
      "incp3": [],
      "vgg19": []
    }
  }
  # Loop over all movies
  for movieId in movieIds:
    # Loop over all feature models
    for featureModel in featureModels:
      # Loop over all aggregated feature sources
      for aggFeatureSource in aggFeatureSources:
        # Generate address
        address = datasetUrl + f"{aggFeatureSource}/{featureModel}/{movieId}.json"
        aggFeatureAddresses[aggFeatureSource][featureModel].append(address)
  # Return
  return aggFeatureAddresses

def generatedAggFeatureAddresses(cfgDatasets: dict):
  """
  Fetches all aggregated features of movies from the dataset and combines them into a DataFrame.

  Parameters:
      datasetUrl (str): The base URL of the dataset.
      gFeature (str): The feature type (e.g., "audio", "visual").
      gModel (str): The model used for feature extraction.
      gMovieId (int): The ID of the movie.

  Returns:
      moviePackets (list): A list of all packets of the movie.  
  """
  # Variables
  rawFilesUrl = cfgDatasets['visual_dataset']['scenesense']['path_raw']
  featureModels = cfgDatasets['visual_dataset']['scenesense']['feature_models']
  datasetMetadataUrl = cfgDatasets['visual_dataset']['scenesense']['path_metadata']
  aggFeatureSources = cfgDatasets['visual_dataset']['scenesense']['agg_feature_sources']
  # Fetch JSON metadata from the URL
  print(f"- Fetching URL from '{datasetMetadataUrl}' ...")
  jsonData = loadJsonFromUrl(datasetMetadataUrl)
  # Fetch all movie IDs
  print(f"- Fetching all movie IDs ...")
  movieIds = fetchAllMovieIds(jsonData)
  print(f"- Found {len(movieIds)} movie IDs ...")
  # Generating a list of addresses to fetch the aggregated features
  print(f"- Generating a list of addresses to fetch the aggregated features ...")
  aggFeatureAddresses = allAggregatedFeatureAddresses(rawFilesUrl, featureModels, movieIds, aggFeatureSources)
  # Count all members of aggFeatureAddresses
  numberOfGeneratedAddresses = len(aggFeatureAddresses) * len(aggFeatureAddresses['full_movies_agg']) * len(aggFeatureAddresses['full_movies_agg']['incp3'])
  print(f"- Generated {numberOfGeneratedAddresses} aggregated feature addresses, e.g., {aggFeatureAddresses['full_movies_agg']['incp3'][0]} ...")
  # Return
  return aggFeatureAddresses
  
def loadAggregatedFeaturesIntoDataFrame(aggFeatureAddresses: list):
  """
  Loads all aggregated features of movies from the dataset into a DataFrame.

  Parameters:
      aggFeatureAddresses (list): A list of all aggregated feature addresses.

  Returns:
      dfAggFeaturesMax (DataFrame): A DataFrame containing the maximum aggregated features.
      dfAggFeaturesMean (DataFrame): A DataFrame containing the mean aggregated features.
  """
  # Variables
  counter = 0
  dfAggFeaturesMax = pd.DataFrame()
  dfAggFeaturesMean = pd.DataFrame()
  # Loop over all addresses
  for item in aggFeatureAddresses:
    # Variables
    itemId = item.split('/')[-1].split('.')[0]
    # Fetch the JSON data from the URL
    jsonData = loadJsonFromUrl(item)
    aggFeatMax, aggFeatMean = jsonData[0]['Max'], jsonData[0]['Mean']
    # Convert the list to a string, like "0.1,0.2,0.3"
    aggFeatMax = ','.join(map(str, aggFeatMax))
    aggFeatMean = ','.join(map(str, aggFeatMean))
    # Add "" to the string, making it similar to MMTF format
    aggFeatMax, aggFeatMean = f'"{aggFeatMax}"', f'"{aggFeatMean}"'
    # Append to the DataFrames
    dfAggFeaturesMax = pd.concat([dfAggFeaturesMax, pd.DataFrame([{'itemId': int(itemId), 'embedding': aggFeatMax}])],
                                           ignore_index=True)
    dfAggFeaturesMean = pd.concat([dfAggFeaturesMean, pd.DataFrame([{'itemId': itemId, 'embedding': aggFeatMean}])],
                                            ignore_index=True)
    # Better logging for the user
    counter += 1
    if counter % 100 == 0:
      print(f"- Loading aggregated features ({int(counter / len(aggFeatureAddresses) * 100)}%) ...")
  # Return
  return dfAggFeaturesMax, dfAggFeaturesMean