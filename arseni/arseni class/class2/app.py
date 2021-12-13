from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    found = True
    if found:
        return render_template('Page1.html', name='Áriel')
    else:
        return render_template('Page1.html')


@app.route('/about')
def about_func():  # put application's code here
    name = 'ariel'
    second_name = 'hamamy'
    uni = 'BGU'
    return render_template('About.html',
                           Profile={'name': 'ariel', 'second_name': 'hamamy'},
                           university='BGU',
                           degrees=['BSc', 'MSc'],
                           hobbies=('music', 'sql', 'flask'))
#name=name, university=uni, second_name=second_name


@app.route('/catalog')
def catalog_func():  # put application's code here
    return 'catalog page!'


if __name__ == '__main__':
    app.run(debug=True)