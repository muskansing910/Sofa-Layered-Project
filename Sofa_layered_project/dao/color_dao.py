from database.connection import Database
from model.color import Color


class Color_dao:

    def add_color(self, color):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO color
        (color_id, color_name, color_code,
         description, status)
        VALUES (%s, %s, %s, %s, %s)
        '''

        data = (
            color.color_id,
            color.color_name,
            color.color_code,
            color.description,
            color.status
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from color'

        cursor.execute(query)

        rows = cursor.fetchall()

        colors = []

        for row in rows:

            color = Color(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

            colors.append(color)

        cursor.close()
        conn.close()

        return colors

    def display_active_colors(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        SELECT * FROM color
        WHERE UPPER(status) = 'ACTIVE'
        '''

        cursor.execute(query)

        rows = cursor.fetchall()

        colors = []

        for row in rows:

            color = Color(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5]
            )

            colors.append(color)

        cursor.close()
        conn.close()

        return colors