from flask import Flask, redirect, url_for
from flask import render_template
from flask import request
from flask import session

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


if __name__ == '__main__':
    app.run(debug=True)