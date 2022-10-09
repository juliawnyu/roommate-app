"""
This is the file containing all of the pages of our app.
"""

from flask import Flask, render_template
from apis import api
# import db.db as db

app = Flask(__name__)
api.init_app(app)


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')
