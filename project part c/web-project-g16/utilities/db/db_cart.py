from interact_with_DB import interact_db

class DBcart:
    def insert(self, username):
        query = "insert into web_project_g16.carts(cart_id, username, time) \
                        values (null , '%s', CURRENT_TIMESTAMP);" % ( username )
        interact_db(query=query, query_type='commit')


    def get_last_cart_id(self,username):
        query = "SELECT *" \
                " FROM web_project_g16.carts " \
                "where username = '%s';" % (username)
        answer = interact_db(query=query, query_type='fetch')
        return len(answer)

    def get_orders_of_user(self,username):
        query = "SELECT * FROM web_project_g16.carts where username = '%s' and status != 'in process';" % username
        answer = interact_db(query=query, query_type='fetch')
        return answer

    def update_total_cost(self,username, cart_id,total_cost):
        query = "UPDATE web_project_g16.carts SET total_cost='%s' where username = '%s' and cart_id = '%s';" % (total_cost, username, cart_id)
        answer = interact_db(query=query, query_type='commit')


    def get_total_cost(self,username,cart_id):
        query = "SELECT total_cost FROM web_project_g16.carts where username = '%s' and cart_id = '%s';" % (username,cart_id)
        answer = interact_db(query=query, query_type='fetchone')
        return answer[0]

    def update_address(self,username,cart_id,address):
        query = "UPDATE web_project_g16.carts SET address='%s' where username = '%s' and cart_id = '%s';" % (address,username,cart_id)
        answer = interact_db(query=query, query_type='commit')

    def update_status(self,username,cart_id,Delivery_Method):
        query = "UPDATE web_project_g16.carts SET status='%s' where username = '%s' and cart_id = '%s';" % (Delivery_Method,username,cart_id)
        answer = interact_db(query=query, query_type='commit')

# Creates an instance for the DBproducts class for export.
dbcart = DBcart()