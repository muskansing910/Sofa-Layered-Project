from database.connection import Database
from model.sofa_type import SofaType


class SofaType_dao:

    def add_sofa_type(self, sofa_type):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'INSERT INTO sofa_type(sofa_type_id, type_name, description, status) VALUES (%s, %s, %s, %s)'

        data = (
            sofa_type.sofa_type_id,
            sofa_type.type_name,
            sofa_type.description,
            sofa_type.status
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from sofa_type'

        cursor.execute(query)

        rows = cursor.fetchall()

        sofa_types = []

        for row in rows:

            sofa_type = SofaType(row[0],row[1],row[2],row[3],row[4])
            
            sofa_types.append(sofa_type)

        cursor.close()
        conn.close()

        return sofa_types
    def display_active_sofa_types(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        SELECT * FROM sofa_type
        WHERE UPPER(status) = 'ACTIVE'
        '''

        cursor.execute(query)

        rows = cursor.fetchall()

        sofa_types = []

        for row in rows:

            sofa_type = SofaType(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4]
            )

            sofa_types.append(sofa_type)

        cursor.close()
        conn.close()

        return sofa_types