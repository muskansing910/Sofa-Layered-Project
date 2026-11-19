from model.inquiry import Inquiry
from service.inquiry_service import Inquiry_service


inquiry = Inquiry(
    1310,              # inquiry_id
    1234,              # customer_id
    1310,              # custom_sofa_id
    None,              # admin_id
    None,              # inquiry_date
    "NEW",             # status
    "Customer customized sofa",  # customer_message
    None,              # admin_notes
    None               # created_at
)

service = Inquiry_service()

service.add_inquiry(inquiry)

print("Inquiry added successfully!")