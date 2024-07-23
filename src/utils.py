#!/usr/bin/env python3

import yaml

def readConfigs(configPath: str):
    """
    Read the configuration file and store the values in a dictionary

    Parameters
    -------
    configPath: str
        The path to the configuration file

    Returns
    -------
    windowTitle: str
        The name of the window to be shown
    """
    with open(configPath) as cfg:
        try:
            print("Reading the configuration file...")
            return yaml.safe_load(cfg)
        except yaml.YAMLError as err:
            print(f"[Error] Error while reading the configuration file: {err}")