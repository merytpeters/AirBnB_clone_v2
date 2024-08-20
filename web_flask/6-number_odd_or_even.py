#!/usr/bin/python3
"""Script that starts a Flask web application"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    # Replace underscores with spaces
    text = text.replace('_', ' ')
    return f'C {text}'


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    text = text.replace('_', ' ')
    return f'Python {text}'


@app.route('/number/<int:n>', strict_slashes=False)
def number(n):
    return f'{n} is a number'


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even(n):
    if n % 2 == 0:
        result = f"is even"
    else:
        result = f"is odd"
    return render_template('6-number_odd_or_even.html', n=n, result=result)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
