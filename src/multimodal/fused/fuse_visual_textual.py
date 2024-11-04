#!/usr/bin/env python3

import os
import numpy as np
import pandas as pd
from src.utils import loadDataFromCSV

def fuseTextualWithMMTF(cfgRecSys: dict, cfgDatasets: dict):
    """
    Fuse the textual data with the MMTF-14K dataset for recommendation, generating the fused dataset as pandas DataFrame

    Parameters
    ----------
    cfgRecSys :dict
        The configurations dictionary for the recommendation system
    cfgDatasets :dict
        The configurations dictionary for the datasets
    """
    # Variables
    outputDir = os.path.normpath(cfgRecSys['fused']['output_dir'])
    if not os.path.exists(outputDir):
        os.makedirs(outputDir)
    # (A) Read the LLM-enriched dataset
    textCSVFilePath = os.path.normpath(cfgRecSys['textual']['llm_enriched_file_path'])
    print(f"I. Reading the enriched text dataset CSV file from '{textCSVFilePath}' ...")
    # Load the CSV data
    enrichedLLMDataset = loadDataFromCSV(textCSVFilePath)
    if enrichedLLMDataset is None:
        return
    print(f"- Loaded {len(enrichedLLMDataset)} records from the LLM-enriched dataset!")
    # print(enrichedLLMDataset.head())
    # Filter only the 'itemId' and 'title' columns
    enrichedLLMDataset = enrichedLLMDataset[['itemId', 'title', 'genres']]
    print(f"- Filtered the dataset to contain only 'itemId' and 'title' columns! Check the first 3 records:")
    print(enrichedLLMDataset.head(3))
    # (2) Read the MMTF-14K dataset
    mmtfDatasetRootUrl = cfgDatasets['visual_dataset']['mmtf']['path_root']
    # Join the paths
    mmtfVisualAvgCSVFilePath = os.path.join(mmtfDatasetRootUrl, 'Visual', 'AlexNet features', 'Avg', 'AlexNetFeatures - AVG - fc7.csv')
    mmtfVisualMedCSVFilePath = os.path.join(mmtfDatasetRootUrl, 'Visual', 'AlexNet features', 'Med', 'AlexNetFeatures - MED - fc7.csv')
    mmtfVisualAvgVarCSVFilePath = os.path.join(mmtfDatasetRootUrl, 'Visual', 'AlexNet features', 'AvgVar', 'AlexNetFeatures - AVGVAR - fc7.csv')
    mmtfVisualMedMadCSVFilePath = os.path.join(mmtfDatasetRootUrl, 'Visual', 'AlexNet features', 'MedMad', 'AlexNetFeatures - MEDMAD - fc7.csv')
    # Round#1: Load the 'Avg' dataset
    print(f"\nII-A. Reading the MMTF-14K Visual Features (Avg) from '{mmtfVisualAvgCSVFilePath}' ...")
    tmpVisualDataFrame = loadVisualFeaturesCSVIntoDataFrame(mmtfVisualAvgCSVFilePath)
    if tmpVisualDataFrame is None:
        return
    # Merging the textual and visual data
    fusedDataset = pd.merge(enrichedLLMDataset, tmpVisualDataFrame, on='itemId', how='inner')
    print(f"- Merging Textual and Visual (Avg) datasets based on the 'itemId' resulted in '{len(fusedDataset)}' items! Check the first 3 records:")
    print(fusedDataset.head(3))
    # Save the fused dataset to a CSV file
    outputFile = os.path.join(outputDir, 'fused_llm_mmtf_avg.csv')
    outputFile = os.path.normpath(outputFile)
    print(f"- Saving the fused dataset to '{outputFile}' ...")
    fusedDataset.to_csv(outputFile, index=False)
    # Round#2: Load the 'Med' dataset
    print(f"\nII-B. Reading the MMTF-14K Visual Features (Med) from '{mmtfVisualMedCSVFilePath}' ...")
    tmpVisualDataFrame = loadVisualFeaturesCSVIntoDataFrame(mmtfVisualMedCSVFilePath)
    if tmpVisualDataFrame is None:
        return
    # Merging the textual and visual data
    fusedDataset = pd.merge(enrichedLLMDataset, tmpVisualDataFrame, on='itemId', how='inner')
    print(f"- Merging Textual and Visual (Med) datasets based on the 'itemId' resulted in '{len(fusedDataset)}' items! Check the first 3 records:")
    print(fusedDataset.head(3))
    # Save the fused dataset to a CSV file
    outputFile = os.path.join(outputDir, 'fused_llm_mmtf_med.csv')
    outputFile = os.path.normpath(outputFile)
    print(f"- Saving the fused dataset to '{outputFile}' ...")
    fusedDataset.to_csv(outputFile, index=False)
    # Round#3: Load the 'AvgVar' dataset
    print(f"\nII-C. Reading the MMTF-14K Visual Features (AvgVar) from '{mmtfVisualAvgVarCSVFilePath}' ...")
    tmpVisualDataFrame = loadVisualFeaturesCSVIntoDataFrame(mmtfVisualAvgVarCSVFilePath)
    if tmpVisualDataFrame is None:
        return
    # Merging the textual and visual data
    fusedDataset = pd.merge(enrichedLLMDataset, tmpVisualDataFrame, on='itemId', how='inner')
    print(f"- Merging Textual and Visual (AvgVar) datasets based on the 'itemId' resulted in '{len(fusedDataset)}' items! Check the first 3 records:")
    print(fusedDataset.head(3))
    # Save the fused dataset to a CSV file
    outputFile = os.path.join(outputDir, 'fused_llm_mmtf_avgvar.csv')
    outputFile = os.path.normpath(outputFile)
    print(f"- Saving the fused dataset to '{outputFile}' ...")
    fusedDataset.to_csv(outputFile, index=False)
    # Round#4: Load the 'MedMad' dataset
    print(f"\nII-D. Reading the MMTF-14K Visual Features (MedMad) from '{mmtfVisualMedMadCSVFilePath}' ...")
    tmpVisualDataFrame = loadVisualFeaturesCSVIntoDataFrame(mmtfVisualMedMadCSVFilePath)
    if tmpVisualDataFrame is None:
        return
    # Merging the textual and visual data
    fusedDataset = pd.merge(enrichedLLMDataset, tmpVisualDataFrame, on='itemId', how='inner')
    print(f"- Merging Textual and Visual (MedMad) datasets based on the 'itemId' resulted in '{len(fusedDataset)}' items! Check the first 3 records:")
    print(fusedDataset.head(3))
    # Save the fused dataset to a CSV file
    outputFile = os.path.join(outputDir, 'fused_llm_mmtf_medmad.csv')
    outputFile = os.path.normpath(outputFile)
    print(f"- Saving the fused dataset to '{outputFile}' ...")
    fusedDataset.to_csv(outputFile, index=False)
    print("\nFusion completed successfully!")

def loadVisualFeaturesCSVIntoDataFrame(givenCSVFilePath: str):
    """
    Load the visual features CSV file into a pandas DataFrame

    Parameters
    ----------
    givenCSVFilePath :str
        The path to the visual features CSV file
    """
    # Normalize the path
    givenCSVFilePath = os.path.normpath(givenCSVFilePath)
    # Load the CSV data
    MMTFDataset = loadDataFromCSV(givenCSVFilePath)
    if MMTFDataset is None:
        return
    # Prepare the data frame
    MMTFDataset.rename(columns={'movieId': 'itemId'}, inplace=True)
    # Convert deep feature columns to a single embedding column
    embeddingCols = [col for col in MMTFDataset.columns if col.startswith('deep')]
    MMTFDataset['embedding'] = MMTFDataset[embeddingCols].apply(lambda row: ','.join(map(str, row)), axis=1)
    # Drop the original deep feature columns
    MMTFDataset = MMTFDataset[['itemId', 'embedding']]
    print(f"- Loaded {len(MMTFDataset)} records into the memory! Check the first 3 records:")
    print(MMTFDataset.head(3))
    return MMTFDataset