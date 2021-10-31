from flask import Flask, request, redirect, json, session, jsonify
from twilio.twiml.messaging_response import MessagingResponse
import firebase_admin
from firebase_admin import credentials, firestore, initialize_app
from flask_cors import CORS
import uuid
import requests


app = Flask(__name__)
CORS(app)

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred)

db = firestore.client()

# Dictionary API base URL
base_url = 'https://api.dictionaryapi.dev/api/v2/entries/en/'

# TEST


@app.route('/')
def hello():
    return "hello world"


@app.route('/word/<word>', methods=['GET'])
def word(word):
    word_dict = get_word_dict(word)
    return jsonify(get_word_definition(word_dict))


def get_word_dict(word):
    data = requests.get(base_url + word)
    return data.json()[0]


def get_word_definition(word_dict):
    return word_dict['meanings'][0]['definitions'][0]['definition']


# Will be used make a string of whatever we want to text.


def make_sms_response(word_dict):
    return
