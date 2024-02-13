#!/usr/bin/python3
"""product api"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/', strict_slashes=False)
@app.route('/landing', strict_slashes=False)
def index():
    return render_template('landing.html')

@app.route('/products', strict_slashes=False)
def products():
    return render_template('products.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
