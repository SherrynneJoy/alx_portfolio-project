#!/usr/bin/python3
"""product api"""
from flask import Flask, render_template, redirect, url_for, flash, request
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, logout_user
from flask_login import login_required
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email, Length


app = Flask(__name__)
app.secret_key = 'pictureperfect'


"""MySQL configuration"""
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:@localhost/planrightdb'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'

"""Defining the user authentication model"""


class User(UserMixin, db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


"""Defining the lofin form"""


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


"""Define the login route"""


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.password == form.password.data:
            login_user(user)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('index'))
        else:
            flash('Login unsuccessful. Please check email and password.')
    return render_template('login.html', title='Login', form=form)


"""Define the logout route"""


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))


products_data = [
    {"id": 1, "name": "Product 1", "price": 10.99},
    {"id": 2, "name": "Product 2", "price": 15.99},
    {"id": 3, "name": "Product 3", "price": 20.99},
]


@app.route('/', strict_slashes=False)
@app.route('/landing', strict_slashes=False)
def index():
    return render_template('landing.html')


@app.route('/products', strict_slashes=False)
def products():
    return render_template('products.html', products=products_data)


@app.route('/product/<int:product_id>', methods=['GET'])
def product_detail(product_id):
    """Dummy function to fetch product details from database"""
    product = next((p for p in products_data if p["id"] == product_id), None)
    if product:
        return render_template('product_detail.html', product=product)
    else:
        return "Product not found", 404


@app.route('/add_to_cart/<int:product_id>', methods=['POST'])
def add_to_cart(product_id):
    """Retrieve the product from the products_data list"""
    product = next((p for p in products_data if p["id"] == product_id), None)
    if not product:
        return jsonify({"error": "Product not found"}), 404

    """Initialize the cart in the session if it doesn't exist"""
    if 'cart' not in session:
        session['cart'] = []
        print("Adding product ID:", product_id)

    """Add the product to the cart"""
    session['cart'].append(product_id)

    """Return a success message"""
    return jsonify({"message": "Product added to cart successfully"}), 200


@app.route('/cart', methods=['GET'])
def view_cart():
    """Retrieve the cart from the session"""
    cart = session.get('cart', [])

    """Calculate the total cost of the items in the cart"""
    total_cost = sum(item["price"] for item in cart)

    """Return the cart contents along with the total cost"""
    return jsonify({
        "cart": cart,
        "total_cost": total_cost
    }), 200
    return render_template('cart.html')


@app.route('/inspect_session', methods=['GET'])
def inspect_session():
    """Inspect the session data"""
    cart = session.get('cart', [])
    return jsonify({
        "message": "Session data inspected",
        "cart": cart
    }), 200


@app.route('/place_order', methods=['POST'])
def place_order():
    """Retrieve the order data from the request"""
    order_data = request.json

    """Validate the order data (e.g., ensure required fields are present)"""
    if not order_data:
        return jsonify({"error": "Invalid order data"}), 400

    """Retrieve the items in the user's shopping cart from the order data"""
    cart_items = order_data.get("cart_items")
    if not cart_items:
        return jsonify({"error": "No items in the cart"}), 400

    """Calculate the total cost of the order"""
    total_cost = sum(item.get("price", 0) * item.get("quantity", 1) for item
                     in cart_items)

    """print("Order Details:")"""
    for item in cart_items:
        print(f"- {item['name']}: ${item['price']} x {item['quantity']}")
    print(f"Total Cost: ${total_cost}")

    """if payment is successful"""
    payment_status = "Success"

    print("Sending Confirmation Emails:")
    print("User Email: ", order_data.get("user_email"))
    print("Store Owner Email: ", "store@example.com")

    """Return a response indicating that the order was successfully placed"""
    return jsonify({
        "message": "Order placed successfully",
        "total_cost": total_cost,
        "payment_status": payment_status
    }), 200
    return "Order placed successfully"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
