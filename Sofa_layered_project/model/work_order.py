class WorkOrder:

    def __init__(self, work_order_id, inquiry_id, visit_id,
                 final_price, start_date, expected_completion_date,
                 completion_date, status, work_notes):

        self.work_order_id = work_order_id
        self.inquiry_id = inquiry_id
        self.visit_id = visit_id
        self.final_price = final_price
        self.start_date = start_date
        self.expected_completion_date = expected_completion_date
        self.completion_date = completion_date
        self.status = status
        self.work_notes = work_notes