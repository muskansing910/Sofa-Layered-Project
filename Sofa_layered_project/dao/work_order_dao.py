from database.connection import Database
from model.work_order import WorkOrder


class WorkOrderDAO:

    def add_work_order(self, work_order):
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        INSERT INTO work_order
        (work_order_id, inquiry_id, visit_id, final_price,
         start_date, expected_completion_date, completion_date,
         status, work_notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            work_order.work_order_id,
            work_order.inquiry_id,
            work_order.visit_id,
            work_order.final_price,
            work_order.start_date,
            work_order.expected_completion_date,
            work_order.completion_date,
            work_order.status,
            work_order.work_notes
        )

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

        print("Work order added successfully.")

    def display_all(self):
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = "SELECT * FROM work_order"

        cursor.execute(query)
        rows = cursor.fetchall()

        work_orders = []

        for row in rows:
            work_order = WorkOrder(
                row[0], row[1], row[2], row[3],
                row[4], row[5], row[6], row[7], row[8]
            )

            work_orders.append(work_order)

        cursor.close()
        connection.close()

        return work_orders

    def display_by_customer_id(self, customer_id):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        query = """
        SELECT wo.*
        FROM work_order wo
        JOIN inquiry i
        ON wo.inquiry_id = i.inquiry_id
        WHERE i.customer_id = %s
        """

        cursor.execute(query, (customer_id,))

        rows = cursor.fetchall()

        work_orders = []

        for row in rows:

            work_order = WorkOrder(
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

            work_orders.append(work_order)

        cursor.close()
        connection.close()

        return work_orders

    def update_status(self, work_order_id, status, work_notes):
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        UPDATE work_order
        SET status = %s,
            work_notes = %s
        WHERE work_order_id = %s
        """

        data = (status, work_notes, work_order_id)

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

        print("Work order updated successfully.")

    def delete_work_order(self, work_order_id):
        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        DELETE FROM work_order
        WHERE work_order_id = %s
        """

        data = (work_order_id,)

        cursor.execute(query, data)
        connection.commit()

        cursor.close()
        connection.close()

        print("Work order deleted successfully.")