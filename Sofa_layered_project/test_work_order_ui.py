import customtkinter as ctk

from ui.work_order.work_order_ui import WorkOrderUI


window = ctk.CTk()

window.geometry("1000x700")

WorkOrderUI(
    window,
    1234,
    "Muskan"
)

window.mainloop()