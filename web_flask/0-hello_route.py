#!/usr/bin/python3
""" Flask """
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello():
    """ Message """
    return 'Hello HBNB!'


if __name__ == '__main__':
    app.run()
