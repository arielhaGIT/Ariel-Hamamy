from interact_with_DB import interact_db

class DBproduct_in_cart:
    def insert_product_to_product_cart(self, product_id, cart_id, username):
            query = "insert into web_project_g16.products_in_cart(cart_id,username ,product_id, quantity) \
                            values ('%s', '%s','%s','%s');" % (cart_id,username, product_id, 1)
            interact_db(query=query, query_type='commit')
            # message
            return True

    def get_product_from_product_cart(self, productid, username, cart_id):
        query = "SELECT product_id  FROM web_project_g16.products_in_cart where username = '%s' and cart_id='%s' and product_id='%s';" % (username, cart_id, productid)
        answer = interact_db(query=query, query_type='fetch')
        return len(answer)



    def get_cart_details(self, username, cart_id):
        get_products = "SELECT pp.product_id, pp.link,pp.name,pp.price,pp.sale,pp.sale_price,pic.quantity, pp.price*pic.quantity as totalPRICE,  pp.sale_price*pic.quantity as totalSALE   FROM web_project_g16.products_in_cart as pic left join web_project_g16.products as pp on pic.product_id=pp.product_id where pic.product_id=pp.product_id and username = '%s' and cart_id='%s';" % (username, cart_id)
        answer = interact_db(query=get_products, query_type='fetch')
        print(answer)
        return answer

    def update_product_quantity(self, product_id, cart_id, username, quantity, action):
        if action == "minus":
            query = "UPDATE web_project_g16.products_in_cart set quantity='%s'-1 WHERE username='%s' and cart_id='%s' and product_id='%s';" % (quantity, username, cart_id, product_id)
        if action == "plus":
            query = "UPDATE web_project_g16.products_in_cart set quantity='%s'+1 WHERE username='%s' and cart_id='%s' and product_id='%s';" % (quantity, username, cart_id, product_id)
        interact_db(query=query, query_type='commit')
        # message
        return True

    def delete_product_from_cart(self, product_id, cart_id, username):
        query = "delete from web_project_g16.products_in_cart where username = '%s' and cart_id='%s' and product_id='%s';" % (username, cart_id, product_id)
        interact_db(query=query, query_type='commit')
        return True


    def update_total(self, username, cart_id):
        get_products = "SELECT pp.product_id, pp.link,pp.name,pp.price,pp.sale,pp.sale_price,pic.quantity, pp.price*pic.quantity as totalPRICE,  pp.sale_price*pic.quantity as totalSALE   FROM web_project_g16.products_in_cart as pic left join web_project_g16.products as pp on pic.product_id=pp.product_id where pic.product_id=pp.product_id and username = '%s' and cart_id='%s';" % (username, cart_id)
        answer = interact_db(query=get_products, query_type='fetch')
        total_price = 0
        for prod in answer:
            if prod.totalSALE:
                total_price = total_price + prod.totalSALE
            else:
                total_price = total_price + prod.totalPRICE
        return total_price
# Creates an instance for the DBproducts class for export.
dbproduct_in_cart = DBproduct_in_cart()