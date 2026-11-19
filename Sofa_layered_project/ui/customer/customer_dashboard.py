import customtkinter as ctk
from tkinter import messagebox

class CustomerDashboard:

    def __init__(self, window, customer_id, customer_name):
        self.window = window
        self.customer_id = customer_id
        self.customer_name = customer_name

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # =========================
        # SIDEBAR
        # =========================

        self.sidebar = ctk.CTkFrame(
            self.window,
            width=250
        )

        self.sidebar.pack(
            side="left",
            fill="y"
        )

        # Logo
        self.logo_label = ctk.CTkLabel(
            self.sidebar,
            text="SOFA CUSTOMIZER",
            font=("Arial", 20, "bold")
        )

        self.logo_label.pack(pady=(30, 20))

        # Customer label
        self.customer_label = ctk.CTkLabel(
            self.sidebar,
            text="CUSTOMER",
            font=("Arial", 16, "bold")
        )

        self.customer_label.pack(pady=10)

        # My Profile
        self.profile_button = ctk.CTkButton(
            self.sidebar,
            text="My Profile",
            width=200,
            height=40,
            command=self.open_profile
        )

        self.profile_button.pack(pady=10)

        # Browse Sofa Designs
        self.sofa_button = ctk.CTkButton(
            self.sidebar,
            text="Browse Sofa Designs",
            width=200,
            height=40,
            command=self.open_sofa
        )

        self.sofa_button.pack(pady=10)

        # Customize Sofa
        self.customize_button = ctk.CTkButton(
            self.sidebar,
            text="Customize Sofa",
            width=200,
            height=40,
            command=self.open_customize
        )

        self.customize_button.pack(pady=10)

        # My Inquiries
        self.inquiry_button = ctk.CTkButton(
            self.sidebar,
            text="My Inquiries",
            width=200,
            height=40,
            command=self.open_inquiries
        )

        self.inquiry_button.pack(pady=10)

        # Home Visit
        self.home_visit_button = ctk.CTkButton(
            self.sidebar,
            text="Home Visit",
            width=200,
            height=40,
            command=self.open_home_visit

        )
        self.home_visit_button.pack(pady=10)

        # My Work Order
        self.work_order_button = ctk.CTkButton(
            self.sidebar,
            text="My Work Order",
            width=200,
            height=40,
            command=self.open_work_order
        )

        self.work_order_button.pack(pady=10)

        # Give Feedback
        self.feedback_button = ctk.CTkButton(
            self.sidebar,
            text="Give Feedback",
            width=200,
            height=40,
            command=self.open_feedback

        )

        self.feedback_button.pack(pady=10)

        # Logout
        self.logout_button = ctk.CTkButton(
            self.sidebar,
            text="Logout",
            width=200,
            height=40,
            command=self.logout
        )

        self.logout_button.pack(pady=10)

        # =========================
        # MAIN AREA
        # =========================

        self.main_area = ctk.CTkFrame(
            self.window
        )

        self.main_area.pack(
            side="right",
            fill="both",
            expand=True
        )

        self.title_label = ctk.CTkLabel(
            self.main_area,
            text="CUSTOMER DASHBOARD",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(pady=(80, 20))

        self.welcome_label = ctk.CTkLabel(
            self.main_area,
            text="Welcome to Sofa Customizer!",
            font=("Arial", 20)
        )

        self.welcome_label.pack(pady=10)

    # =========================
    # BROWSE SOFA
    # =========================

    def open_sofa(self):

        from ui.sofa.sofa_ui import SofaUI

        SofaUI(
            self.window,
            self.customer_id,
            self.customer_name
        )

    

    def open_customize(self):

        from ui.sofa.customize_ui import CustomizeUI

        CustomizeUI(
            self.window,
            self.customer_id,
            self.customer_name
        )

    

    def open_inquiries(self):

        messagebox.showinfo(
            "Test",
            "My Inquiries button is working!"
        )

        print("Customer ID:", self.customer_id)
        print("Customer Name:", self.customer_name)

        from ui.inquiry.inquiry_ui import InquiryUI

        print("Opening InquiryUI...")

        InquiryUI(
            self.window,
            self.customer_id,
            self.customer_name
        )

        print("InquiryUI opened")



    def open_home_visit(self):

        from ui.home_visit.home_visit_ui import HomeVisitUI

        HomeVisitUI(
            self.window,
            self.customer_id,
            self.customer_name
        )

    # =========================
# MY WORK ORDER
# =========================

    def open_work_order(self):

        from ui.work_order.work_order_ui import WorkOrderUI

        WorkOrderUI(
            self.window,
            self.customer_id,
            self.customer_name
        )

  
    # =========================
    # MY PROFILE
    # =========================

    def open_profile(self):

        for widget in self.window.winfo_children():
            widget.destroy()

        from service.customer_service import customer_service

        customer_service_obj = customer_service()

        customer = customer_service_obj.search_customer_by_id(
            self.customer_id
        )

        title_label = ctk.CTkLabel(
            self.window,
            text="MY PROFILE",
            font=("Arial", 30, "bold")
        )

        title_label.pack(pady=(50, 20))

        if customer is not None:

            profile_frame = ctk.CTkFrame(
                self.window,
                width=500,
                height=350
            )

            profile_frame.pack(
                padx=20,
                pady=10
            )

            name_label = ctk.CTkLabel(
                profile_frame,
                text="Name: " + str(customer.name),
                font=("Arial", 18)
            )
            name_label.pack(pady=10)

            phone_label = ctk.CTkLabel(
                profile_frame,
                text="Phone: " + str(customer.phone),
                font=("Arial", 18)
            )
            phone_label.pack(pady=10)

            email_label = ctk.CTkLabel(
                profile_frame,
                text="Email: " + str(customer.email),
                font=("Arial", 18)
            )
            email_label.pack(pady=10)

            address_label = ctk.CTkLabel(
                profile_frame,
                text="Address: " + str(customer.address),
                font=("Arial", 18)
            )
            address_label.pack(pady=10)

            city_label = ctk.CTkLabel(
                profile_frame,
                text="City: " + str(customer.city),
                font=("Arial", 18)
            )
            city_label.pack(pady=10)

        else:

            message_label = ctk.CTkLabel(
                self.window,
                text="Customer profile not found.",
                font=("Arial", 18)
            )

            message_label.pack(pady=30)

        back_button = ctk.CTkButton(
            self.window,
            text="← Back to Dashboard",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )

        back_button.pack(pady=20)


    # =========================
    # BACK TO DASHBOARD
    # =========================

    def back_to_dashboard(self):

        CustomerDashboard(
            self.window,
            self.customer_id,
            self.customer_name
        )
    def open_feedback(self):
        print("Give Feedback button clicked")

        from ui.feedback.feedback_ui import FeedbackUI

        FeedbackUI(
            self.window,
            self.customer_id,
            self.customer_name
        )



    def logout(self):

        from ui.login.login_ui import LoginUI

        LoginUI(self.window)