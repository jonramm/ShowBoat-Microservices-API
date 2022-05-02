import os
from flask import Flask, request, jsonify
import requests
import pprint

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello world!"


