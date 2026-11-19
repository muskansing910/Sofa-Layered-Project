# 🛋️ Sofa Customizer Management System

## 📌 About the Project

The **Sofa Customizer Management System** is a Python and MySQL-based application developed to simplify and digitize the sofa customization and order management process for an upholstery business.

The application provides a user-friendly frontend where customers can explore different sofa designs and customize their sofas by selecting fabrics, colours, dimensions, and other components according to their preferences.

The backend is developed using Python and follows a **Layered Architecture**, ensuring proper separation of business logic, database operations, and application functionality.

The system helps manage the complete business workflow, starting from customer inquiries and confirmation to home visits and final work orders.

## 🚀 Features

- **Customer Management:** Manage customer registration and customer information.
- **Sofa Design Management:** Browse and manage different sofa types and designs.
- **Sofa Customization:** Customize sofas by selecting fabrics, colours, dimensions, foam, armrests, legs, and seating capacity.
- **Inquiry Management:** Create, view, and manage customer inquiries.
- **Home Visit Management:** Schedule and track home visits for final measurements and discussions.
- **Work Order Management:** Manage and track sofa-making orders.
- **Feedback Management:** Collect and manage customer feedback.
- **Reports:** Generate customer inquiry reports and monitor business activities.
- **Authentication:** Secure login and password hashing.

## 🏗️ Project Architecture

The backend follows a layered architecture:

1. **Model Layer:** Defines the application's data models and entities.
2. **DAO Layer:** Handles database operations such as INSERT, SELECT, UPDATE, and DELETE.
3. **Service Layer:** Contains business logic and validation.
4. **Presentation Layer:** Provides the user interface and handles user interactions.
5. **Database Layer:** Stores and manages application data using MySQL.

## 🔄 Business Workflow

Customer Inquiry → Inquiry Confirmation → Home Visit → Work Order → Feedback

## 🛠️ Technologies Used

- Python
- MySQL
- HTML5
- CSS3
- bcrypt for password hashing

## 🎯 Project Objective

The main objective is to reduce manual work in the upholstery business, improve customer experience, organize sofa customization requests, and manage the complete sofa-making process efficiently.

## 📚 Learning Outcomes

- Understanding layered architecture.
- Implementing CRUD operations.
- Working with Python and MySQL integration.
- Database design and relationship management.
- Implementing business logic using service and DAO layers.
- Developing frontend interfaces.
- Managing real-world business workflows.
