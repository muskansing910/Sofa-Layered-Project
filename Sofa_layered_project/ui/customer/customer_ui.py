import customtkinter as ctk

from service.customer_service import customer_service
from model.customer import Customer


class CustomerUI:

    def __init__(self, window):

        self.window = window
        self.customer_service = customer_service()

        for widget in self.window.winfo_children():
            widget.destroy()

        self.title_label = ctk.CTkLabel(
            self.window,
            text="CUSTOMER MANAGEMENT",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))

        self.add_button = ctk.CTkButton(
            self.window,
            text="Add Customer",
            width=300,
            height=40,
            command=self.add_customer
        )
        self.add_button.pack(pady=10)

        self.view_button = ctk.CTkButton(
            self.window,
            text="View Customers",
            width=300,
            height=40,
            command=self.view_customers
        )
        self.view_button.pack(pady=10)

        self.search_button = ctk.CTkButton(
            self.window,
            text="Search Customer",
            width=300,
            height=40,
            command=self.search_customer


        )
        self.search_button.pack(pady=10)

        self.update_button = ctk.CTkButton(
            self.window,
            text="Update Customer",
            width=300,
            height=40,
            command=self.update_customer

        )
        self.update_button.pack(pady=10)

        self.delete_button = ctk.CTkButton(
            self.window,
            text="Delete Customer",
            width=300,
            height=40,
            command=self.delete_customer
        )
        self.delete_button.pack(pady=10)

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=30)


    def add_customer(self):

        for widget in self.window.winfo_children():
            widget.destroy()

        self.title_label = ctk.CTkLabel(
            self.window,
            text="ADD CUSTOMER",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))


        self.name_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="Name"
        )
        self.name_entry.pack(pady=8)

        self.phone_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="Phone"
        )
        self.phone_entry.pack(pady=8)

        self.email_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="Email"
        )
        self.email_entry.pack(pady=8)

        self.password_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="Password",
            show="*"
        )
        self.password_entry.pack(pady=8)

        self.address_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="Address"
        )
        self.address_entry.pack(pady=8)

        self.city_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="City"
        )
        self.city_entry.pack(pady=8)

        self.message_label = ctk.CTkLabel(
            self.window,
            text=""
        )
        self.message_label.pack(pady=5)

        self.save_button = ctk.CTkButton(
            self.window,
            text="Save Customer",
            width=300,
            height=40,
            command=self.save_customer
        )
        self.save_button.pack(pady=10)

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=15)


    def save_customer(self):

        name = self.name_entry.get()
        phone = self.phone_entry.get()
        email = self.email_entry.get()
        password = self.password_entry.get()
        address = self.address_entry.get()
        city = self.city_entry.get()

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

        self.customer_service.register_customer(
            customer,
            password
        )

        self.message_label.configure(
            text="Customer added successfully!"
        )


    def view_customers(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.title_label = ctk.CTkLabel(
            self.window,
            text="VIEW CUSTOMERS",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))

        customers = self.customer_service.Display_customers()

        for customer in customers:
            customer_label = ctk.CTkLabel(
                self.window,
                text="ID: " + str(customer.customer_id) +
                    " | Name: " + str(customer.name) +
                    " | Phone: " + str(customer.phone) +
                    " | Email: " + str(customer.email)
            )
            customer_label.pack(pady=5)

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=20)

    def search_customer(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.title_label = ctk.CTkLabel(
            self.window,
            text="SEARCH CUSTOMER",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))

        self.id_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="Enter Customer ID"
        )
        self.id_entry.pack(pady=10)

        self.search_button = ctk.CTkButton(
            self.window,
            text="Search",
            width=300,
            height=40,
            command=self.perform_search
        )
        self.search_button.pack(pady=10)

        self.message_label = ctk.CTkLabel(
            self.window,
            text=""
        )
        self.message_label.pack(pady=10)

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=20)

    def perform_search(self):
        customer_id = self.id_entry.get()

        customer = self.customer_service.search_customer_by_id(
            customer_id
        )

        if customer is not None:
            self.message_label.configure(
                text="ID: " + str(customer.customer_id) +
                    "\nName: " + str(customer.name) +
                    "\nPhone: " + str(customer.phone) +
                    "\nEmail: " + str(customer.email) +
                    "\nAddress: " + str(customer.address) +
                    "\nCity: " + str(customer.city)
            )
        else:
            self.message_label.configure(
                text="Customer not found."
            )

    def update_customer(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.title_label = ctk.CTkLabel(
            self.window,
            text="UPDATE CUSTOMER",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))

        self.id_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="Enter Customer ID"
        )
        self.id_entry.pack(pady=10)

        self.phone_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="Enter New Phone"
        )
        self.phone_entry.pack(pady=10)

        self.update_button = ctk.CTkButton(
            self.window,
            text="Update",
            width=300,
            height=40,
            command=self.perform_update
        )
        self.update_button.pack(pady=10)

        self.message_label = ctk.CTkLabel(
            self.window,
            text=""
        )
        self.message_label.pack(pady=10)

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=20)

    def perform_update(self):
        customer_id = self.id_entry.get()
        new_phone = self.phone_entry.get()

        if customer_id == "" or new_phone == "":
            self.message_label.configure(
                text="Please enter Customer ID and new phone."
            )
            return

        customer = self.customer_service.search_customer_by_id(
            customer_id
        )

        if customer is not None:
            self.customer_service.update_customer(
                customer_id,
                new_phone
            )

            self.message_label.configure(
                text="Customer phone updated successfully!"
            )
        else:
            self.message_label.configure(
                text="Customer not found."
            )

    def delete_customer(self):
        for widget in self.window.winfo_children():
            widget.destroy()

        self.title_label = ctk.CTkLabel(
            self.window,
            text="DELETE CUSTOMER",
            font=("Arial", 30, "bold")
        )
        self.title_label.pack(pady=(30, 20))

        self.id_entry = ctk.CTkEntry(
            self.window,
            width=300,
            placeholder_text="Enter Customer ID"
        )
        self.id_entry.pack(pady=10)

        self.delete_button = ctk.CTkButton(
            self.window,
            text="Delete",
            width=300,
            height=40,
            command=self.perform_delete
        )
        self.delete_button.pack(pady=10)

        self.message_label = ctk.CTkLabel(
            self.window,
            text=""
        )
        self.message_label.pack(pady=10)

        self.back_button = ctk.CTkButton(
            self.window,
            text="← Back",
            width=200,
            height=40,
            command=self.back_to_dashboard
        )
        self.back_button.pack(pady=20)

    def perform_delete(self):
        customer_id = self.id_entry.get()

        if customer_id == "":
            self.message_label.configure(
                text="Please enter Customer ID."
            )
            return

        customer = self.customer_service.search_customer_by_id(
            customer_id
        )

        if customer is not None:
            self.customer_service.delete_customer(customer_id)

            self.message_label.configure(
                text="Customer deleted successfully!"
            )
        else:
            self.message_label.configure(
                text="Customer not found."
            )

    def back_to_dashboard(self):
        from ui.admin.admin_dashboard import AdminDashboard
        AdminDashboard(self.window)