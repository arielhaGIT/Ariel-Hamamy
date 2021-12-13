from flask import Flask, redirect, url_for
from flask import render_template
app = Flask(__name__)

@app.route('/')
def home_func():  # put application's code here
    return render_template('CV.html', name='ariel')

@app.route('/assignment8', methods=['GET', 'POST'])
def about_func():  # put application's code here
    name = 'Ariel'
    second_name = 'Hamamy'
    uni = 'BGU'
    return render_template('assignment8.html',
                           profile={'name': 'Ariel', 'second_name' : 'Hamamy'},
                           name=name,
                           university=uni,
                           second_name=second_name,
                           degreas=['BSc', 'MSc', 'GrandMaster'],
                           hobies=('art', 'music', 'sql'))


if __name__ == '__main__':
    app.run(debug=True)