#!/usr/bin/python3
""" Flask """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_world():
    """ Message Hello """
    return 'Hello HBNB!'


@app.route('/hbnb')
def hello_hbnb():
    """ Message HBNB """
    return 'HBNB'


if __name__ == '__main__':
    app.run()
