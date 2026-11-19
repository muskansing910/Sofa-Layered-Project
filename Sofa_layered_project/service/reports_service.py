from dao.reports_dao import ReportsDAO


class ReportsService:

    def __init__(self):
        self.reports_dao = ReportsDAO()

    def customer_inquiry_report(self):

        reports = self.reports_dao.customer_inquiry_report()

        return reports