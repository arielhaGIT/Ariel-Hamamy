from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session, jsonify
from interact_with_DB import interact_db
import json
import requests

app = Flask(__name__)
app.secret_key = '123'
app.config.from_pyfile('settings.py')


users = {'user1': { 'Name': 'Yossi', 'Last name': 'cohen', 'Email': 'yossi@gmail.com'},
         'user2': { 'Name': 'Yotam', 'Last name': 'Hen', 'Email': 'yotem@gmail.com'},
         'user3': {'Name': 'Ariel', 'Last name': 'Hamamy', 'Email': 'ariel@gmail.com'},
         'user4': {'Name': 'Gal', 'Last name': 'Baron', 'Email': 'gal@gmail.com'},
         'user5': {'Name': 'Matan', 'Last name': 'Ron', 'Email': 'matan@gmail.com'}}

@app.route('/')
def home_func():  # put application's code here
    return render_template('cv.html', name='ariel')

@app.route('/assignment8', methods=['GET', 'POST'])
def about_func():  # put application's code here
    name = 'Ariel'
    second_name = 'Hamamy'
    uni = 'BGU'
    return render_template('assignment8.html',
                           profile={'name': 'Ariel', 'second_name': 'Hamamy'},
                           name=name,
                           university=uni,
                           second_name=second_name,
                           degreas=['BSc', 'MSc', 'GrandMaster'],
                           hobies=('art', 'music', 'sql'))

@app.route('/assignment9', methods=['GET', 'POST'])
def login_func():  # put application's code here
    if request.method == 'GET':
        if 'username' in session:
            if 'search_user' in request.args:
                search_user = request.args['search_user']
                return render_template('assignment9.html', username=session['username']
                                       , search_user=search_user
                                       , users=users)
            return render_template('assignment9.html', users=users, username=session['username'])
        return render_template('assignment9.html', users=users)
    if request.method == 'POST':
        #DB
        username = request.form['username']
        Password = request.form['password']
        found = True
        if found:
            session['username'] = username
            session['user_login'] = True
            return render_template('assignment9.html', username=username, users=users)
        else:
            return render_template('assignment9.html')

@app.route('/logout')
def logout_func():  # put application's code here
    session['username'] = ''
    return render_template('CV.html')


###### Pages
## assignment10
from pages.assignment10.assignment10 import assignment10
app.register_blueprint(assignment10)

@app.route('/assignment11')
def assignment11_func():  # put application's code here
    return render_template('assignment11.html', non="non")

def get_users(num):
    res = requests.get(f'https://reqres.in/api/users/{num}')
    res = res.json()
    return res

@app.route('/assignment11/users')
def DB_to_json_func():  # put application's code here
    return_dict = {}
    query = "SELECT * FROM webhw.users ;"
    answer = interact_db(query=query, query_type='fetch')
    for user in answer:
        return_dict[f'user_{user.id}'] = {
            'id': user.id,
            'name': user.name,
            'email': user.email,
            'password': user.password
        }
    return render_template('assignment11.html', answer=return_dict, non="non")

@app.route('/assignment11/outer_source',  methods=['post'])
def outer_source_func():
    if "frontend" in request.form:
        num = int(request.form['frontend'])
        return render_template('assignment11.html', frontend=num)
    elif "backend" in request.form:
        num = int(request.form["backend"])
        user = get_users(num)
        return render_template('assignment11.html', backend=user)
    else:
        return render_template('assignment11.html')

@app.route('/assignment12/restapi_users', defaults={'id': 1})
@app.route('/assignment12/restapi_users/<int:id>')
def get_users_func(id):
    query = 'select * from users where id=%s;' % id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        return_dict = {
            'status': 'failed',
            'message': 'user not found'
        }
    else:
        return_dict = {
            'status': 'success',
            f'id': users[0].id,
            'name': users[0].name,
            'email': users[0].email,
        }
    return jsonify(return_dict)


if __name__ == '__main__':
    app.run(debug=True)