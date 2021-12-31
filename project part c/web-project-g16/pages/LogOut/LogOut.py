from flask import Blueprint, render_template,session,redirect,url_for

# catalog blueprint definition
LogOut = Blueprint('LogOut', __name__, static_folder='static', static_url_path='/LogOut', template_folder='templates')


@LogOut.route('/LogOut')
def index():
    if session['logged_in']:
        session['logged_in'] = False
        session.pop('user_data')
        return redirect(url_for('SignIn.index'))
    return redirect(url_for('SignIn.index'))

