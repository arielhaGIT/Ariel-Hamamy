from flask import Blueprint, render_template,session,request
from utilities.db.db_users import dbusers
from utilities.db.db_cart import dbcart


# catalog blueprint definition
SignIn = Blueprint('SignIn', __name__, static_folder='static', static_url_path='/SignIn', template_folder='templates')


# Routes
@SignIn.route('/SignIn', methods=['GET', 'POST'])
def index():
    if 'logged_in' not in session:
        session['logged_in'] = False
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if dbusers.check_user_signIn(username, password):
            session['logged_in'] = True
            details = dbusers.get_all_details(username)
            dbcart.insert(username)
            cartid = dbcart.get_last_cart_id(username)
            session['user_data'] = {
                'username': username,
                'password': password,
                'phone': details[0].phone,
                'address': details[0].address,
                'birthdate': details[0].birthdate,
                'email': details[0].email,
                'firstname': details[0].firstName,
                'lastname': details[0].lastName,
                'cart_id': cartid
            }
            session['WrongDetails'] = False
            session.pop('WrongDetails')
            return render_template('homepage.html')
        else:
            session['WrongDetails'] = True
            return render_template('SignIn.html')

    if 'WrongDetails' in session:
        session.pop('WrongDetails')
    session['logged_in'] = False
    return render_template('SignIn.html')