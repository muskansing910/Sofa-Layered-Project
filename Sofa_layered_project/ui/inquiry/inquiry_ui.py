import customtkinter as ctk

from service.inquiry_service import Inquiry_service


class InquiryUI:

    def __init__(self, window, customer_id, customer_name):
        self.window = window
        self.customer_id = customer_id
        self.customer_name = customer_name

        self.inquiry_service = Inquiry_service()

        for widget in self.window.winfo_children():
            widget.destroy()

        self.title_label = ctk.CTkLabel(
            self.window,
            text="MY INQUIRIES",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))

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

        print("Logged Customer ID:", self.customer_id)
        inquiries = self.inquiry_service.display_inquiries_by_customer_id(self.customer_id)

        for inquiry in inquiries:

            inquiry_frame = ctk.CTkFrame(
                self.scroll_frame
            )
            inquiry_frame.pack(
                padx=20,
                pady=10,
                fill="x"
            )

            inquiry_label = ctk.CTkLabel(
                inquiry_frame,
                text="Inquiry ID: " + str(inquiry.inquiry_id),
                font=("Arial", 18, "bold")
            )
            inquiry_label.pack(pady=5)

            customer_label = ctk.CTkLabel(
                inquiry_frame,
                text="Customer ID: " + str(inquiry.customer_id)
            )
            customer_label.pack(pady=3)

            sofa_label = ctk.CTkLabel(
                inquiry_frame,
                text="Custom Sofa ID: " + str(inquiry.custom_sofa_id)
            )
            sofa_label.pack(pady=3)

            status_label = ctk.CTkLabel(
                inquiry_frame,
                text="Status: " + str(inquiry.status)
            )
            status_label.pack(pady=3)

            message_label = ctk.CTkLabel(
                inquiry_frame,
                text="Message: " + str(inquiry.customer_message)
            )
            message_label.pack(pady=3)

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