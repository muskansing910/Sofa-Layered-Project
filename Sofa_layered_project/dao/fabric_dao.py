from database.connection import Database
from model.fabric import Fabric


class Fabric_dao:

    def add_fabric(self, fabric):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO fabric
        (fabric_id, fabric_name, description,
         price_per_meter, image, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        data = (
            fabric.fabric_id,
            fabric.fabric_name,
            fabric.description,
            fabric.price_per_meter,
            fabric.image,
            fabric.status
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from fabric'

        cursor.execute(query)

        rows = cursor.fetchall()

        fabrics = []

        for row in rows:

            fabric = Fabric(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            fabrics.append(fabric)

        cursor.close()
        conn.close()

        return fabrics

    def display_active_fabrics(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        SELECT * FROM fabric
        WHERE UPPER(status) = 'ACTIVE'
        '''

        cursor.execute(query)

        rows = cursor.fetchall()

        fabrics = []

        for row in rows:

            fabric = Fabric(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            fabrics.append(fabric)

        cursor.close()
        conn.close()

        return fabrics