import json, os
from flask import *
from os import environ as env

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


# app.route('/login')
# def login():
    # do something