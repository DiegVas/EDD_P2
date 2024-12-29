import customtkinter as ctk
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked
from controllers.classes.client import client

class VerClienteWindow(ctk.CTkToplevel):
    def __init__(self, client_est, parent, colors):
        super().__init__(parent)
        self.parent = parent
        self.client_est: circular_doubly_linked = client_est
        self.colors = colors
        self.title("Ver Cliente")
        self.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Ver Cliente", font=ctk.CTkFont(size=20)).pack(pady=20)

        self.dpi_entry = self.create_input("DPI")
        self.search_button = ctk.CTkButton(self, text="Buscar", command=self.search_client, fg_color=self.colors['primary'])
        self.search_button.pack(pady=10)

        self.name_entry = self.create_input("Nombre", readonly=True)
        self.last_name_entry = self.create_input("Apellido", readonly=True)
        self.gender_entry = self.create_input("Género", readonly=True)
        self.phone_entry = self.create_input("Teléfono", readonly=True)
        self.address_entry = self.create_input("Dirección", readonly=True)

    def create_input(self, placeholder, readonly=False):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=5, padx=20, fill="x")
        ctk.CTkLabel(frame, text=placeholder, width=100, anchor="w").pack(side="left")
        entry = ctk.CTkEntry(frame)
        entry.pack(side="left", fill="x", expand=True)
        if readonly:
            entry.configure(state="readonly")
        return entry

    def search_client(self):
        if not self.dpi_entry.get():
            return
        dpi = int(self.dpi_entry.get())
        client = self.client_est.search(dpi)
        if client:
            self.name_entry.configure(state="normal")
            self.name_entry.delete(0, "end")
            self.name_entry.insert(0, client.name)
            self.name_entry.configure(state="readonly")

            self.last_name_entry.configure(state="normal")
            self.last_name_entry.delete(0, "end")
            self.last_name_entry.insert(0, client.lastName)
            self.last_name_entry.configure(state="readonly")

            self.gender_entry.configure(state="normal")
            self.gender_entry.delete(0, "end")
            self.gender_entry.insert(0, client.gender)
            self.gender_entry.configure(state="readonly")

            self.phone_entry.configure(state="normal")
            self.phone_entry.delete(0, "end")
            self.phone_entry.insert(0, client.phone)
            self.phone_entry.configure(state="readonly")

            self.address_entry.configure(state="normal")
            self.address_entry.delete(0, "end")
            self.address_entry.insert(0, client.address)
            self.address_entry.configure(state="readonly")