#!/usr/bin/python3
"""defines methods & attributes for users / buyers who visit app"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)
    full_name = db.Column(db.String(100))
    address = db.Column(db.Text)
    phone_number = db.Column(db.String(20))
    registration_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)

class Category(db.Model):
    __tablename__ = 'categories'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    price = db.Column(db.DECIMAL(10, 2), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'))
    image_url = db.Column(db.Text)
    created_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    category = db.relationship('Category', backref=db.backref('products', lazy=True))

class Order(db.Model):
    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    total_price = db.Column(db.DECIMAL(10, 2), nullable=False)
    order_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    status = db.Column(db.Enum('pending', 'completed', 'cancelled'), default='pending', nullable=False)
    user = db.relationship('User', backref=db.backref('orders', lazy=True))
    product = db.relationship('Product', backref=db.backref('orders', lazy=True))

class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    comment = db.Column(db.Text)
    review_date = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    user = db.relationship('User', backref=db.backref('reviews', lazy=True))
    product = db.relationship('Product', backref=db.backref('reviews', lazy=True))

class Cart(db.Model):
    __tablename__ = 'cart'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    product_id = db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    added_at = db.Column(db.TIMESTAMP, server_default=db.func.current_timestamp(), nullable=False)
    user = db.relationship('User', backref=db.backref('cart', lazy=True))
    product = db.relationship('Product', backref=db.backref('cart', lazy=True))
