from flask import Flask, render_template, request, redirect, jsonify
import sqlite3
import string
import random
import qrcode
import io
import base64

app = Flask(__name__)

def generate_short_code():
    characters = string.ascii_letters + string.digits
    return ''.join(random.choice(characters) for _ in range(6))

def get_db():
    conn = sqlite3.connect('urls.db')
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS urls
                     (id INTEGER PRIMARY KEY, short_code TEXT UNIQUE, long_url TEXT, clicks INTEGER)''')
    conn.commit()
    return conn

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/api/shorten', methods=['POST'])
def shorten():
    data = request.json
    long_url = data.get('url')
    short_code = generate_short_code()
    
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO urls VALUES (NULL, ?, ?, 0)", (short_code, long_url))
    conn.commit()
    conn.close()
    
    qr = qrcode.QR(image_factory=qrcode.image.svg.SvgPathImage)
    qr.add_data(f'http://localhost:5000/{short_code}')
    qr.make()
    img = qr.make_image()
    
    return jsonify({'short_code': short_code, 'short_url': f'http://localhost:5000/{short_code}'})

@app.route('/<short_code>')
def redirect_to_long(short_code):
    conn = get_db()
    cursor = conn.cursor()
    cursor.execute("SELECT long_url FROM urls WHERE short_code = ?", (short_code,))
    result = cursor.fetchone()
    conn.close()
    
    if result:
        return redirect(result[0])
    return "URL not found", 404

if __name__ == '__main__':
    app.run(debug=True)
