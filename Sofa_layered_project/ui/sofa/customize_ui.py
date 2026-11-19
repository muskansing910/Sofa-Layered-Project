import customtkinter as ctk

from service.sofa_type_service import SofaType_service
from service.fabric_service import Fabric_service
from service.color_service import Color_service
from service.foam_type_service import FoamType_service
from service.back_design_service import BackDesign_service
from service.armrest_design_service import ArmrestDesign_service
from service.leg_design_service import LegDesign_service

from model.custom_sofa import CustomSofa
from service.custom_sofa_service import CustomSofa_service
from model.inquiry import Inquiry
from service.inquiry_service import Inquiry_service


class CustomizeUI:

    def __init__(self, window, customer_id, customer_name):

        self.window = window
        self.customer_id = customer_id
        self.customer_name = customer_name

        # =========================
        # Services
        # =========================

        self.sofa_type_service = SofaType_service()
        self.fabric_service = Fabric_service()
        self.color_service = Color_service()
        self.foam_type_service = FoamType_service()
        self.back_design_service = BackDesign_service()
        self.armrest_design_service = ArmrestDesign_service()
        self.leg_design_service = LegDesign_service()
        self.custom_sofa_service = CustomSofa_service()
        self.inquiry_service = Inquiry_service()

        # Clear previous screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # =========================
        # Title
        # =========================

        self.title_label = ctk.CTkLabel(
            self.window,
            text="CUSTOMIZE YOUR SOFA",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(pady=(25, 15))

        # =========================
        # Main Form
        # =========================

        self.form_frame = ctk.CTkScrollableFrame(
            self.window,
            width=700,
            height=500
        )

        self.form_frame.pack(
            padx=30,
            pady=10,
            fill="both",
            expand=True
        )

        # =========================
        # Sofa Type
        # =========================

        self.sofa_type_label = ctk.CTkLabel(
            self.form_frame,
            text="Sofa Type"
        )

        self.sofa_type_label.pack(pady=(15, 5))

        self.sofa_types = (
            self.sofa_type_service.display_active_sofa_types()
        )

        sofa_type_names = []

        for sofa_type in self.sofa_types:
            sofa_type_names.append(sofa_type.type_name)

        self.sofa_type_menu = ctk.CTkOptionMenu(
            self.form_frame,
            values=sofa_type_names,
            width=300
        )

        self.sofa_type_menu.pack(pady=5)

        # =========================
        # Fabric
        # =========================

        self.fabrics = (
            self.fabric_service.display_active_fabrics()
        )

        fabric_names = []

        for fabric in self.fabrics:
            fabric_names.append(fabric.fabric_name)

        self.fabric_label = ctk.CTkLabel(
            self.form_frame,
            text="Fabric"
        )

        self.fabric_label.pack(pady=(15, 5))

        self.fabric_menu = ctk.CTkOptionMenu(
            self.form_frame,
            values=fabric_names,
            width=300
        )

        self.fabric_menu.pack(pady=5)

        # =========================
        # Color
        # =========================

        self.colors = (
            self.color_service.display_active_colors()
        )

        color_names = []

        for color in self.colors:
            color_names.append(color.color_name)

        self.color_label = ctk.CTkLabel(
            self.form_frame,
            text="Color"
        )

        self.color_label.pack(pady=(15, 5))

        self.color_menu = ctk.CTkOptionMenu(
            self.form_frame,
            values=color_names,
            width=300
        )

        self.color_menu.pack(pady=5)

        # =========================
        # Foam Type
        # =========================

        self.foam_types = (
            self.foam_type_service.display_active_foam_types()
        )

        foam_names = []

        for foam in self.foam_types:
            foam_names.append(foam.foam_type_name)

        self.foam_label = ctk.CTkLabel(
            self.form_frame,
            text="Foam Type"
        )

        self.foam_label.pack(pady=(15, 5))

        self.foam_menu = ctk.CTkOptionMenu(
            self.form_frame,
            values=foam_names,
            width=300
        )

        self.foam_menu.pack(pady=5)

        # =========================
        # Back Design
        # =========================

        self.back_designs = (
            self.back_design_service.display_active_back_designs()
        )

        back_design_names = []

        for back_design in self.back_designs:
            back_design_names.append(
                back_design.back_design_name
            )

        self.back_design_label = ctk.CTkLabel(
            self.form_frame,
            text="Back Design"
        )

        self.back_design_label.pack(pady=(15, 5))

        self.back_design_menu = ctk.CTkOptionMenu(
            self.form_frame,
            values=back_design_names,
            width=300
        )

        self.back_design_menu.pack(pady=5)

        # =========================
        # Armrest Design
        # =========================

        self.armrest_designs = (
            self.armrest_design_service.display_active_armrest_designs()
        )

        armrest_design_names = []

        for armrest_design in self.armrest_designs:
            armrest_design_names.append(
                armrest_design.armrest_design_name
            )

        self.armrest_design_label = ctk.CTkLabel(
            self.form_frame,
            text="Armrest Design"
        )

        self.armrest_design_label.pack(pady=(15, 5))

        self.armrest_design_menu = ctk.CTkOptionMenu(
            self.form_frame,
            values=armrest_design_names,
            width=300
        )

        self.armrest_design_menu.pack(pady=5)

        # =========================
        # Leg Design
        # =========================

        self.leg_designs = (
            self.leg_design_service.display_active_leg_designs()
        )

        leg_design_names = []

        for leg_design in self.leg_designs:
            leg_design_names.append(
                leg_design.leg_design_name
            )

        self.leg_design_label = ctk.CTkLabel(
            self.form_frame,
            text="Leg Design"
        )

        self.leg_design_label.pack(pady=(15, 5))

        self.leg_design_menu = ctk.CTkOptionMenu(
            self.form_frame,
            values=leg_design_names,
            width=300
        )

        self.leg_design_menu.pack(pady=5)

        # =========================
        # Length
        # =========================

        self.length_label = ctk.CTkLabel(
            self.form_frame,
            text="Length"
        )

        self.length_label.pack(pady=(15, 5))

        self.length_entry = ctk.CTkEntry(
            self.form_frame,
            width=300,
            placeholder_text="Enter length"
        )

        self.length_entry.pack(pady=5)

        # =========================
        # Width
        # =========================

        self.width_label = ctk.CTkLabel(
            self.form_frame,
            text="Width"
        )

        self.width_label.pack(pady=(15, 5))

        self.width_entry = ctk.CTkEntry(
            self.form_frame,
            width=300,
            placeholder_text="Enter width"
        )

        self.width_entry.pack(pady=5)

        # =========================
        # Height
        # =========================

        self.height_label = ctk.CTkLabel(
            self.form_frame,
            text="Height"
        )

        self.height_label.pack(pady=(15, 5))

        self.height_entry = ctk.CTkEntry(
            self.form_frame,
            width=300,
            placeholder_text="Enter height"
        )

        self.height_entry.pack(pady=5)

        # =========================
        # Message
        # =========================

        self.message_label = ctk.CTkLabel(
            self.form_frame,
            text=""
        )

        self.message_label.pack(pady=5)

        # =========================
        # Create Button
        # =========================

        self.submit_button = ctk.CTkButton(
            self.form_frame,
            text="Create Custom Sofa",
            width=300,
            height=40,
            command=self.create_sofa
        )

        self.submit_button.pack(pady=20)

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

    # =====================================================
    # CREATE CUSTOM SOFA
    # =====================================================

    def create_sofa(self):

        try:

            # =========================
            # Get selected values
            # =========================

            sofa_type_name = self.sofa_type_menu.get()
            fabric_name = self.fabric_menu.get()
            color_name = self.color_menu.get()
            foam_name = self.foam_menu.get()
            back_design_name = self.back_design_menu.get()
            armrest_design_name = self.armrest_design_menu.get()
            leg_design_name = self.leg_design_menu.get()

            # =========================
            # Find Sofa Type ID
            # =========================

            sofa_type_id = None

            for sofa_type in self.sofa_types:

                if sofa_type.type_name == sofa_type_name:

                    sofa_type_id = sofa_type.sofa_type_id

            # =========================
            # Find Fabric ID
            # =========================

            fabric_id = None

            for fabric in self.fabrics:

                if fabric.fabric_name == fabric_name:

                    fabric_id = fabric.fabric_id

            # =========================
            # Find Color ID
            # =========================

            color_id = None

            for color in self.colors:

                if color.color_name == color_name:

                    color_id = color.color_id

            # =========================
            # Find Foam Type ID
            # =========================

            foam_type_id = None

            for foam in self.foam_types:

                if foam.foam_type_name == foam_name:

                    foam_type_id = foam.foam_type_id

            # =========================
            # Find Back Design ID
            # =========================

            back_design_id = None

            for back_design in self.back_designs:

                if back_design.back_design_name == back_design_name:

                    back_design_id = back_design.back_design_id

            # =========================
            # Find Armrest Design ID
            # =========================

            armrest_design_id = None

            for armrest_design in self.armrest_designs:

                if (
                    armrest_design.armrest_design_name
                    == armrest_design_name
                ):

                    armrest_design_id = (
                        armrest_design.armrest_design_id
                    )

            # =========================
            # Find Leg Design ID
            # =========================

            leg_design_id = None

            for leg_design in self.leg_designs:

                if (
                    leg_design.leg_design_name
                    == leg_design_name
                ):

                    leg_design_id = (
                        leg_design.leg_design_id
                    )

            # =========================
            # Get dimensions
            # =========================

            length = self.length_entry.get()
            width = self.width_entry.get()
            height = self.height_entry.get()

            # =========================
            # Temporary values
            # =========================

            design_id = None
            seat_depth = None
            number_of_seats = 3
            custom_requirements = "Customer customized sofa"

            # Temporary ID for testing
            # Generate new Custom Sofa ID
            custom_sofa_id = self.custom_sofa_service.get_next_id()

            # =========================
            # Create CustomSofa object
            # =========================

            custom_sofa = CustomSofa(
                custom_sofa_id,
                self.customer_id,
                sofa_type_id,
                design_id,
                fabric_id,
                color_id,
                back_design_id,
                armrest_design_id,
                leg_design_id,
                foam_type_id,
                length,
                width,
                height,
                seat_depth,
                number_of_seats,
                custom_requirements,
                None
            )

            # =========================
            # Save to database
            # =========================

            self.custom_sofa_service.add_custom_sofa(
                custom_sofa
            )
            # =========================
            # Create Inquiry
            # =========================

# Generate new Inquiry ID
            inquiry_id = self.inquiry_service.get_next_id()
            inquiry = Inquiry(
                inquiry_id,
                self.customer_id,
                custom_sofa_id,
                None,
                None,
                "NEW",
                "Customer customized sofa",
                None,
                None
            )

            self.inquiry_service.add_inquiry(inquiry)
            # =========================
            # Success message
            # =========================

            self.message_label.configure(
                text="Custom sofa saved successfully!"
            )

        except Exception as e:

            self.message_label.configure(
                text="Error: " + str(e)
            )

            print("Customize Sofa Error:", e)

    # =====================================================
    # BACK TO DASHBOARD
    # =====================================================

    def back_to_dashboard(self):

        from ui.customer.customer_dashboard import CustomerDashboard

        CustomerDashboard(
            self.window,
            self.customer_id,
            self.customer_name
        )