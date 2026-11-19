
import customtkinter as ctk
from service.feedback_service import FeedbackService


class AdminFeedbackUI:

    def __init__(self, window):

        self.window = window
        self.feedback_service = FeedbackService()

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # ==============================
        # TITLE
        # ==============================

        self.title_label = ctk.CTkLabel(
            self.window,
            text="FEEDBACK MANAGEMENT",
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
        # GET ALL FEEDBACK
        # ==============================

        feedbacks = self.feedback_service.display_all()

        # ==============================
        # DISPLAY FEEDBACK
        # ==============================

        for feedback in feedbacks:

            feedback_frame = ctk.CTkFrame(
                self.scroll_frame
            )

            feedback_frame.pack(
                padx=20,
                pady=10,
                fill="x"
            )

            ctk.CTkLabel(
                feedback_frame,
                text="Feedback ID: " +
                     str(feedback.feedback_id),
                font=("Arial", 18, "bold")
            ).pack(pady=5)

            ctk.CTkLabel(
                feedback_frame,
                text="Work Order ID: " +
                     str(feedback.work_order_id)
            ).pack(pady=3)

            ctk.CTkLabel(
                feedback_frame,
                text="Rating: " +
                     str(feedback.rating)
            ).pack(pady=3)

            ctk.CTkLabel(
                feedback_frame,
                text="Comment: " +
                     str(feedback.comment)
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