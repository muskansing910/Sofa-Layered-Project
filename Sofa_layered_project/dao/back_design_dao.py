from database.connection import Database
from model.back_design import BackDesign


class BackDesign_dao:

    def add_back_design(self, back_design):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO back_design
        (back_design_id, back_design_name,
         description, image, status)
        VALUES (%s, %s, %s, %s, %s)
        '''

        data = (
            back_design.back_design_id,
            back_design.back_design_name,
            back_design.description,
            back_design.image,
            back_design.status
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from back_design'

        cursor.execute(query)

        rows = cursor.fetchall()

        back_designs = []

        for row in rows:

            back_design = BackDesign(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

            back_designs.append(back_design)

        cursor.close()
        conn.close()

        return back_designs
    def display_active_back_designs(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        SELECT * FROM back_design
        WHERE UPPER(status) = 'ACTIVE'
        '''

        cursor.execute(query)

        rows = cursor.fetchall()

        back_designs = []

        for row in rows:

            back_design = BackDesign(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

            back_designs.append(back_design)

        cursor.close()
        conn.close()

        return back_designs