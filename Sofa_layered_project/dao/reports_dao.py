from database.connection import Database

from model.reports import CustomerInquiryReport

class ReportsDAO:

    def customer_inquiry_report(self):

        db = Database()
        connection = db.connect()
        cursor = connection.cursor()

        query = """
        SELECT
            c.customer_id,
            c.name,
            c.phone,
            i.inquiry_id,
            i.inquiry_date,
            i.status,
            i.customer_message
        FROM customer c
        JOIN inquiry i
            ON c.customer_id = i.customer_id
        """

        cursor.execute(query)

        rows = cursor.fetchall()

        reports = []

        for row in rows:

            report = CustomerInquiryReport(
                row[0],
                row[1],
                row[2],
                row[3],
                row[4],
                row[5],
                row[6]
            )

            reports.append(report)

        cursor.close()
        connection.close()

        return reports