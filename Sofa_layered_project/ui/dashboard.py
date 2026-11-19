import customtkinter as ctk
from ui.customer.customer_dashboard import CustomerUI

class Dashboard:

    def __init__(self):

        self.window = ctk.CTk()

        self.window.title("Sofa Customizer Management System")

        self.window.geometry("1100x650")


        # ================= SIDEBAR =================

        self.sidebar = ctk.CTkFrame(
            self.window,
            width=250
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )


        # Sidebar title
        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text="SOFA CUSTOMIZER",
            font=("Arial", 20, "bold")
        )

        self.logo_label.pack(pady=30)


        # Customer button
        self.customer_button = ctk.CTkButton(
            self.sidebar,
            text="Customer Management",
            width=200,
            height=40,
            command=self.open_customer
        )

        self.customer_button.pack(pady=10)


        # Sofa button
        self.sofa_button = ctk.CTkButton(
            self.sidebar,
            text="Sofa Management",
            width=200,
            height=40
        )

        self.sofa_button.pack(pady=10)


        # Inquiry button
        self.inquiry_button = ctk.CTkButton(
            self.sidebar,
            text="Inquiry Management",
            width=200,
            height=40
        )

        self.inquiry_button.pack(pady=10)


        # Home Visit button
        self.home_visit_button = ctk.CTkButton(
            self.sidebar,
            text="Home Visit",
            width=200,
            height=40
        )

        self.home_visit_button.pack(pady=10)


        # Work Order button
        self.work_order_button = ctk.CTkButton(
            self.sidebar,
            text="Work Order",
            width=200,
            height=40
        )

        self.work_order_button.pack(pady=10)


        self.feedback_button = ctk.CTkButton(
        self.sidebar,
        text="Give Feedback",
        width=200,
        height=40,
        command=self.open_feedback
    )

        self.feedback_button.pack(pady=10)


        # Reports button
        self.reports_button = ctk.CTkButton(
            self.sidebar,
            text="Reports",
            width=200,
            height=40
        )

        self.reports_button.pack(pady=10)


        # ================= MAIN AREA =================

        self.main_area = ctk.CTkFrame(
            self.window
        )

        self.main_area.pack(
            side="right",
            fill="both",
            expand=True
        )


        # Main title
        self.title_label = ctk.CTkLabel(
            self.main_area,
            text="SOFA CUSTOMIZER MANAGEMENT SYSTEM",
            font=("Arial", 28, "bold")
        )

        self.title_label.pack(pady=50)


        self.welcome_label = ctk.CTkLabel(
            self.main_area,
            text="Welcome to the Management Dashboard",
            font=("Arial", 18)
        )

        self.welcome_label.pack(pady=10)


        # Start application
        self.window.mainloop()

    def open_customer(self):

        for widget in self.main_area.winfo_children():
            widget.destroy()

        CustomerUI(self.main_area)

    def open_feedback(self):
        from ui.feedback.feedback_ui import FeedbackUI
        FeedbackUI(self.window, self.customer_id, self.customer_name)