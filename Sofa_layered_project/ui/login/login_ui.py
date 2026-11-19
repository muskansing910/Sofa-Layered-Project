import customtkinter as ctk
from service.login_service import LoginService
from service.customer_service import customer_service
from model.customer import Customer

class LoginUI:

    def __init__(self, window):
        self.window = window
        self.login_service = LoginService()

        # Clear existing screen
        for widget in self.window.winfo_children():
            widget.destroy()

        # Login title
        self.title_label = ctk.CTkLabel(
            self.window,
            text="SOFA CUSTOMIZER",
            font=("Arial", 30, "bold")
        )

        self.title_label.pack(pady=(80, 10))

        # Subtitle
        self.subtitle_label = ctk.CTkLabel(
            self.window,
            text="Management System",
            font=("Arial", 18)
        )

        self.subtitle_label.pack(pady=5)

        # Login frame
        self.login_frame = ctk.CTkFrame(
            self.window,
            width=400,
            height=350
        )

        self.login_frame.pack(pady=30)

        # Username
        self.username_entry = ctk.CTkEntry(
            self.login_frame,
            width=300,
            height=40,
            placeholder_text="Email"
        )

        self.username_entry.pack(pady=(35, 15))

        # Password
        self.password_entry = ctk.CTkEntry(
            self.login_frame,
            width=300,
            height=40,
            placeholder_text="Password",
            show="*"
        )

        self.password_entry.pack(pady=15)

        # Role selection
        self.role_label = ctk.CTkLabel(
            self.login_frame,
            text="Login as:"
        )

        self.role_label.pack(pady=(10, 5))

        self.role_menu = ctk.CTkOptionMenu(
            self.login_frame,
            values=["Customer", "Admin"],
            width=300
        )

        self.role_menu.pack(pady=5)

        # Login button
        self.login_button = ctk.CTkButton(
            self.login_frame,
            text="Login",
            width=300,
            height=40,
            command=self.login
        )

        self.login_button.pack(pady=20)

        self.register_button = ctk.CTkButton(
            self.login_frame,
            text="New Customer? Register",
            width=300,
            height=40,
            command=self.register_customer
        )

        self.register_button.pack(pady=10)

        # Error message
        self.message_label = ctk.CTkLabel(
            self.login_frame,
            text="",
            text_color="red"
        )

        self.message_label.pack(pady=5)

    def login(self):

        email = self.username_entry.get()
        password = self.password_entry.get()
        role = self.role_menu.get()

        result = self.login_service.login(
            email,
            password,
            role
        )

        if result:

            if role == "Customer":

                customer_id = result[0]
                customer_name = result[1]

                from ui.customer.customer_dashboard import CustomerDashboard

                CustomerDashboard(
                    self.window,
                    customer_id,
                    customer_name
                )

            elif role == "Admin":

                from ui.admin.admin_dashboard import AdminDashboard

                AdminDashboard(self.window)

        else:

            self.message_label.configure(
                text="Invalid email or password"
            )

    def register_customer(self):

        for widget in self.window.winfo_children():
            widget.destroy()

        self.title_label = ctk.CTkLabel(
            self.window,
            text="CUSTOMER REGISTRATION",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(20, 10))

        self.name_entry = ctk.CTkEntry(
            self.window,
            width=300,
            height=35,
            placeholder_text="Name"
        )
        self.name_entry.pack(pady=5)

        self.phone_entry = ctk.CTkEntry(
            self.window,
            width=300,
            height=35,
            placeholder_text="Phone"
        )
        self.phone_entry.pack(pady=5)

        self.email_entry = ctk.CTkEntry(
            self.window,
            width=300,
            height=35,
            placeholder_text="Email"
        )
        self.email_entry.pack(pady=5)

        self.password_entry = ctk.CTkEntry(
            self.window,
            width=300,
            height=35,
            placeholder_text="Password",
            show="*"
        )
        self.password_entry.pack(pady=5)

        self.address_entry = ctk.CTkEntry(
            self.window,
            width=300,
            height=35,
            placeholder_text="Address"
        )
        self.address_entry.pack(pady=5)

        self.city_entry = ctk.CTkEntry(
            self.window,
            width=300,
            height=35,
            placeholder_text="City"
        )
        self.city_entry.pack(pady=5)

        self.registration_message = ctk.CTkLabel(
            self.window,
            text=""
        )
        self.registration_message.pack(pady=3)

        self.save_registration_button = ctk.CTkButton(
            self.window,
            text="Register",
            width=300,
            height=40,
            command=self.save_registration
        )
        self.save_registration_button.pack(pady=5)

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back to Login",
            width=200,
            height=40,
            command=self.back_to_login
        )
        self.back_button.pack(pady=5)

    def save_registration(self):

        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()

        if name == "" or phone == "" or email == "" or password == "":
            self.registration_message.configure(
                text="Please fill all required fields.",
                text_color="red"
            )
            return

        customer = Customer(
            None,
            name,
            phone,
            email,
            None,
            address,
            city,
            None
        )

        try:

            customer_service_obj = customer_service()

            customer_service_obj.register_customer(
                customer,
                password
            )

            self.registration_message.configure(
                text="Registration successful! You can now login.",
                text_color="green"
            )

        except Exception as e:

            self.registration_message.configure(
                text="Registration failed.",
                text_color="red"
            )

            print("Registration Error:", e)

    def back_to_login(self):

        LoginUI(self.window)

