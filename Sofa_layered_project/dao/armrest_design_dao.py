from database.connection import Database
from model.armrest_design import ArmrestDesign


class ArmrestDesign_dao:

    def add_armrest_design(self, armrest_design):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO armrest_design
        (armrest_design_id, armrest_design_name,
         description, image, status)
        VALUES (%s, %s, %s, %s, %s)
        '''

        data = (
            armrest_design.armrest_design_id,
            armrest_design.armrest_design_name,
            armrest_design.description,
            armrest_design.image,
            armrest_design.status
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from armrest_design'

        cursor.execute(query)

        rows = cursor.fetchall()

        armrest_designs = []

        for row in rows:

            armrest_design = ArmrestDesign(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

            armrest_designs.append(armrest_design)

        cursor.close()
        conn.close()

        return armrest_designs

    def display_active_armrest_designs(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        SELECT * FROM armrest_design
        WHERE UPPER(status) = 'ACTIVE'
        '''

        cursor.execute(query)

        rows = cursor.fetchall()

        armrest_designs = []

        for row in rows:

            armrest_design = ArmrestDesign(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

            armrest_designs.append(armrest_design)

        cursor.close()
        conn.close()

        return armrest_designs