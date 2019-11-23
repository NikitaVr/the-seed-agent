import socketio

reward = 0

# standard Python
sio = socketio.Client(reconnection=False)

@sio.on('get proximity')
def on_message(data):
    global reward
    print('I received a message!')
    reward += 1
    if('berries' in data['dynamic'][4][4]):
        sio.emit('action', { 'type': 'use ground item' })
        print("USE ITEM")
    else:
        sio.emit('action', { 'type': 'move', 'direction': 'right' })

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