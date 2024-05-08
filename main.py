#!/usr/bin/env python3
from src.utils import readConfigs

def main():
    print("Welcome! Starting 'SceneSense'!\n")
    # Read the configuration file
    configs = readConfigs("config/config.yml")
    # If properly read, print the configurations
    if configs:
        print(configs)
    # Finish the program
    print("\nStopping 'SceneSense'!")

main()