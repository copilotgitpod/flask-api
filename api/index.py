from flask import Flask, jsonify
import random

app = Flask(__name__)

news = [
    {'title': 'News 1', 'content': 'Content 1'},
    {'title': 'News 2', 'content': 'Content 2'},
    {'title': 'News 3', 'content': 'Content 3'},
    # Add more news here...
]

@app.route('/api/news/', methods=['GET'])
def get_all_news():
    return jsonify(news)

@app.route('/api/random-news/', methods=['GET'])
def get_random_news():
    return jsonify(random.choice(news))

if __name__ == '__main__':
    app.run(debug=True)
