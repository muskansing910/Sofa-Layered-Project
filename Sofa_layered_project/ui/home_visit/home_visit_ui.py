import customtkinter as ctk

from service.home_visit_service import HomeVisitService


class HomeVisitUI:

    def __init__(self, window, customer_id, customer_name):

        self.window = window
        self.customer_id = customer_id
        self.customer_name = customer_name

        self.home_visit_service = HomeVisitService()

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # Title
        self.title_label = ctk.CTkLabel(
            self.window,
            text="MY HOME VISIT",
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

        # Get customer's home visits
        home_visits = self.home_visit_service.display_by_customer_id(
            self.customer_id
        )

        # Check if there are no visits
        if len(home_visits) == 0:

            no_visit_label = ctk.CTkLabel(
                self.scroll_frame,
                text="No home visit scheduled yet.",
                font=("Arial", 18)
            )
            no_visit_label.pack(pady=50)

        else:

            for visit in home_visits:

                visit_frame = ctk.CTkFrame(
                    self.scroll_frame
                )
                visit_frame.pack(
                    padx=20,
                    pady=10,
                    fill="x"
                )

                visit_id_label = ctk.CTkLabel(
                    visit_frame,
                    text="Visit ID: " + str(visit.visit_id),
                    font=("Arial", 18, "bold")
                )
                visit_id_label.pack(pady=5)

                inquiry_label = ctk.CTkLabel(
                    visit_frame,
                    text="Inquiry ID: " + str(visit.inquiry_id)
                )
                inquiry_label.pack(pady=3)

                upholsterer_label = ctk.CTkLabel(
                    visit_frame,
                    text="Upholsterer ID: " + str(visit.upholsterer_id)
                )
                upholsterer_label.pack(pady=3)

                date_label = ctk.CTkLabel(
                    visit_frame,
                    text="Visit Date: " + str(visit.visit_date)
                )
                date_label.pack(pady=3)

                time_label = ctk.CTkLabel(
                    visit_frame,
                    text="Visit Time: " + str(visit.visit_time)
                )
                time_label.pack(pady=3)

                address_label = ctk.CTkLabel(
                    visit_frame,
                    text="Address: " + str(visit.visit_address)
                )
                address_label.pack(pady=3)

                status_label = ctk.CTkLabel(
                    visit_frame,
                    text="Status: " + str(visit.status)
                )
                status_label.pack(pady=3)

                notes_label = ctk.CTkLabel(
                    visit_frame,
                    text="Notes: " + str(visit.notes)
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