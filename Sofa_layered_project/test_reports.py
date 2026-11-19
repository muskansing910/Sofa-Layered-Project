from service.reports_service import ReportsService


service = ReportsService()

reports = service.customer_inquiry_report()

for report in reports:

    print("--------------------------------")
    print("Customer ID:", report.customer_id)
    print("Name:", report.name)
    print("Phone:", report.phone)
    print("Inquiry ID:", report.inquiry_id)
    print("Inquiry Date:", report.inquiry_date)
    print("Status:", report.status)
    print("Message:", report.customer_message)