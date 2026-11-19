
import customtkinter as ctk
from tkinter import messagebox

from service.work_order_service import WorkOrderService
from service.feedback_service import FeedbackService


class FeedbackUI:

    def __init__(self, window, customer_id, customer_name):

        self.window = window
        self.customer_id = customer_id
        self.customer_name = customer_name

        self.work_order_service = WorkOrderService()
        self.feedback_service = FeedbackService()

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # =========================
        # Title
        # =========================

        title_label = ctk.CTkLabel(
            self.window,
            text="GIVE FEEDBACK",
            font=("Arial", 30, "bold")
        )
        title_label.pack(pady=(40, 20))

        # =========================
        # Work Order
        # =========================

        work_orders = self.work_order_service.display_by_customer_id(
            self.customer_id
        )

        print("Customer ID:", self.customer_id)
        print("Number of Work Orders:", len(work_orders))

        completed_work_order = None

        for work_order in work_orders:

            print(
                "Work Order:",
                work_order.work_order_id,
                "Status:",
                work_order.status
            )

            if work_order.status == "COMPLETED":
                completed_work_order = work_order
                break

        # =========================
        # Feedback Form
        # =========================



        if completed_work_order is not None:

            self.work_order_id = completed_work_order.work_order_id

            work_order_label = ctk.CTkLabel(
                self.window,
                text=f"Work Order ID: {self.work_order_id}",
                font=("Arial", 18, "bold")
            )
            work_order_label.pack(pady=10)

            status_label = ctk.CTkLabel(
                self.window,
                text="Status: COMPLETED",
                font=("Arial", 16)
            )
            status_label.pack(pady=5)

            # Check whether feedback is already submitted
            feedbacks = self.feedback_service.display_all()

            feedback_already_submitted = False

            for feedback in feedbacks:

                if feedback.work_order_id == self.work_order_id:
                    feedback_already_submitted = True
                    break

            if feedback_already_submitted:

                already_label = ctk.CTkLabel(
                    self.window,
                    text="Feedback Already Submitted",
                    font=("Arial", 20, "bold")
                )
                already_label.pack(pady=40)

            else:

                rating_label = ctk.CTkLabel(
                    self.window,
                    text="Select Rating:",
                    font=("Arial", 16)
                )
                rating_label.pack(pady=(20, 5))

                self.rating_dropdown = ctk.CTkOptionMenu(
                    self.window,
                    values=["1", "2", "3", "4", "5"],
                    width=200
                )
                self.rating_dropdown.set("5")
                self.rating_dropdown.pack(pady=5)

                comment_label = ctk.CTkLabel(
                    self.window,
                    text="Your Comment:",
                    font=("Arial", 16)
                )
                comment_label.pack(pady=(20, 5))

                self.comment_entry = ctk.CTkTextbox(
                    self.window,
                    width=400,
                    height=120
                )
                self.comment_entry.pack(pady=5)

                submit_button = ctk.CTkButton(
                    self.window,
                    text="Submit Feedback",
                    width=200,
                    height=40,
                    command=self.submit_feedback
                )
                submit_button.pack(pady=20)

        else:

            message_label = ctk.CTkLabel(
                self.window,
                text="No completed work order available for feedback.",
                font=("Arial", 18)
            )
            message_label.pack(pady=30)

        # =========================
        # Back Button
        # =========================

        back_button = ctk.CTkButton(
            self.window,
            text="← Back to Dashboard",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )
        back_button.pack(pady=20)

    # =========================
    # Submit Feedback
    # =========================

    def submit_feedback(self):

        rating = int(self.rating_dropdown.get())

        comment = self.comment_entry.get(
            "1.0",
            "end"
        ).strip()

        if comment == "":
            messagebox.showwarning(
                "Warning",
                "Please enter your comment."
            )
            return

        feedbacks = self.feedback_service.display_all()

        if len(feedbacks) == 0:

            feedback_id = 1601

        else:

            max_id = 0

            for feedback in feedbacks:

                if feedback.feedback_id > max_id:
                    max_id = feedback.feedback_id

            feedback_id = max_id + 1

        self.feedback_service.add_feedback(
            feedback_id,
            self.work_order_id,
            rating,
            comment
        )

        messagebox.showinfo(
            "Success",
            "Feedback submitted successfully!"
        )

        self.back_to_dashboard()

    # =========================
    # Back to Dashboard
    # =========================

    def back_to_dashboard(self):

        from ui.customer.customer_dashboard import CustomerDashboard

        CustomerDashboard(
            self.window,
            self.customer_id,
            self.customer_name
        )
