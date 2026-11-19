class CustomerInquiryReport:

    def __init__(self, customer_id, name, phone,
                 inquiry_id, inquiry_date, status,
                 customer_message):

        self.customer_id = customer_id
        self.name = name
        self.phone = phone
        self.inquiry_id = inquiry_id
        self.inquiry_date = inquiry_date
        self.status = status
        self.customer_message = customer_message