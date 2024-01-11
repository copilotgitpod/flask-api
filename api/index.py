from flask import Flask, jsonify
from flask_cors import CORS  # You need to install flask-cors first
import random

app = Flask(__name__)
CORS(app)  # This will enable CORS for all routes

news = [
    {'title': 'News 1', 'content': 'Content 1'},
    {'title': 'News 2', 'content': 'Content 2'},
    {'title': 'News 3', 'content': 'Content 3'},
    # ... Add more news here
]

@app.route('/api/news/', methods=['GET'])
def get_all_news():
    return jsonify(news)

@app.route('/api/random-news/', methods=['GET'])
def get_random_news():
    return jsonify(random.choice(news))

if name == '__main__':
    app.run(debug=True)