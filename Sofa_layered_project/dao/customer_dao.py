from database.connection import Database
from model.customer import Customer


class Customer_dao:

    def register_customer(self, customer):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO customer
        (name, phone, email, password_hash, address, city)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        data = (
            customer.name,
            customer.phone,
            customer.email,
            customer.password_hash,
            customer.address,
            customer.city
        )

        cursor.execute(query, data)
        conn.commit()

        cursor.close()
        conn.close()

    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from customer'

        cursor.execute(query)

        rows = cursor.fetchall()

        customers = []

        for row in rows:

            customer = Customer(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )

            customers.append(customer)

        cursor.close()
        conn.close()

        return customers


    def display_by_id(self, id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from customer where customer_id = %s'

        cursor.execute(query, (id,))

        row = cursor.fetchone()

        if row is None:
            cursor.close()
            conn.close()
            return None

        customer = Customer(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7]
        )

        cursor.close()
        conn.close()

        return customer


    def get_customer_by_email(self, email):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from customer where email = %s'

        cursor.execute(query, (email,))

        row = cursor.fetchone()

        if row is None:
            cursor.close()
            conn.close()
            return None

        customer = Customer(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7]
        )

        cursor.close()
        conn.close()

        return customer


    def update_customer(self, id, new_phone):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'update customer set phone=%s where customer_id=%s'

        data = (new_phone, id)

        cursor.execute(query, data)

        conn.commit()

        print("customer data updated successfully")

        cursor.close()
        conn.close()


    def delete_customer(self, id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'delete from customer where customer_id = %s'

        cursor.execute(query, (id,))

        conn.commit()

        print("deleted successfully")

        cursor.close()
        conn.close()


    def search_by_name(self, name):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from customer where name like %s'

        cursor.execute(query, ('%' + name + '%',))

        rows = cursor.fetchall()

        customers = []

        for row in rows:

            customer = Customer(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )

            customers.append(customer)

        cursor.close()
        conn.close()

        return customers


    def search_by_phone(self, phone):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from customer where phone = %s'

        cursor.execute(query, (phone,))

        row = cursor.fetchone()

        if row is None:
            cursor.close()
            conn.close()
            return None

        customer = Customer(row[0],row[1],row[2],row[3],row[4],row[5],row[6],row[7])

        cursor.close()
        conn.close()

        return customer