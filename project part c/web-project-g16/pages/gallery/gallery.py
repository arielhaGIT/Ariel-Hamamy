from flask import Blueprint, render_template

# catalog blueprint definition
gallery = Blueprint('gallery', __name__, static_folder='static', static_url_path='/gallery', template_folder='templates')


# Routes
@gallery.route('/gallery')
def index():
    return render_template('gallery.html')
