from database.connection import Database
from model.home_visit import HomeVisit


class HomeVisitDAO:

    def add_home_visit(self, home_visit):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        query = """
        INSERT INTO home_visit
        (visit_id, inquiry_id, upholsterer_id, visit_date,
         visit_time, visit_address, status, notes)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """

        data = (
            home_visit.visit_id,
            home_visit.inquiry_id,
            home_visit.upholsterer_id,
            home_visit.visit_date,
            home_visit.visit_time,
            home_visit.visit_address,
            home_visit.status,
            home_visit.notes
        )

        cursor.execute(query, data)

        connection.commit()

        cursor.close()
        connection.close()

        print("Home visit added successfully.")

    def display_all(self):

            db = Database()
            connection = db.connect()

            cursor = connection.cursor()

            query = "SELECT * FROM home_visit"

            cursor.execute(query)

            rows = cursor.fetchall()

            home_visits = []

            for row in rows:

                home_visit = HomeVisit(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7]
                )

                home_visits.append(home_visit)

            cursor.close()
            connection.close()

            return home_visits

    def display_by_customer_id(self, customer_id):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        query = """
        SELECT hv.*
        FROM home_visit hv
        JOIN inquiry i
        ON hv.inquiry_id = i.inquiry_id
        WHERE i.customer_id = %s
        """

        cursor.execute(query, (customer_id,))

        rows = cursor.fetchall()

        home_visits = []

        for row in rows:

            home_visit = HomeVisit(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )

            home_visits.append(home_visit)

        cursor.close()
        connection.close()

        return home_visits
    
    def update_status(self, visit_id, status, notes):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        query = """
        UPDATE home_visit
        SET status = %s,
            notes = %s
        WHERE visit_id = %s
        """

        data = (
            status,
            notes,
            visit_id
        )

        cursor.execute(query, data)

        connection.commit()

        cursor.close()
        connection.close()

        print("Home visit updated successfully.")

    def delete_home_visit(self, visit_id):

        db = Database()
        connection = db.connect()

        cursor = connection.cursor()

        query = """
        DELETE FROM home_visit
        WHERE visit_id = %s
        """

        data = (visit_id,)

        cursor.execute(query, data)

        connection.commit()

        cursor.close()
        connection.close()

        print("Home visit deleted successfully.")