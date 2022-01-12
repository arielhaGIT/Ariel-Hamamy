from flask import Flask, redirect, url_for
from flask import render_template
from flask import request, jsonify
from flask import session
from interact_with_DB import interact_db
import requests
import random

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


@app.route('/db_users', defaults={'user_id': 1})
@app.route('/db_users/<int:user_id>')
def get_users_func(user_id):
    query = 'select * from users where user_id=%s;' % user_id
    users = interact_db(query=query, query_type='fetch')
    if len(users) == 0:
        return_dict = {
            'status': 'failed',
            'message': 'user not found'
        }
    else:
        return_dict = {
            'status': 'success',
            f'id': users[0].user_id,
            'name': users[0].name,
            'email': users[0].email,
        }
    return jsonify(return_dict)

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

@app.route('/req_fronthand')
def req_fronthand_func():
    return render_template('req_fronthand.html')

def get_pokemons(num):
    pokemons = []
    for i in range(num):
        random_num = random.randint(1, 100)
        res = requests.get(f'https://pokeapi.co/api/v2/pokemon/{random_num}')
        res = res.json()
        pokemons.append(res)
    return pokemons

@app.route('/req_backhand')
def req_backhand_func():
    num = 3;
    if "number" in request.args:
        num = int(request.args["number"])
    pokemons = get_pokemons(num)
    return render_template('req_backhand.html', pokemons=pokemons)



if __name__ == '__main__':
    app.run(debug=True)