from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session
from interact_with_DB import interact_db

app = Flask(__name__)
app.secret_key = '123'


@app.route('/')
def home_func():  # put application's code here
    return render_template('home.html', name='ariel')

@app.route('/login', methods=['GET', 'POST'])
def login_func():  # put application's code here
    if request.method == 'GET':
        return render_template('login.html')
    if request.method == 'POST':
        #DB
        username = request.form['username']
        Password = request.form['password']
        found = True
        if found:
            session['username'] = username
            session['user_login'] = True
            return redirect(url_for('home_func'))
        else:
            return render_template('login.html')

@app.route('/logout')
def logout_func():  # put application's code here
    session['username'] = ''
    return render_template('home.html')

@app.route('/catalog')
def catalog_func():
    if session['user_inside']:
        print('user_inside')
    if 'product' in request.args:
        product = request.args['product']
        size = request.args['size']
        return render_template('catalog.html', p_name=product, p_size=size)
    return render_template('catalog.html')

@app.route('/assignment8', methods=['GET', 'POST'])
def about_func():  # put application's code here
    name = 'Ariel'
    second_name = 'Hamamy'
    uni = 'BGU'
    return render_template('class.html',
                           profile={'name': 'Ariel', 'second_name' : 'Hamamy'},
                           name=name,
                           university=uni,
                           second_name=second_name,
                           degreas=['BSc', 'MSc', 'GrandMaster'],
                           hobies=('art', 'music', 'sql'))

@app.route('/users')
def users_func():
    query = 'select * from users;'
    users = interact_db(query=query, query_type='fetch')
    return render_template('users.html', users=users)


@app.route('/insert_user', methods=['post'])  # get the record that was inserted into the form
def insertUsers():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']

        check_input = "SELECT name FROM web.users WHERE name='%s';" % name
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into web.users (name, email , password)\
                            value ('%s', '%s', '%s');" % (name, email, password)
            interact_db(query=query, query_type='commit')
            # message
            return redirect('/users')
        else:
            # message
            return redirect('/users')
    return render_template('users.html', req_method=request.method)


@app.route('/delete_user', methods=['post'])
def delete_user_func():
    user_id = request.form['id']
    query = "delete from users where id='%s';" % user_id
    interact_db(query=query, query_type='commit')
    return redirect('/users')

if __name__ == '__main__':
    app.run(debug=True)