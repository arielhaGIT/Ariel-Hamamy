from flask import Blueprint, render_template,session,request
from utilities.db.db_complains import dbComplains

# catalog blueprint definition
returns = Blueprint('returns', __name__, static_folder='static', static_url_path='/returns', template_folder='templates')


# Routes
@returns.route('/returns', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('returns.html')
    #post
    if 'logged_in' not in session:
        session['logged_in'] = False
    if  session['logged_in'] == False:
        return render_template('SignIn.html')

    subject = request.form['subject']
    orderNum = request.form['orderNum']
    file = request.form['file']
    problem = request.form['problem']
    username = session['user_data']['username']
    id = dbComplains.get_last_complain_id(username)
    dbComplains.insert(id+1,username,orderNum,subject,problem,file)

    return render_template('HomePage.html')