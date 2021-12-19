from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World! my name is Ariel'

@app.route('/about', methods=['GET', 'POST'])
def about_func():
    #TODO
    #do something with DB
    return redirect(url_for('profile_func'))


@app.route('/profile')
def profile_func():
    return 'Welcome to profile page'

@app.route('/cart')
def cart_func():  # put application's code here
    #TODO
    #DO SOMTHING WITH DB
    return redirect('/profile')

if __name__ == '__main__':
    app.run(debug=True)