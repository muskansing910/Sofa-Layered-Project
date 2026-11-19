from database.connection import Database
from model.inquiry import Inquiry


class Inquiry_dao:

    def add_inquiry(self, inquiry):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        
        query = """
INSERT INTO inquiry
(inquiry_id, customer_id, custom_sofa_id, admin_id,
 status, customer_message, admin_notes)
VALUES (%s, %s, %s, %s, %s, %s, %s)
"""
        

        data = (
    inquiry.inquiry_id,
    inquiry.customer_id,
    inquiry.custom_sofa_id,
    inquiry.admin_id,
    inquiry.status,
    inquiry.customer_message,
    inquiry.admin_notes
)

        cursor.execute(query, data)

        connection.commit()

        cursor.close()
        connection.close()


    def display_all(self):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        query = "SELECT * FROM inquiry"

        cursor.execute(query)

        rows = cursor.fetchall()

        inquiries = []

        for row in rows:

            inquiry = Inquiry(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8]
            )

            inquiries.append(inquiry)

        cursor.close()
        connection.close()

        return inquiries

    def display_by_customer_id(self, customer_id):
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = "SELECT * FROM inquiry WHERE customer_id = %s"

        cursor.execute(query, (customer_id,))

        rows = cursor.fetchall()

        inquiries = []

        for row in rows:
            inquiry = Inquiry(
                row[0], row[1], row[2], row[3], row[4],
                row[5], row[6], row[7], row[8]
            )
            inquiries.append(inquiry)

        cursor.close()
        connection.close()

        return inquiries

    def get_next_id(self):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        query = "SELECT MAX(inquiry_id) FROM inquiry"

        cursor.execute(query)

        row = cursor.fetchone()

        cursor.close()
        connection.close()

        if row[0] is None:
            return 1

        return row[0] + 1