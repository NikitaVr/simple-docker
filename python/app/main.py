from flask import Flask, jsonify, request
from flask_cors import CORS
import os
import pymongo
import json
from bson import ObjectId

class JSONEncoder(json.JSONEncoder):
    def default(self, o):
        if isinstance(o, ObjectId):
            return str(o)
        return json.JSONEncoder.default(self, o)

app = Flask(__name__)
CORS(app)

animals = ["cat", "dog"]

client = pymongo.MongoClient("mongodb+srv://<USER>:<PASSWORD>@cluster0-mvqxw.mongodb.net/test?retryWrites=true&w=majority")
db = client.Zoo


@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/list/<int:index>')
def getAnimal(index):
    return jsonify(animals[index])


@app.route('/add', methods=['POST'])
def createAnimal():
    animals.append(request_json['animal'])
    return "added"


@app.route('/user/<username>')
def showUser(username):
    # show the user profile for that user
    return 'User %s' % username

@app.route('/animals/all')
def getAllAnimals():
    allAnimals = list(db.Animals.find({}))
    return JSONEncoder().encode(allAnimals)


if __name__ == "__main__":
    # Only for debugging while developing
    app.run(host='0.0.0.0', debug=True, port=os.environ.get('PORT', 80))
