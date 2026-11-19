from database.connection import Database
from model.feedback import Feedback


class FeedbackDAO:

    def add_feedback(self, feedback):
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        INSERT INTO feedback
        (feedback_id, work_order_id, rating, comment)
        VALUES (%s, %s, %s, %s)
        """

        data = (
            feedback.feedback_id,
            feedback.work_order_id,
            feedback.rating,
            feedback.comment
        )

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

        print("Feedback added successfully.")

    def display_all(self):
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = "SELECT * FROM feedback"

        cursor.execute(query)
        rows = cursor.fetchall()

        feedbacks = []

        for row in rows:
            feedback = Feedback(
                row[0],
                row[1],
                row[2],
                row[3]
            )

            feedbacks.append(feedback)

        cursor.close()
        connection.close()

        return feedbacks

    def display_by_customer_id(self, customer_id):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        query = """
        SELECT f.*
        FROM feedback f
        JOIN work_order wo
        ON f.work_order_id = wo.work_order_id
        JOIN inquiry i
        ON wo.inquiry_id = i.inquiry_id
        WHERE i.customer_id = %s
        """

        cursor.execute(query, (customer_id,))

        rows = cursor.fetchall()

        feedbacks = []

        for row in rows:

            feedback = Feedback(
                row[0],
                row[1],
                row[2],
                row[3]
            )

            feedbacks.append(feedback)

        cursor.close()
        connection.close()

        return feedbacks

    def update_feedback(self, feedback_id, rating, comment):
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        UPDATE feedback
        SET rating = %s,
            comment = %s
        WHERE feedback_id = %s
        """

        data = (rating, comment, feedback_id)

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

        print("Feedback updated successfully.")

    def delete_feedback(self, feedback_id):
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        DELETE FROM feedback
        WHERE feedback_id = %s
        """

        data = (feedback_id,)

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

        print("Feedback deleted successfully.")