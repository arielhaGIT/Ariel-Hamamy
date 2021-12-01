from flask import Blueprint, render_template, redirect, url_for, request, flash
import mysql.connector

ass10 = Blueprint('ass10', __name__,
                  static_folder='static',
                  static_url_path='/pages/ass10',
                  template_folder='templates')


def interact_db(query, query_type: str):
    return_value = False
    connection = mysql.connector.connect(host='localhost',
                                         user='root',
                                         password='root',
                                         database='assignment10')
    cursor = connection.cursor(named_tuple=True)
    cursor.execute(query)

    if query_type == 'commit':
        connection.commit()
        return_value = True

    if query_type == 'fetch':
        query_result = cursor.fetchall()
        return_value = query_result


    connection.close()
    cursor.close()
    return return_value


lastChange = "none"

@ass10.route('/ass10', methods=['GET', 'POST'])
def assignment10():
    last = lastChange
    query = "select *  from users10"
    query_result = interact_db(query=query, query_type='fetch')
    return render_template('ass10.html', users10=query_result, req_method=request.method, lastChange=last)


@ass10.route('/delete', methods=['POST'])
def delete_user():

    if request.method == 'POST':
        email = request.form['email']
        query = "DELETE FROM users10 WHERE email = '%s';" % email
        interact_db(query=query, query_type='commit')
        flash('Last change was : Delete')

    return redirect('/ass10')


@ass10.route('/insert', methods=['POST'])
def insert_user():
    if request.method == 'POST':

        email = request.form['email']
        firstName = request.form['firstName']
        lastName = request.form['lastName']
        role = request.form['role']
        query = "INSERT INTO users10(email, firstName, lastName, role) VALUES ('%s', '%s', '%s', '%s')" % (
        email, firstName, lastName, role)
        interact_db(query=query, query_type='commit')
    flash('Last change was : Insert')

    return redirect('/ass10')


@ass10.route('/update', methods=['POST'])
def update_users():
    email = request.form['email']
    firstName = request.form['firstName']
    lastName = request.form['lastName']
    role = request.form['role']
    query = "SELECT firstName FROM users10 WHERE email='%s';" % email
    query_result = interact_db(query=query, query_type='fetch')
    if len(query_result) > 0:
        query = "UPDATE users10 SET firstName='%s', lastName='%s', role='%s' WHERE email='%s';" % \
                (firstName, lastName, role, email)
        interact_db(query=query, query_type='commit')
        flash('Last change was : Update')

        return redirect('/ass10')
    else:
        return redirect('/ass10')
