from dao.inquiry_dao import Inquiry_dao


class Inquiry_service:

    def add_inquiry(self, inquiry):

        dao = Inquiry_dao()

        dao.add_inquiry(inquiry)


    def display_inquiries(self):

        dao = Inquiry_dao()

        inquiries = dao.display_all()

        return inquiries
    def display_inquiries_by_customer_id(self, customer_id):
        dao = Inquiry_dao()
        inquiries = dao.display_by_customer_id(customer_id)
        return inquiries

    def get_next_id(self):

        dao = Inquiry_dao()

        next_id = dao.get_next_id()

        return next_id