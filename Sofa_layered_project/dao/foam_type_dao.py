from database.connection import Database
from model.foam_type import FoamType


class FoamType_dao:

    def add_foam_type(self, foam_type):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO foam_type
        (foam_type_id, foam_type_name,
         density, description,
         price_per_cubic_ft, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        data = (
            foam_type.foam_type_id,
            foam_type.foam_type_name,
            foam_type.density,
            foam_type.description,
            foam_type.price_per_cubic_ft,
            foam_type.status
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from foam_type'

        cursor.execute(query)

        rows = cursor.fetchall()

        foam_types = []

        for row in rows:

            foam_type = FoamType(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            foam_types.append(foam_type)

        cursor.close()
        conn.close()

        return foam_types
    def display_active_foam_types(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        SELECT * FROM foam_type
        WHERE UPPER(status) = 'ACTIVE'
        '''

        cursor.execute(query)

        rows = cursor.fetchall()

        foam_types = []

        for row in rows:

            foam_type = FoamType(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            foam_types.append(foam_type)

        cursor.close()
        conn.close()

        return foam_types