from flask import Blueprint, render_template, redirect, url_for, request, flash
import mysql.connector
from flask import jsonify, json, Response

users = Blueprint('ass11', __name__,
                  static_folder='static',
                  static_url_path='/pages/ass11/users',
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


@users.route('/ass11/users', methods=['GET'])
def find():
    if request.method == 'GET':
        query = "select * from users10"
        query_result = interact_db(query=query, query_type='fetch')
        response = jsonify(query_result)
    return response


@users.route('/ass11/users/selected', defaults={'ID': 2})
@users.route('/ass11/users/selected/<int:ID>')
def select_user(ID):
    query = "select * FROM users10"
    query_result = interact_db(query=query, query_type='fetch')
    user_exist = ID in range(1, len(query_result)+1)
    if user_exist:
        query = "select * FROM users10 WHERE ID = '%s';" % ID
        query_result = interact_db(query=query, query_type='fetch')
        response = jsonify(query_result)
        return response
    else:
        return jsonify({'request status =': 'False',
                        'user data': 'doesnt exist'})

