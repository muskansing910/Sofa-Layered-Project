import customtkinter as ctk
from ui.login.login_ui import LoginUI


window = ctk.CTk()

window.title("Sofa Customizer Management System")

window.geometry("1000x650")

LoginUI(window)

window.mainloop()