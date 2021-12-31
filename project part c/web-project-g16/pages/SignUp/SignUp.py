from flask import Blueprint, render_template, request, session
from utilities.db.db_users import DBusers

# catalog blueprint definition
SignUp = Blueprint('SignUp', __name__, static_folder='static', static_url_path='/SignUp', template_folder='templates')


# Routes
@SignUp.route('/SignUp')
def index():
    return render_template('SignUp.html')


@SignUp.route('/insert_user', methods=['POST'])
def insert_user():
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']
        firstname = request.form['firstname']
        lastname = request.form['lastname']
        phone = request.form['phone']

        if DBusers.insert_User_DB(username, email, password, firstname, lastname, phone):
            session['userAlreadyExists'] = False
            session.pop('userAlreadyExists')
            return render_template('/SignIn.html')
        else:
            session['userAlreadyExists'] = True
            return render_template('/SignUp.html')








