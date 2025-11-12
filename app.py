from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO, emit
import qrcode
import io
import base64

app = Flask(__name__)
socketio = SocketIO(app)

# In-memory data
users = {}
chats = {}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat/<username>')
def chat(username):
    return render_template('chat.html', username=username, users=list(users.keys()))

@app.route('/add_user', methods=['POST'])
def add_user():
    username = request.json.get('username')
    if username not in users:
        users[username] = {"friends": []}
    return jsonify({"message": "User added", "username": username})

@app.route('/generate_qr/<username>')
def generate_qr(username):
    url = f"http://127.0.0.1:5000/add_friend/{username}"
    img = qrcode.make(url)
    buffer = io.BytesIO()
    img.save(buffer, format="PNG")
    qr_b64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return jsonify({"qr": qr_b64})

@app.route('/add_friend/<username>')
def add_friend(username):
    friend = request.args.get('friend')
    if username in users and friend in users:
        if friend not in users[username]["friends"]:
            users[username]["friends"].append(friend)
        if username not in users[friend]["friends"]:
            users[friend]["friends"].append(username)
        return jsonify({"message": f"{friend} added as friend!"})
    return jsonify({"error": "User not found"}), 404

@socketio.on('send_message')
def handle_message(data):
    sender = data['sender']
    receiver = data['receiver']
    message = data['message']

    chat_key = tuple(sorted([sender, receiver]))
    chats.setdefault(chat_key, []).append((sender, message))

    emit('receive_message', {'sender': sender, 'message': message}, room=receiver)
    print(f"Message from {sender} → {receiver}: {message}")

@socketio.on('join')
def on_join(data):
    username = data['username']
    emit('user_joined', {'username': username}, broadcast=True)
    print(f"{username} joined the chat")

if __name__ == "__main__":
    socketio.run(app, debug=True)
