from flask import Blueprint, render_template, session, request
from utilities.db.db_products_in_cart import dbproduct_in_cart as DBP
from utilities.db.db_cart import dbcart
# catalog blueprint definition
cart = Blueprint('cart', __name__, static_folder='static', static_url_path='/cart', template_folder='templates')


# Routes
@cart.route('/cart')
def index():
    cart_id = dbcart.get_last_cart_id(session['user_data']['username'])
    products_in_cart = DBP.get_cart_details(session['user_data']['username'], cart_id)
    total_price = DBP.update_total(session['user_data']['username'], cart_id)
    return render_template('cart.html', products_in_cart=products_in_cart, total_price=total_price)

@cart.route('/minus', methods=['POST'])
def minus():
    cart_id = dbcart.get_last_cart_id(session['user_data']['username'])
    quantity = request.form['quantity']
    product_id = request.form['product_id']
    username = session['user_data']['username']
    if quantity == "1":
        DBP.delete_product_from_cart(product_id, cart_id, username)
    else:
        minus = "minus"
        DBP.update_product_quantity(product_id, cart_id, username, quantity, minus)
    products_in_cart = DBP.get_cart_details(session['user_data']['username'], cart_id)
    total_price = DBP.update_total(session['user_data']['username'], cart_id)
    return render_template('cart.html', products_in_cart=products_in_cart, total_price=total_price)

@cart.route('/plus', methods=['POST'])
def plus():
    quantity = request.form['quantity']
    product_id = request.form['product_id']
    cart_id = dbcart.get_last_cart_id(session['user_data']['username'])
    username = session['user_data']['username']
    plus = "plus"
    DBP.update_product_quantity(product_id, cart_id, username, quantity, plus)
    products_in_cart = DBP.get_cart_details(session['user_data']['username'], cart_id)
    total_price = DBP.update_total(session['user_data']['username'], cart_id)
    return render_template('cart.html', products_in_cart=products_in_cart, total_price=total_price)