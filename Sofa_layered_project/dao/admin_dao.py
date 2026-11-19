from database.connection import Database
from model.admin import Admin


class Admin_dao:

    def display_all(self):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        query = "SELECT * FROM admin"

        cursor.execute(query)

        rows = cursor.fetchall()

        admins = []

        for row in rows:

            admin = Admin(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            admins.append(admin)

        cursor.close()
        connection.close()

        return admins