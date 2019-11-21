import socketio

# standard Python
sio = socketio.Client(reconnection=False)

@sio.on('get proximity')
def on_message(data):
    print('I received a message!')
    sio.emit('action', { 'type': 'move', 'direction': 'right' })

@sio.on('dead of hunger''')
def on_dead():
    print('DEAD')

sio.connect('http://localhost:3000')