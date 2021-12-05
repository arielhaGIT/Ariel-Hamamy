from flask import Flask,redirect,url_for

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/about', methods=['GET', 'POST'])
def about_func():
    #TODO
    #do something with DB
    return redirect(url_for('catalog_func'))


@app.route('/catalog')
def catalog_func():
    return 'Welcome to catalog page'

@app.route('/US')
def US_func():  # put application's code here
    #TODO
    #DO SOMTHING WITH DB
    return redirect('/catalog')

if __name__ == '__main__':
    app.run(debug=True)


