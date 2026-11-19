from service.home_visit_service import HomeVisitService

service = HomeVisitService()

customer_id = 1234

home_visits = service.display_by_customer_id(customer_id)

print("Home Visits for Customer:", customer_id)

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