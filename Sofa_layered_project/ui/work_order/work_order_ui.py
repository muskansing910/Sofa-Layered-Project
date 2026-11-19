import customtkinter as ctk

from service.work_order_service import WorkOrderService


class WorkOrderUI:

    def __init__(self, window, customer_id, customer_name):

        self.window = window
        self.customer_id = customer_id
        self.customer_name = customer_name

        self.work_order_service = WorkOrderService()

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # Title
        self.title_label = ctk.CTkLabel(
            self.window,
            text="MY WORK ORDER",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))

        # Scroll frame
        self.scroll_frame = ctk.CTkScrollableFrame(
            self.window,
            width=850,
            height=450
        )
        self.scroll_frame.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        # Get customer's work orders
        work_orders = self.work_order_service.display_by_customer_id(
            self.customer_id
        )

        # Check if there are no work orders
        if len(work_orders) == 0:

            no_order_label = ctk.CTkLabel(
                self.scroll_frame,
                text="No work order available yet.",
                font=("Arial", 18)
            )
            no_order_label.pack(pady=50)

        else:

            for work_order in work_orders:

                order_frame = ctk.CTkFrame(
                    self.scroll_frame
                )
                order_frame.pack(
                    padx=20,
                    pady=10,
                    fill="x"
                )

                order_id_label = ctk.CTkLabel(
                    order_frame,
                    text="Work Order ID: "
                         + str(work_order.work_order_id),
                    font=("Arial", 18, "bold")
                )
                order_id_label.pack(pady=5)

                inquiry_label = ctk.CTkLabel(
                    order_frame,
                    text="Inquiry ID: "
                         + str(work_order.inquiry_id)
                )
                inquiry_label.pack(pady=3)

                visit_label = ctk.CTkLabel(
                    order_frame,
                    text="Visit ID: "
                         + str(work_order.visit_id)
                )
                visit_label.pack(pady=3)

                price_label = ctk.CTkLabel(
                    order_frame,
                    text="Final Price: ₹"
                         + str(work_order.final_price)
                )
                price_label.pack(pady=3)

                start_label = ctk.CTkLabel(
                    order_frame,
                    text="Start Date: "
                         + str(work_order.start_date)
                )
                start_label.pack(pady=3)

                expected_label = ctk.CTkLabel(
                    order_frame,
                    text="Expected Completion: "
                         + str(work_order.expected_completion_date)
                )
                expected_label.pack(pady=3)

                completion_label = ctk.CTkLabel(
                    order_frame,
                    text="Completion Date: "
                         + str(work_order.completion_date)
                )
                completion_label.pack(pady=3)

                status_label = ctk.CTkLabel(
                    order_frame,
                    text="Status: "
                         + str(work_order.status)
                )
                status_label.pack(pady=3)

                notes_label = ctk.CTkLabel(
                    order_frame,
                    text="Work Notes: "
                         + str(work_order.work_notes)
                )
                notes_label.pack(pady=(3, 10))

        # Back button
        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back to Dashboard",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=15)

    def back_to_dashboard(self):

        from ui.customer.customer_dashboard import CustomerDashboard

        CustomerDashboard(
            self.window,
            self.customer_id,
            self.customer_name
        )