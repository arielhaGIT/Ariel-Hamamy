from flask import Blueprint, render_template, session, request
from utilities.db.db_products import dbProducts
from utilities.db.db_products_in_cart import dbproduct_in_cart as DBP
from utilities.db.db_cart import dbcart

# import pyautogui



# shop blueprint definition
shop = Blueprint('shop', __name__, static_folder='static', static_url_path='/shop', template_folder='templates')


# Routes
@shop.route('/shop')
def index():
    products = dbProducts.get_products()
    print(products)
    return render_template('shop.html', products=products)

# add to cart
@shop.route('/add_to_cart', methods=['POST'])
def add_to_cart():
    # position = pyautogui.position()
    if session['logged_in'] == False or 'logged_in' not in session :
        return render_template('SignIn.html')
    else:
        productid = request.form['productId']
        productPrice = request.form['productPrice']
        productSale = request.form['productSale']
        cart_id = dbcart.get_last_cart_id(session['user_data']['username'])
        if DBP.get_product_from_product_cart(productid, session['user_data']['username'], cart_id):
            products = dbProducts.get_products()
            return render_template('shop.html', products=products)
        else:
                DBP.insert_product_to_product_cart(productid, cart_id, session['user_data']['username'])
        products = dbProducts.get_products()
        return render_template('shop.html', products=products)