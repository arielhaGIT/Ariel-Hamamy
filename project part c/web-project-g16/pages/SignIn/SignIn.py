from flask import Blueprint, render_template,session,request
from utilities.db.db_users import DBusers


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

        if DBusers.check_user_signIn(username, password):
            session['logged_in'] = True
            session['user_data'] = {
                'username': username,
                'password': password
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
