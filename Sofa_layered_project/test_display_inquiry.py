from service.inquiry_service import Inquiry_service


inquiry_service = Inquiry_service()

inquiries = inquiry_service.display_inquiries()

print("\n========== ALL INQUIRIES ==========")

for inquiry in inquiries:

    print(
        inquiry.inquiry_id,
        inquiry.customer_id,
        inquiry.custom_sofa_id,
        inquiry.admin_id,
        inquiry.inquiry_date,
        inquiry.status,
        inquiry.customer_message,
        inquiry.admin_notes,
        inquiry.created_at
    )