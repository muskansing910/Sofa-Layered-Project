
import customtkinter as ctk
from service.work_order_service import WorkOrderService


class AdminWorkOrderUI:

    def __init__(self, window):

        self.window = window
        self.work_order_service = WorkOrderService()

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # ==============================
        # TITLE
        # ==============================

        self.title_label = ctk.CTkLabel(
            self.window,
            text="WORK ORDER MANAGEMENT",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))

        # ==============================
        # SCROLLABLE FRAME
        # ==============================

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

        # ==============================
        # GET ALL WORK ORDERS
        # ==============================

        work_orders = self.work_order_service.display_all()

        # ==============================
        # DISPLAY WORK ORDERS
        # ==============================

        for work_order in work_orders:

            work_order_frame = ctk.CTkFrame(
                self.scroll_frame
            )

            work_order_frame.pack(
                padx=20,
                pady=10,
                fill="x"
            )

            ctk.CTkLabel(
                work_order_frame,
                text="Work Order ID: " +
                     str(work_order.work_order_id),
                font=("Arial", 18, "bold")
            ).pack(pady=5)

            ctk.CTkLabel(
                work_order_frame,
                text="Inquiry ID: " +
                     str(work_order.inquiry_id)
            ).pack(pady=3)

            ctk.CTkLabel(
                work_order_frame,
                text="Visit ID: " +
                     str(work_order.visit_id)
            ).pack(pady=3)

            ctk.CTkLabel(
                work_order_frame,
                text="Final Price: " +
                     str(work_order.final_price)
            ).pack(pady=3)

            ctk.CTkLabel(
                work_order_frame,
                text="Start Date: " +
                     str(work_order.start_date)
            ).pack(pady=3)

            ctk.CTkLabel(
                work_order_frame,
                text="Expected Completion Date: " +
                     str(work_order.expected_completion_date)
            ).pack(pady=3)

            ctk.CTkLabel(
                work_order_frame,
                text="Completion Date: " +
                     str(work_order.completion_date)
            ).pack(pady=3)

            ctk.CTkLabel(
                work_order_frame,
                text="Status: " +
                     str(work_order.status)
            ).pack(pady=3)

            ctk.CTkLabel(
                work_order_frame,
                text="Work Notes: " +
                     str(work_order.work_notes)
            ).pack(pady=3)

        # ==============================
        # BACK BUTTON
        # ==============================

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back to Dashboard",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )

        self.back_button.pack(pady=15)

    # ==============================
    # BACK TO ADMIN DASHBOARD
    # ==============================

    def back_to_dashboard(self):

        from ui.admin.admin_dashboard import AdminDashboard

        AdminDashboard(self.window)
