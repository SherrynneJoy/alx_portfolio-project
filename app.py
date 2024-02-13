#!/usr/bin/python3
"""product api"""
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = {'id': product_id, 'name': 'Product Name', 'price': 10.99, 'description': 'Product Description'}
    return render_template('product_detail.html', product=product)

# Placeholder functions for database interaction
def get_products():
    return []

def get_product(product_id):
    return None

if __name__ == '__main__':
    app.run(debug=True)
