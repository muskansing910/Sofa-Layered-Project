class HomeVisit:

    def __init__(self, visit_id, inquiry_id, upholsterer_id,
                 visit_date, visit_time, visit_address,
                 status, notes):

        self.visit_id = visit_id
        self.inquiry_id = inquiry_id
        self.upholsterer_id = upholsterer_id
        self.visit_date = visit_date
        self.visit_time = visit_time
        self.visit_address = visit_address
        self.status = status
        self.notes = notes