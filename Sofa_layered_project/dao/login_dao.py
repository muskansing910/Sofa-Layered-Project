import bcrypt
from database.connection import Database


class LoginDAO:

    def login_customer(self, email, password):

        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        SELECT customer_id, name, password_hash
        FROM customer
        WHERE email = %s
        """

        cursor.execute(query, (email,))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        if result is None:
            return None

        customer_id = result[0]
        name = result[1]
        password_hash = result[2]

        if password_hash is None:
            return None

        if bcrypt.checkpw(
            password.encode("utf-8"),
            password_hash.encode("utf-8")
        ):
            return (customer_id, name)

        return None


    def login_admin(self, email, password):

        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        SELECT admin_id, name
        FROM admin
        WHERE email = %s AND password = %s
        """

        cursor.execute(query, (email, password))

        result = cursor.fetchone()

        cursor.close()
        connection.close()

        return result