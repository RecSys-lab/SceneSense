#!/usr/bin/env python3

def InitModelInception3():
    # Load Inception-v3 model
    from tensorflow.keras.applications import InceptionV3
    from tensorflow.keras.models import Model
    
    # Create a model
    model = InceptionV3()
    model = Model(inputs=model.inputs, outputs=model.layers[-2].output)
    # keras.applications.InceptionV3(
    #     include_top=True,
    #     weights="imagenet",
    #     input_tensor=None,
    #     input_shape=None,
    #     pooling=None,
    #     classes=1000,
    #     classifier_activation="softmax",
    # )
    
    # Return the model
    return model