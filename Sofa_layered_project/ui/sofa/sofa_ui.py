import customtkinter as ctk
from PIL import Image
import os

from service.sofa_design_service import SofaDesignService


class SofaUI:

    def __init__(self, window, customer_id, customer_name):
        self.window = window
        self.customer_id = customer_id
        self.customer_name = customer_name

        self.sofa_service = SofaDesignService()

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # =========================
        # TITLE
        # =========================

        self.title_label = ctk.CTkLabel(
            self.window,
            text="SOFA DESIGNS",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(pady=(20, 10))

        # =========================
        # BACK BUTTON
        # =========================

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back to Dashboard",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )

        self.back_button.pack(pady=10)

        # =========================
        # SCROLLABLE AREA
        # =========================

        self.scroll_frame = ctk.CTkScrollableFrame(
            self.window,
            width=850,
            height=500
        )

        self.scroll_frame.pack(
            padx=20,
            pady=10,
            fill="both",
            expand=True
        )

        # Keep image objects alive
        self.image_list = []

        # =========================
        # GET DESIGNS
        # =========================

        designs = self.sofa_service.display_active_designs()

        # =========================
        # DISPLAY DESIGNS
        # =========================

        for design in designs:

            design_frame = ctk.CTkFrame(
                self.scroll_frame
            )

            design_frame.pack(
                padx=20,
                pady=15,
                fill="x"
            )

            # Image path
            image_path = design.image

            if not os.path.exists(image_path):

                image_path = os.path.join(
                    "images",
                    os.path.basename(design.image)
                )

            # Display image
            if os.path.exists(image_path):

                original_image = Image.open(image_path)

                sofa_image = ctk.CTkImage(
                    light_image=original_image,
                    dark_image=original_image,
                    size=(250, 170)
                )

                self.image_list.append(sofa_image)

                image_label = ctk.CTkLabel(
                    design_frame,
                    image=sofa_image,
                    text=""
                )

                image_label.pack(pady=10)

            else:

                image_label = ctk.CTkLabel(
                    design_frame,
                    text="Image not found"
                )

                image_label.pack(pady=10)

            # Design name
            name_label = ctk.CTkLabel(
                design_frame,
                text=design.design_name,
                font=("Arial", 20, "bold")
            )

            name_label.pack(pady=5)

            # Description
            description_label = ctk.CTkLabel(
                design_frame,
                text=design.description,
                font=("Arial", 14)
            )

            description_label.pack(pady=5)

            # Price
            price_label = ctk.CTkLabel(
                design_frame,
                text="Starting Price: ₹" + str(design.starting_price),
                font=("Arial", 16, "bold")
            )

            price_label.pack(pady=(5, 15))


    def back_to_dashboard(self):

        from ui.customer.customer_dashboard import CustomerDashboard

        CustomerDashboard(
            self.window,
            self.customer_id,
            self.customer_name
        )