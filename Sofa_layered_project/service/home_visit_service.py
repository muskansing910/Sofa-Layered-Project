from model.home_visit import HomeVisit
from dao.home_visit_dao import HomeVisitDAO


class HomeVisitService:

    def __init__(self):
        self.home_visit_dao = HomeVisitDAO()

    def add_home_visit(self, visit_id, inquiry_id, upholsterer_id,
                       visit_date, visit_time, visit_address,
                       status, notes):

        home_visit = HomeVisit(
            visit_id,
            inquiry_id,
            upholsterer_id,
            visit_date,
            visit_time,
            visit_address,
            status,
            notes
        )

        self.home_visit_dao.add_home_visit(home_visit)

    def display_all(self):

        home_visits = self.home_visit_dao.display_all()

        for visit in home_visits:

            print("----------------------------------------")
            print("Visit ID       :", visit.visit_id)
            print("Inquiry ID     :", visit.inquiry_id)
            print("Upholsterer ID :", visit.upholsterer_id)
            print("Visit Date     :", visit.visit_date)
            print("Visit Time     :", visit.visit_time)
            print("Address        :", visit.visit_address)
            print("Status         :", visit.status)
            print("Notes          :", visit.notes)

    def display_by_customer_id(self, customer_id):

        home_visits = self.home_visit_dao.display_by_customer_id(customer_id)

        return home_visits

    def update_status(self, visit_id, status, notes):

        self.home_visit_dao.update_status(
            visit_id,
            status,
            notes
        )
    def delete_home_visit(self, visit_id):

        self.home_visit_dao.delete_home_visit(visit_id)