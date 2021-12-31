from flask import Blueprint, render_template, request, session
from utilities.db.db_users import DBusers

# catalog blueprint definition
UpdateDetails = Blueprint('UpdateDetails', __name__, static_folder='static', static_url_path='/UpdateDetails', template_folder='templates')


# Routes
@UpdateDetails.route('/UpdateDetails')
def index():
    return render_template('UpdateDetails.html')


@UpdateDetails.route('/update_user', methods=['POST'])
def update_user():
        username = session['username']
        if request.form['email']:
            email = request.form['email']
        else:
            email = DBusers.get_detail_by_username(username,email)
        password = request.form['password']
        phone = request.form['phone']

        if DBusers.update_user_profile(email, phone, password):
            session['userAlreadyExists'] = False
            session.pop('userAlreadyExists')
            return render_template('/SignIn.html')
        else:
            session['userAlreadyExists'] = True
            return render_template('/UpdateDetails.html')
