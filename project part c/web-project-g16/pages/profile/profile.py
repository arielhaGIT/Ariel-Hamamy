from flask import Blueprint, render_template, session, redirect, url_for
from utilities.db.db_users import dbusers
from utilities.db.db_cart import dbcart


# catalog blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', static_url_path='/profile', template_folder='templates')


# Routes
@profile.route('/profile')
def index():
    if 'logged_in' not in session:
        return render_template('SignIn.html')
    if session['logged_in']:
        username = session['user_data']['username']
        address = 'address'
        email = 'email'
        phone = 'phone'
        birthdate = 'birthdate'
        BDaddress = dbusers.get_detail_by_username(username, address)
        DBemail = dbusers.get_detail_by_username(username, email)
        DBphone = dbusers.get_detail_by_username(username, phone)
        DBbirthdate = dbusers.get_detail_by_username(username, birthdate)
        orders = dbcart.get_orders_of_user(username)
        return render_template('profile.html', address=BDaddress, email=DBemail, phone=DBphone, birthdate=DBbirthdate, orders= orders)
    else:
        return render_template('SignIn.html')

@profile.route('/deleteUser')
def deleteUser():
    username = session['user_data']['username']
    if dbusers.delete_user_profile(username):
        if session['logged_in']:
            session['logged_in'] = False
            session.pop('user_data')
            return redirect(url_for('homepage.index'))
        return redirect(url_for('homepage.index'))


