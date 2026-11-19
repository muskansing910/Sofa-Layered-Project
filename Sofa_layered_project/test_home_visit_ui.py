import customtkinter as ctk

from ui.home_visit.home_visit_ui import HomeVisitUI


window = ctk.CTk()

window.geometry("1000x700")

HomeVisitUI(
    window,
    1234,
    "Muskan"
)

window.mainloop()
