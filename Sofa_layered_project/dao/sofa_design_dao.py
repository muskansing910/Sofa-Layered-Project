from database.connection import Database
from model.sofa_design import SofaDesign


class SofaDesign_dao:

    def add_sofa_design(self, sofa_design):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO sofa_design
        (design_id, sofa_type_id, design_name,
         description, starting_price, image, status)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        '''

        data = (
            sofa_design.design_id,
            sofa_design.sofa_type_id,
            sofa_design.design_name,
            sofa_design.description,
            sofa_design.starting_price,
            sofa_design.image,
            sofa_design.status
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from sofa_design'

        cursor.execute(query)

        rows = cursor.fetchall()

        designs = []

        for row in rows:

            design = SofaDesign(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7]
            )

            designs.append(design)

        cursor.close()
        conn.close()

        return designs

    def display_active_designs(self):

            db = Database()
            conn = db.connect()
            cursor = conn.cursor()

            query = '''
            SELECT * FROM sofa_design
            WHERE UPPER(status) = 'ACTIVE'
            '''

            cursor.execute(query)

            rows = cursor.fetchall()

            designs = []

            for row in rows:

                design = SofaDesign(
                    row[0],
                    row[1],
                    row[2],
                    row[3],
                    row[4],
                    row[5],
                    row[6],
                    row[7]
                )

                designs.append(design)

            cursor.close()
            conn.close()

            return designs