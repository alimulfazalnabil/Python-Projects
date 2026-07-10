from flask import Flask, render_template, request, jsonify
import os
from dotenv import load_dotenv

load_dotenv()
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        data = request.json
        # Handle contact form submission
        return jsonify({'status': 'success', 'message': 'Thank you for your message!'})
    return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
