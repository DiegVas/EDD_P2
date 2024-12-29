import customtkinter as ctk
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked

class EliminarClienteWindow(ctk.CTkToplevel):
    def __init__(self, client_est, parent, colors):
        super().__init__(parent)
        self.parent = parent
        self.client_est:circular_doubly_linked = client_est
        self.colors = colors
        self.title("Eliminar Cliente")
        self.geometry("300x200")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Eliminar Cliente", font=ctk.CTkFont(size=20)).pack(pady=20)

        self.dpi_entry = self.create_input("DPI")

        ctk.CTkButton(self, text="Eliminar", command=self.delete_client, fg_color=self.colors['primary']).pack(pady=20)

    def create_input(self, placeholder):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=5, padx=20, fill="x")
        ctk.CTkLabel(frame, text=placeholder, width=100, anchor="w").pack(side="left")
        entry = ctk.CTkEntry(frame)
        entry.pack(side="left", fill="x", expand=True)
        return entry

    def delete_client(self):
        dpi = int(self.dpi_entry.get())
        self.client_est.delete(dpi)
        self.parent.update_user_list()
        self.destroy()