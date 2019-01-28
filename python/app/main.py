from flask import Flask, jsonify, request
from flask_cors import CORS
import os

app = Flask(__name__)
CORS(app)

animals = ["cat", "dog"]


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/list/<int:index>')
def nearby_links(index):
    return jsonify(animals[index])


@app.route('/add', methods=['POST'])
def create_link():
    animals.append(request_json['animal'])
    return "added"


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))
