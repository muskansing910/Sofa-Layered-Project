
from model.work_order import WorkOrder
from dao.work_order_dao import WorkOrderDAO


class WorkOrderService:

    def __init__(self):
        self.work_order_dao = WorkOrderDAO()

    def add_work_order(self, work_order_id, inquiry_id, visit_id,
                       final_price, start_date,
                       expected_completion_date, completion_date,
                       status, work_notes):

        work_order = WorkOrder(
            work_order_id,
            inquiry_id,
            visit_id,
            final_price,
            start_date,
            expected_completion_date,
            completion_date,
            status,
            work_notes
        )

        self.work_order_dao.add_work_order(work_order)

    def display_all(self):

        work_orders = self.work_order_dao.display_all()

        return work_orders

    def display_by_customer_id(self, customer_id):

        work_orders = self.work_order_dao.display_by_customer_id(
            customer_id
        )

        return work_orders

    def update_status(self, work_order_id, status, work_notes):

        self.work_order_dao.update_status(
            work_order_id,
            status,
            work_notes
        )

    def delete_work_order(self, work_order_id):

        self.work_order_dao.delete_work_order(
            work_order_id
        )

