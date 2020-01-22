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


@app.route('/c/<text>')
def c(text):
    """ Message """
    words = text.replace('_', ' ')
    return 'C {}'.format(words)


@app.route('/python/')
@app.route('/python/<text>')
def hello_py(text='is cool'):
    """ Message """
    words = text.replace('_', ' ')
    return 'Python {}'.format(words)


if __name__ == '__main__':
    app.run()
