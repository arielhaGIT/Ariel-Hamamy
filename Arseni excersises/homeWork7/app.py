from flask import Flask ,redirect,url_for

app = Flask(_name_)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('cart')
def cart_func():  # put application's code here
    #TODO
    #DO SOMTHING WITH DB
    return redirect('/catalog')


@app.route('/about' ,methods=['GET','POST'])
def about_func():  # put application's code here
    #TODO
    #DO SOMTHING WITH DB
    return redirect(url_for('catalog_func'))

@app.route('/catalog')
def catalog_func():  # put application's code here
    return 'catalog page!'

if _name_ == '_main_':
    app.run(debug=True)