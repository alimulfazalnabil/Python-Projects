from flask import Flask, render_template, session, request
from flask_socketio import SocketIO, emit, join_room, leave_room
import json
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
socketio = SocketIO(app, cors_allowed_origins="*")

users = {}
rooms = {"general": []}

@app.route('/')
def index():
    return render_template('index.html')

@socketio.on('connect')
def handle_connect():
    session['user_id'] = request.sid
    print(f"User connected: {request.sid}")

@socketio.on('join')
def on_join(data):
    username = data['username']
    room = data.get('room', 'general')
    
    session['username'] = username
    session['room'] = room
    
    join_room(room)
    
    if room not in rooms:
        rooms[room] = []
    
    rooms[room].append(username)
    users[request.sid] = {'username': username, 'room': room}
    
    emit('message', {
        'msg': f'{username} has joined the chat',
        'username': 'System',
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, room=room)
    
    emit('user_list', {'users': rooms[room]}, room=room)

@socketio.on('message')
def handle_message(data):
    room = session.get('room', 'general')
    username = session.get('username', 'Anonymous')
    
    emit('message', {
        'msg': data['msg'],
        'username': username,
        'timestamp': datetime.now().strftime('%H:%M:%S')
    }, room=room)

@socketio.on('disconnect')
def handle_disconnect():
    if request.sid in users:
        user = users[request.sid]
        username = user['username']
        room = user['room']
        
        if room in rooms and username in rooms[room]:
            rooms[room].remove(username)
        
        emit('message', {
            'msg': f'{username} has left the chat',
            'username': 'System',
            'timestamp': datetime.now().strftime('%H:%M:%S')
        }, room=room)
        
        emit('user_list', {'users': rooms.get(room, [])}, room=room)
        
        del users[request.sid]

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=5000)
