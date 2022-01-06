from flask import Blueprint, render_template, session, request
from utilities.db.db_cart import dbcart
from utilities.db.db_products_in_cart import dbproduct_in_cart as DBP

# catalog blueprint definition
payment = Blueprint('payment', __name__, static_folder='static', static_url_path='/payment', template_folder='templates')


# Routes
@payment.route('/payment', methods=['GET', 'POST'])
def index():
    cart_id = dbcart.get_last_cart_id(session['user_data']['username'])

    if 'logged_in' not in session:
        return render_template('SignIn.html')
    if session['logged_in'] == True:
        if request.method == 'GET':
            total_price = DBP.update_total(session['user_data']['username'], session['user_data']['cart_id'])
            return render_template('payment.html',total_price=total_price)
        if request.method == 'POST':
            Delivery_Method = request.form['Delivery_Method']
            Address = request.form['address']
            if Delivery_Method == "new_Address" or Delivery_Method == "current_Address":
                status = dbcart.update_status(session['user_data']['username'], cart_id,"On the way")
            else:
                status = dbcart.update_status(session['user_data']['username'], cart_id, "Waiting for collection")
            if Delivery_Method == "new_Address":
                dbcart.update_address(session['user_data']['username'], cart_id,Address)
            elif Delivery_Method == "current_Address":
                print(session['user_data']['address'])

                dbcart.update_address(session['user_data']['username'], cart_id, session['user_data']['address'])
            total_price = DBP.update_total(session['user_data']['username'], session['user_data']['cart_id'])
            dbcart.update_total_cost(session['user_data']['username'], cart_id, total_price)
            next_cart = cart_id+1
            session['user_data']['cart_id']=next_cart
            dbcart.insert(session['user_data']['username'])

            return render_template('confirmationOrder.html', cart_id=cart_id)
