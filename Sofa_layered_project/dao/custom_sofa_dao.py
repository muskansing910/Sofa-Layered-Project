from database.connection import Database
from model.custom_sofa import CustomSofa


class CustomSofa_dao:

    def add_custom_sofa(self, custom_sofa):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO custom_sofa
        (custom_sofa_id, customer_id, sofa_type_id,
         design_id, fabric_id, color_id,
         back_design_id, armrest_design_id,
         leg_design_id, foam_type_id,
         length, width, height, seat_depth,
         number_of_seats, custom_requirements)
        VALUES
        (%s, %s, %s, %s, %s, %s, %s, %s,
         %s, %s, %s, %s, %s, %s, %s, %s)
        '''

        data = (
            custom_sofa.custom_sofa_id,
            custom_sofa.customer_id,
            custom_sofa.sofa_type_id,
            custom_sofa.design_id,
            custom_sofa.fabric_id,
            custom_sofa.color_id,
            custom_sofa.back_design_id,
            custom_sofa.armrest_design_id,
            custom_sofa.leg_design_id,
            custom_sofa.foam_type_id,
            custom_sofa.length,
            custom_sofa.width,
            custom_sofa.height,
            custom_sofa.seat_depth,
            custom_sofa.number_of_seats,
            custom_sofa.custom_requirements
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from custom_sofa'

        cursor.execute(query)

        rows = cursor.fetchall()

        custom_sofas = []

        for row in rows:

            custom_sofa = CustomSofa(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6],
                row[7],
                row[8],
                row[9],
                row[10],
                row[11],
                row[12],
                row[13],
                row[14],
                row[15],
                row[16]
            )

            custom_sofas.append(custom_sofa)

        cursor.close()
        conn.close()

        return custom_sofas


    def display_by_id(self, id):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from custom_sofa where custom_sofa_id = %s'

        cursor.execute(query, (id,))

        row = cursor.fetchone()

        if row is None:

            cursor.close()
            conn.close()

            return None

        custom_sofa = CustomSofa(
            row[0],
            row[1],
            row[2],
            row[3],
            row[4],
            row[5],
            row[6],
            row[7],
            row[8],
            row[9],
            row[10],
            row[11],
            row[12],
            row[13],
            row[14],
            row[15],
            row[16]
        )

        cursor.close()
        conn.close()

        return custom_sofa

    def get_next_id(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'SELECT MAX(custom_sofa_id) FROM custom_sofa'

        cursor.execute(query)

        row = cursor.fetchone()

        cursor.close()
        conn.close()

        if row[0] is None:
            return 1

        return row[0] + 1