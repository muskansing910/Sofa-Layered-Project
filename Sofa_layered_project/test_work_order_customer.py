from service.work_order_service import WorkOrderService

service = WorkOrderService()

customer_id = 1234

work_orders = service.display_by_customer_id(customer_id)

print("Work Orders for Customer:", customer_id)

for work_order in work_orders:

    print("----------------------------------------")
    print("Work Order ID       :", work_order.work_order_id)
    print("Inquiry ID          :", work_order.inquiry_id)
    print("Visit ID            :", work_order.visit_id)
    print("Final Price         :", work_order.final_price)
    print("Start Date          :", work_order.start_date)
    print("Expected Completion :", work_order.expected_completion_date)
    print("Completion Date     :", work_order.completion_date)
    print("Status              :", work_order.status)
    print("Work Notes          :", work_order.work_notes)