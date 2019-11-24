import numpy as np

import tensorflow as tf

from tensorflow.keras.layers import Input, Concatenate, Conv2D, Flatten, Dense, concatenate
from tensorflow.keras.models import Model

# https://stackoverflow.com/questions/43196636/how-to-concatenate-two-layers-in-keras

# Looks very useful : https://github.com/uber-research/deep-neuroevolution

# https://github.com/CrazyBene/EvolutionaryStrategy

first_input = Input(shape=(9, 9, 1))
# first_dense = Dense(1, )(first_input)
first_conv = Conv2D(filters=81, kernel_size=2,
                    input_shape=(9, 9, 1))(first_input)
first_conv = Flatten()(first_conv)

second_input = Input(shape=(2, ))
second_dense = Dense(2, )(second_input)

merge_one = concatenate([first_conv, second_dense])
# 5 possible actions currently
merge_one = Dense(5, )(merge_one)

model = Model(inputs=[first_input, second_input], outputs=merge_one)

model.compile(loss='mean_squared_error')

sample_items = tf.cast(np.arange(81).reshape((1, 9, 9, 1)), tf.float32)
sample_coords = np.array([20.0, 20.0]).reshape((1, 2))

print(model.predict([sample_items, sample_coords]))

# combine two inputs, one is a grid of berry positions, ( later any item, just represent it as a number, 0 = nothing, 1 = berry, 2 = potion, etc.
# Can each grid spot only contain one item ? could simplify things
# server might be best to have couple of lists instead of 1 dynamic, have items, characters ??
