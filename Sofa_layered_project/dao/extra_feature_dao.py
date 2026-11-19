from database.connection import Database
from model.extra_feature import ExtraFeature


class ExtraFeature_dao:

    def add_extra_feature(self, extra_feature):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = '''
        INSERT INTO extra_feature
        (feature_id, feature_name, description,
         additional_price, image, status)
        VALUES (%s, %s, %s, %s, %s, %s)
        '''

        data = (
            extra_feature.feature_id,
            extra_feature.feature_name,
            extra_feature.description,
            extra_feature.additional_price,
            extra_feature.image,
            extra_feature.status
        )

        cursor.execute(query, data)

        conn.commit()

        cursor.close()
        conn.close()


    def display_all(self):

        db = Database()
        conn = db.connect()
        cursor = conn.cursor()

        query = 'select * from extra_feature'

        cursor.execute(query)

        rows = cursor.fetchall()

        extra_features = []

        for row in rows:

            extra_feature = ExtraFeature(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            extra_features.append(extra_feature)

        cursor.close()
        conn.close()

        return extra_features