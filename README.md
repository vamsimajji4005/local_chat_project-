
# 📱 Local Chat — University LAN Chat App

A modern WhatsApp-style web chat application built with **Flask** and **Socket.IO**, designed for LAN or local university networks.

---

## 🚀 Features

- Real-time chatting (powered by Flask-SocketIO)
- Modern Bootstrap 5 + Icons UI
- Animated chat interface
- User profiles with photos & university info
- QR code-based friend requests (scan to connect!)
- Works locally (LAN IP) — no internet required

---

## 🧩 Tech Stack

- **Frontend:** HTML, CSS (Bootstrap 5), JavaScript (Socket.IO)
- **Backend:** Flask + Flask-SocketIO
- **QR Codes:** Python `qrcode` library
- **No database required** — all chat data resets on restart

---

## ⚙️ Installation & Setup

### Step 1: Clone or download the project
```bash
cd C:\Users\ADMIN\Desktop\local_chat_project
```

### Step 2: Install dependencies
```bash
pip install flask flask-socketio qrcode[pil]
```

### Step 3: Run the server
```bash
python app.py
```

### Step 4: Open in browser
Go to:
```
http://127.0.0.1:5000
```
or from another device on LAN:
```
http://<your-local-ip>:5000
```

---

## 💬 Usage

1. Start the app (`python app.py`)
2. Open the chat page in a browser
3. Scan or share QR codes to add friends
4. Send and receive messages in real-time!

---

## 🧱 Project Structure

```
local_chat_project/
│
├── app.py                  # Flask backend
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
├── /templates/
│   └── index.html          # Frontend HTML template
│
├── /static/
│   ├── /css/
│   │   └── style.css       # Styles
│   ├── /js/
│   │   └── main.js         # Client-side Socket.IO logic
│   └── /images/            # Profile & university logos
│
└── /venv/                  # (Optional) Virtual environment
```

---

## 📸 Screenshots

*(You can add screenshots of your app here)*

---

## 👨‍💻 Author
Developed by **Vamsi Majji**  
For educational and demonstration purposes.
