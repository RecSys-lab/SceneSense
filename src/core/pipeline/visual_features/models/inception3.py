#!/usr/bin/env python3

def InitModelInception3(configs: dict):
    """
    Initializes the Inception-v3 (GoogleNet) model for feature extraction
        - The model expects color images to have the square shape 299 x 299
        - Running the example will load the Inception-v3 model and download the model weights

    Parameters
    ----------
    configs: dict
        The configurations dictionary
    
    Returns
    -------
    model: Model
        The initialized Inception-v model
    """
    print("- Initializing the Inception-v3 model for feature extraction ...")
    # Variables
    model = None
    inputSize = 299  # Default input size for Inception-v3 model
    # Load Inception-v3 model
    from tensorflow.keras.applications.inception_v3 import InceptionV3, preprocess_input
    # Create a model
    model = InceptionV3()
    # Return the model
    return model
    # model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
    # # keras.applications.InceptionV3(
    # #     include_top=True,
    # #     weights="imagenet",
    # #     input_tensor=None,
    # #     input_shape=None,
    # #     pooling=None,
    # #     classes=1000,
    # #     classifier_activation="softmax",
    # # )

# import os
# from keras import Model
# from utils import logger
# from config import featuresDir
# from FeatureExtraction.modelRunner import modelRunner
# from keras.applications.inception_v3 import InceptionV3, preprocess_input

# # About Inception-v3 (GoogleNet):
# # The model expects color images to have the square shape 299×299
# # Running the example will load the Inception-v3 model and download the model weights

# # Static variables
# vggInputSize = 299


# def Inception3Launcher(foldersList: list):
#     logger('Launching Inception-v3 network ...')
#     # Create a folder for outputs if not existed
#     outputPath = f'{featuresDir}/Incp3'
#     if not os.path.exists(outputPath):
#         os.mkdir(outputPath)
#     # Load model
#     model = InceptionV3()
#     # Removing the final output layer, so that the second last fully connected layer with 2,048 nodes will be the new output layer
#     model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
#     modelRunner(outputPath, foldersList, vggInputSize, model, preprocess_input)
