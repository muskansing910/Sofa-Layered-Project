
import customtkinter as ctk

from service.home_visit_service import HomeVisitService


class AdminHomeVisitUI:

    def __init__(self, window):

        self.window = window

        self.home_visit_service = HomeVisitService()

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # =========================
        # Title
        # =========================

        self.title_label = ctk.CTkLabel(
            self.window,
            text="HOME VISIT MANAGEMENT",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))

        # =========================
        # Scroll Frame
        # =========================

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

        # =========================
        # Get All Home Visits
        # =========================

        home_visits = self.home_visit_service.home_visit_dao.display_all()

        for visit in home_visits:

            visit_frame = ctk.CTkFrame(
                self.scroll_frame
            )
            visit_frame.pack(
                padx=20,
                pady=10,
                fill="x"
            )

            visit_label = ctk.CTkLabel(
                visit_frame,
                text="Visit ID: " + str(visit.visit_id),
                font=("Arial", 18, "bold")
            )
            visit_label.pack(pady=5)

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
            notes_label.pack(pady=3)

        # =========================
        # Back Button
        # =========================

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back to Dashboard",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=15)

    # =========================
    # Back to Admin Dashboard
    # =========================

    def back_to_dashboard(self):

        from ui.admin.admin_dashboard import AdminDashboard

        AdminDashboard(self.window)

