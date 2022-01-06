from flask import Blueprint, render_template, redirect, url_for ,session

# homepage blueprint definition
confirmationOrder = Blueprint('confirmationOrder', __name__, static_folder='static', static_url_path='/confirmationOrder', template_folder='templates')


# # Routes
# @confirmationOrder.route('/confirmationOrder')
# def index():
#
#     return render_template('confirmationOrder.html' )
