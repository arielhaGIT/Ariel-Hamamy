from flask import request, redirect
from interact_with_DB import interact_db
from settings import DB
import mysql.connector

class DBusers:
    # __connection = None
    # __cursor = None
    #
    # def __init__(self):
    #     pass

    def insert_User_DB(username, email, password, firstname, lastname, phone):
        check_input = "SELECT username FROM web_project_g16.users WHERE username='%s';" % username
        answer = interact_db(query=check_input, query_type='fetch')
        if len(answer) == 0:
            query = "insert into web_project_g16.users (username, password, email, firstname, lastname, phone)\
                            value ('%s', '%s', '%s', '%s', '%s', '%s');" % (username, password, email, firstname, lastname, phone)
            interact_db(query=query, query_type='commit')
            # message
            return True
        else:
            # message
            # flash('this user name is already registered')
            return False

    def check_user_signIn(username, password):
        check_username = "SELECT username FROM web_project_g16.users WHERE username='%s';" % username
        answer = interact_db(query=check_username, query_type='fetch')
        if len(answer) == 0:
            return False

        else:
            get_password = "SELECT password FROM web_project_g16.users WHERE username='%s';" % username
            answer = interact_db(query=get_password, query_type='fetchone')
            print(answer[0])
            if answer[0] == password:
                return True
            else:
                return False

    def update_user_profile(email, phone, password):
        check_username = "SELECT username FROM web_project_g16.users WHERE username='%s';" % username
        answer = interact_db(query=check_username, query_type='fetch')
        if len(answer) == 0:
            return False
        return True

    def delete_user_profile(username):
        query = "delete from web_project_g16.users WHERE username='%s';" % username
        interact_db(query=query, query_type='commit')
        return True

    def get_detail_by_username(username, detail):
        if detail == 'address':
            get_address = "SELECT address FROM web_project_g16.users WHERE username='%s';" % username
            answer = interact_db(query=get_address, query_type='fetchone')

        elif detail == 'phone':
            get_address = "SELECT phone FROM web_project_g16.users WHERE username='%s';" % username
            answer = interact_db(query=get_address, query_type='fetchone')

        elif detail == 'email':
            get_address = "SELECT email FROM web_project_g16.users WHERE username='%s';" % username
            answer = interact_db(query=get_address, query_type='fetchone')

        elif detail == 'password':
            get_address = "SELECT password FROM web_project_g16.users WHERE username='%s';" % username
            answer = interact_db(query=get_address, query_type='fetchone')

        return answer[0]