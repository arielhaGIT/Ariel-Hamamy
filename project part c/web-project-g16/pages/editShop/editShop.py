from flask import Blueprint, render_template, session, redirect,url_for,request
from utilities.db.db_products import dbProducts
# editShop blueprint definition
editShop = Blueprint('editShop', __name__, static_folder='static', static_url_path='/editShop', template_folder='templates')


# Routes
@editShop.route('/editShop')
def index():
    if 'user_data' in session and session['user_data']['username'] == 'Shop Admin':
        products = dbProducts.get_products()
        if 'message' in session:
            message = session['message']
            session.pop('message')
            return render_template('editShop.html', products=products, message = message)
        return render_template('editShop.html', products=products)
    else:
        return redirect(url_for('shop.index'))

@editShop.route('/editShop_delete', methods = ['POST','GET'])
def deleteProduct():
    if 'user_data' in session and session['user_data']['username'] == 'Shop Admin':
        session['message'] = 'The product successfully deleted!'
        product_id = request.form['product']
        dbProducts.delete_product(product_id)
        return redirect(url_for('editShop.index'))
    else:
        return redirect(url_for('shop.index'))
