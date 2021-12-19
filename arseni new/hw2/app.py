from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session

app = Flask(__name__)
app.secret_key = '123'

users = {'user1': { 'Name': 'Yossi', 'Last name': 'cohen', 'Email': 'yossi@gmail.com'},
         'user2': { 'Name': 'Yotam', 'Last name': 'Hen', 'Email': 'yotem@gmail.com'},
         'user3': {'Name': 'Ariel', 'Last name': 'Hamamy', 'Email': 'ariel@gmail.com'},
         'user4': {'Name': 'Gal', 'Last name': 'Baron', 'Email': 'gal@gmail.com'},
         'user5': {'Name': 'Matan', 'Last name': 'Ron', 'Email': 'matan@gmail.com'},
        }

@app.route('/')
def home_func():  # put application's code here
    return render_template('cv.html', name='ariel')

@app.route('/assignment9', methods=['GET', 'POST'])
def login_func():  # put application's code here
    if request.method == 'GET':
        if 'search_user' in request.args:
            search_user = request.args['search_user']
            return render_template('assignment9.html', username=session['username']
                                                     , search_user=search_user
                                                     , users=users)
        return render_template('assignment9.html', username=session['username'])
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


if __name__ == '__main__':
    app.run(debug=True)