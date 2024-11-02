#!/usr/bin/env python3

import os
import pandas as pd
from src.utils import loadDataFromCSV, loadJsonFromUrl

def runSceneSenseLLMOverlapChecker(cfgRecSys: dict, cfgDatasets: dict):
    """
    Check the overlap between the SceneSense and the LLM-enriched dataset for recommendation

    Parameters
    ----------
    cfgRecSys :dict
        The configurations dictionary for the recommendation system
    cfgDatasets :dict
        The configurations dictionary for the datasets
    """
    # Read the enriched dataset
    csvFilePath = os.path.normpath(cfgRecSys['textual']['llm_enriched_file_path'])
    print(f"- Reading the enriched dataset CSV from '{csvFilePath}' ...")
    # Load the CSV data
    enrichedDataset = loadDataFromCSV(csvFilePath)
    if enrichedDataset is None:
        return
    print(f"- Loaded {len(enrichedDataset)} records from the enriched dataset!")
    # print(enrichedDataset.head())
    # Filter only the 'itemId' and 'title' columns
    enrichedDataset = enrichedDataset[['itemId', 'title']]
    enrichedDataset.rename(columns={'title': 'title_llm'}, inplace=True)
    print(f"- Filtered the dataset to contain only 'itemId' and 'title' columns! Check the first 3 records:")
    print(enrichedDataset.head(3))
    # Read the SceneSense dataset
    datasetMetadataUrl = cfgDatasets['visual_dataset']['path_metadata']
    print(f"- Now, fetching the SceneSense meta-data file from '{datasetMetadataUrl}' ...")
    jsonData = loadJsonFromUrl(datasetMetadataUrl)
    if jsonData is None:
        return
    # Load the data into a DataFrame
    sceneSenseMovies = pd.DataFrame(jsonData)
    print(f"- Loaded {len(sceneSenseMovies)} records from the SceneSense metadata!")
    # print(sceneSenseMovies.head())
    # Normalize the 'id' column
    sceneSenseMovies['id'] = sceneSenseMovies['id'].astype(int)
    # Filter only the 'id' and 'title' columns
    sceneSenseMovies = sceneSenseMovies[['id', 'title']]
    sceneSenseMovies.rename(columns={'id': 'itemId'}, inplace=True)
    sceneSenseMovies.rename(columns={'title': 'title_scn'}, inplace=True)
    print(f"- Filtered the dataset to contain only 'itemId' and 'title' columns! Check the first 3 records:")
    print(sceneSenseMovies.head(3))
    # Merge the two datasets
    mergedDataFrame = pd.merge(enrichedDataset, sceneSenseMovies, on='itemId', how='inner')
    print(f"- Merged the two datasets based on the 'itemId' column, resulting in {len(mergedDataFrame)} items! Check the first 3 records:")
    print(mergedDataFrame.head(3))