from flask import Blueprint, render_template, session, redirect, url_for
from utilities.db.db_users import DBusers

# catalog blueprint definition
profile = Blueprint('profile', __name__, static_folder='static', static_url_path='/profile', template_folder='templates')


# Routes
@profile.route('/profile')
def index():
    if 'logged_in' not in session:
        return render_template('SignIn.html')
    if session['logged_in']:
        return render_template('profile.html')
    else:
        return render_template('SignIn.html')

@profile.route('/deleteUser')
def deleteUser():
    username = session['user_data']['username']
    if DBusers.delete_user_profile(username):
        if session['logged_in']:
            session['logged_in'] = False
            session.pop('user_data')
            return redirect(url_for('homepage.index'))
        return redirect(url_for('homepage.index'))