
import customtkinter as ctk


class AdminDashboard:

    def __init__(self, window):

        self.window = window

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()


        self.title_label = ctk.CTkLabel(
            self.window,
            text="ADMIN DASHBOARD",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(pady=(40, 10))


        self.welcome_label = ctk.CTkLabel(
            self.window,
            text="Welcome Admin!",
            font=("Arial", 20)
        )

        self.welcome_label.pack(pady=10)


        self.customer_button = ctk.CTkButton(
            self.window,
            text="Customer Management",
            width=300,
            height=40,
            command=self.open_customer_management
        )

        self.customer_button.pack(pady=10)


        self.inquiry_button = ctk.CTkButton(
            self.window,
            text="Inquiry Management",
            width=300,
            height=40,
            command=self.open_inquiry_management
        )

        self.inquiry_button.pack(pady=10)

        self.home_visit_button = ctk.CTkButton(
            self.window,
            text="Home Visit Management",
            width=300,
            height=40,
            command=self.open_home_visit_management
        )

        self.home_visit_button.pack(pady=10)

        
        self.work_order_button = ctk.CTkButton(
            self.window,
            text="Work Order Management",
            width=300,
            height=40,
            command=self.open_work_order_management
        )
        self.work_order_button.pack(pady=10)

        
        self.feedback_button = ctk.CTkButton(
            self.window,
            text="Feedback Management",
            width=300,
            height=40,
            command=self.open_feedback_management
        )
        self.feedback_button.pack(pady=10)




        self.logout_button = ctk.CTkButton(
            self.window,
            text="Logout",
            width=200,
            height=40,
            command=self.logout
        )

        self.logout_button.pack(pady=30)

  

    def open_customer_management(self):

        from ui.customer.customer_ui import CustomerUI

        CustomerUI(self.window)


    def open_inquiry_management(self):

        from ui.inquiry.admin_inquiry_ui import AdminInquiryUI

        AdminInquiryUI(self.window)

    def open_home_visit_management(self):
        from ui.home_visit.admin_home_visit_ui import AdminHomeVisitUI
        AdminHomeVisitUI(self.window)

    def open_work_order_management(self):
        from ui.work_order.admin_work_order_ui import AdminWorkOrderUI

        AdminWorkOrderUI(self.window)

    def open_feedback_management(self):
        from ui.feedback.admin_feedback_ui import AdminFeedbackUI
        AdminFeedbackUI(self.window)

    def logout(self):

        from ui.login.login_ui import LoginUI

        LoginUI(self.window)

