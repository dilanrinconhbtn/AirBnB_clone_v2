#!/usr/bin/python3
""" Flask """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Message Hello """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """ Message HBNB """
    return 'HBNB'


if __name__ == '__main__':
    app.run()
