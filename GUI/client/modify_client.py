import customtkinter as ctk
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked
from controllers.classes.client import client

class ModificarClienteWindow(ctk.CTkToplevel):
    def __init__(self, client_est, parent, colors):
        super().__init__(parent)
        self.parent = parent
        self.client_est: circular_doubly_linked = client_est
        self.colors = colors
        self.title("Modificar Cliente")
        self.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Modificar Cliente", font=ctk.CTkFont(size=20)).pack(pady=20)

        self.dpi_entry = self.create_input("DPI")
        self.search_button = ctk.CTkButton(self, text="Buscar", command=self.search_client, fg_color=self.colors['primary'])
        self.search_button.pack(pady=10)

        self.name_entry = self.create_input("Nombre")
        self.last_name_entry = self.create_input("Apellido")
        self.gender_entry = self.create_input("Género")
        self.phone_entry = self.create_input("Teléfono")
        self.address_entry = self.create_input("Dirección")

        self.save_button = ctk.CTkButton(self, text="Guardar", command=self.save_client, fg_color=self.colors['primary'])
        self.save_button.pack(pady=20)

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

            self.last_name_entry.configure(state="normal")
            self.last_name_entry.delete(0, "end")
            self.last_name_entry.insert(0, client.lastName)

            self.gender_entry.configure(state="normal")
            self.gender_entry.delete(0, "end")
            self.gender_entry.insert(0, client.gender)

            self.phone_entry.configure(state="normal")
            self.phone_entry.delete(0, "end")
            self.phone_entry.insert(0, client.phone)

            self.address_entry.configure(state="normal")
            self.address_entry.delete(0, "end")
            self.address_entry.insert(0, client.address)

    def save_client(self):
        dpi = int(self.dpi_entry.get())
        name = self.name_entry.get()
        last_name = self.last_name_entry.get()
        gender = self.gender_entry.get()
        phone = self.phone_entry.get()
        address = self.address_entry.get()

        updated_client = client(dpi, name, last_name, gender, phone, address)
        self.client_est.update(updated_client)
        self.parent.update_user_list()
        self.destroy()