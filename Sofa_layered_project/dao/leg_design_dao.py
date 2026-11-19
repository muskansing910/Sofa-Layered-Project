from database.connection import Database
from model.leg_design import LegDesign


class LegDesign_dao:

    def add_leg_design(self, leg_design):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO leg_design
        (leg_design_id, leg_design_name,
         material, description, image, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        data = (
            leg_design.leg_design_id,
            leg_design.leg_design_name,
            leg_design.material,
            leg_design.description,
            leg_design.image,
            leg_design.status
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from leg_design'

        cursor.execute(query)

        rows = cursor.fetchall()

        leg_designs = []

        for row in rows:

            leg_design = LegDesign(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            leg_designs.append(leg_design)

        cursor.close()
        conn.close()

        return leg_designs
    def display_active_leg_designs(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        SELECT * FROM leg_design
        WHERE UPPER(status) = 'ACTIVE'
        '''

        cursor.execute(query)

        rows = cursor.fetchall()

        leg_designs = []

        for row in rows:

            leg_design = LegDesign(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            leg_designs.append(leg_design)

        cursor.close()
        conn.close()

        return leg_designs