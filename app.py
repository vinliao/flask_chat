from flask import Flask, render_template
from flask_socketio import SocketIO, emit

app = Flask(__name__)
app.config['SECRET_KEY'] = 'secret!'
socketio = SocketIO(app)

data = [
    # {person1 : 'hey dude my first message',}
    # {person2 : 'yes man this is my second message!!!',}
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/test')
def test():
    return 'working'

@socketio.on('new chat')
def new_chat(chat_data):
    user = chat_data['user']
    text = chat_data['text']
    data.append({user, text})

    print(data)
    emit('update chat', str(data))

@socketio.on('connect')
def on_connect():
    emit('after connect', {'data': 'hey it\'s connected'})

if __name__ == '__main__':
    # app.run()
    socketio.run(app, host='0.0.0.0')