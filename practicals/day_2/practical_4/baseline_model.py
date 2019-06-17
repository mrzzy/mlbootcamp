#
# mlbootcamp
# Practical 4 
# Baseline model

import tensorflow as tf
import numpy as np
import keras.backend as K

from keras import models
from keras import layers
from keras import optimizers
from keras import regularizers

from functools import partial

# Build image classification mode with the given input shape, and the given
# no. of output classes n_outputs.
# Model hyperparameters include:
def build_model(input_shape, n_outputs, scale_depth=3, scale_width=8, **model_params):
    # clear already built graph
    K.clear_session()

    # prime dense layer with parameters
    activation = model_params.get("activation", layers.ReLU)
    regularizer = regularizers.l2(model_params.get("l2_lambda", 0))
    primed_dense = partial(layers.Dense,  64 * scale_width, 
                           kernel_regularizer=regularizer)

    # build model
    model = models.Sequential()
    # input layer
    model.add(layers.InputLayer(input_shape=input_shape))
    # hidden layers
    model.add(layers.Flatten())
    for i in range(scale_depth):
        model.add(primed_dense())
        # activation func
        model.add(activation())

        if "dropout_prob" in model_params and model_params["dropout_prob"]:
            model.add(layers.Dropout(model_params["dropout_prob"]))

    # output layers
    model.add(layers.Dense(n_outputs, activation="softmax"))

    return model
