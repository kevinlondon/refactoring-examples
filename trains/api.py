from math import floor
from flask import Flask, request
app = Flask(__name__)

@app.route('/celsius')
def celsius():
    try:
        fahrenheit = int(request.args.get('fahrenheit'))
    except TypeError:
        return 'No degrees in Fahrenheit provided.'

    celsius = (fahrenheit - 32) * 5 / 9;
    return str(floor(celsius))
