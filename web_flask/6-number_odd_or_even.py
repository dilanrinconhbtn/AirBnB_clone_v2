#!/usr/bin/python3
""" Flask """
from flask import Flask
from flask import render_template


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


@app.route('/number/<int:number>')
def is_number(number):
    """ Is a Number """
    return '%s is a number' % number


@app.route('/number_template/<int:number>')
def number_template(number=None):
    """return html"""
    return render_template('5-number.html', number=number)


@app.route('/number_odd_or_even/<int:number>')
def odd_even(number=None):
    """ Odd or even"""
    return render_template('6-number_odd_or_even.html', number=number)


if __name__ == '__main__':
    app.run()
