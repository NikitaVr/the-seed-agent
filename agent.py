import socketio

import network

import tensorflow as tf

from tensorflow.keras.layers import Input, Concatenate, Conv2D, Flatten, Dense, concatenate
from tensorflow.keras.models import Model

import numpy as np

reward = 0

moves = [
    {'type': 'move', 'direction': 'up'},
    {'type': 'move', 'direction': 'right'},
    {'type': 'move', 'direction': 'down'},
    {'type': 'move', 'direction': 'left'},
    {'type': 'use ground item'}
]

net = network.Network()

# standard Python
sio = socketio.Client(reconnection=False)


@sio.on('get proximity')
def on_message(data):
    global reward
    global net
    print('I received a message!')
    reward += 1
    # if('berries' in data['dynamic'][4][4]):
    #     sio.emit('action', {'type': 'use ground item'})
    #     print("USE ITEM")
    # else:
    #     sio.emit('action', {'type': 'move', 'direction': 'right'})
    sample_items = tf.cast(np.arange(81).reshape((1, 9, 9, 1)), tf.float32)
    sample_coords = np.array([20.0, 20.0]).reshape((1, 2))
    move = moves[net.getAction(sample_items, sample_coords)]
    print(move)
    sio.emit('action', move)


@sio.on('dead of hunger')
def on_dead():
    global reward
    print(f"reward: {reward}")
    print('DEAD')
    sio.emit('reset')
    # sio.disconnect()
    # sio.connect('http://localhost:3000')

    print("RESET")


sio.connect('http://localhost:3000')
