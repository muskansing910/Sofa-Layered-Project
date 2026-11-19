from dao.customer_dao import Customer_dao
import bcrypt

class customer_service:

    def register_customer(self, customer, password):

        password_hash = bcrypt.hashpw(
            password.encode('utf-8'),
            bcrypt.gensalt()
        ).decode('utf-8')

        customer.password_hash = password_hash

        dao = Customer_dao()

        dao.register_customer(customer)

    def login_customer(self, email, password):

        dao = Customer_dao()

        customer = dao.get_customer_by_email(email)

        if customer is None:
            return None

        if bcrypt.checkpw(
            password.encode('utf-8'),
            customer.password_hash.encode('utf-8')
        ):
            return customer

        return None

    def Display_customers(self):

        dao = Customer_dao()

        customers = dao.display_all()

        return customers


    def search_customer_by_id(self, id):

        dao = Customer_dao()

        customer = dao.display_by_id(id)

        return customer


    def search_customer_by_email(self, email):

        dao = Customer_dao()

        customer = dao.get_customer_by_email(email)

        return customer


    def update_customer(self, id, new_phone):

        dao = Customer_dao()

        dao.update_customer(id, new_phone)


    def delete_customer(self, id):

        dao = Customer_dao()

        dao.delete_customer(id)


    def search_by_name(self, name):

        dao = Customer_dao()

        customers = dao.search_by_name(name)

        return customers


    def search_by_phone(self, phone):

        dao = Customer_dao()

        customer = dao.search_by_phone(phone)

        return customer