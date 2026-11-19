class Inquiry:

    def __init__(self, inquiry_id,
                 customer_id,
                 custom_sofa_id,
                 admin_id,
                 inquiry_date,
                 status,
                 customer_message,
                 admin_notes,
                 created_at):

        self.inquiry_id = inquiry_id
        self.customer_id = customer_id
        self.custom_sofa_id = custom_sofa_id
        self.admin_id = admin_id
        self.inquiry_date = inquiry_date
        self.status = status
        self.customer_message = customer_message
        self.admin_notes = admin_notes
        self.created_at = created_at