from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.db.db_users import dbusers

# catalog blueprint definition
UpdateDetails = Blueprint('UpdateDetails', __name__, static_folder='static', static_url_path='/UpdateDetails', template_folder='templates')


# Routes
@UpdateDetails.route('/UpdateDetails')
def index():
    return render_template('UpdateDetails.html')


@UpdateDetails.route('/update_user', methods=['POST'])
def update_user():
        username = session['user_data']['username']

        if request.form['email']:
            email = request.form['email']
            dbusers.update_user_email(username, email)
        elif request.form['password']:
            password = request.form['password']
            dbusers.update_user_password(username, password)
        elif request.form['phone']:
            phone = request.form['phone']
            print("XXXXXX")
            dbusers.update_user_phone(username, phone)
        return redirect(url_for('profile.index'))