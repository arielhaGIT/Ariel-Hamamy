from flask import Blueprint, render_template ,session, request, redirect, url_for
from utilities.db.db_products import dbProducts


# new_product blueprint definition
new_product = Blueprint('new_product', __name__, static_folder='static', static_url_path='/new_product', template_folder='templates')


# Routes
@new_product.route('/new_product')
def index():
    if 'user_data' in session and session['user_data']['username'] == 'Shop Admin':
        if 'message' in session:
            message = session['message']
            session.pop('message')
            return render_template('new_product.html', message=message)
        return render_template('new_product.html')
    else:
        return redirect(url_for('shop.index'))

@new_product.route('/new_product_insert', methods=['POST'])
def insert_user():
    if 'user_data' in session and session['user_data']['username'] == 'Shop Admin':
        name = request.form['name']
        price = int(request.form['price'])
        sale_price = request.form['sale_price']
        color = request.form['color']
        photo = request.form['photo']
        if sale_price == "":
            sale_price = 0
        else:
            sale_price = int(sale_price)

        if dbProducts.insert_product(name, price, sale_price, color, photo):
            session['message'] = 'The product successfully added!'
            return redirect(url_for('new_product.index'))
        else:
            session['message'] = 'The product name is already exist!'
            return redirect(url_for('new_product.index'))
    else:
        return redirect(url_for('shop.index'))

