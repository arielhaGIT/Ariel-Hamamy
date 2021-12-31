from flask import Blueprint, render_template

# catalog blueprint definition
returns = Blueprint('returns', __name__, static_folder='static', static_url_path='/returns', template_folder='templates')


# Routes
@returns.route('/returns')
def index():
    return render_template('returns.html')
