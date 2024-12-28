import customtkinter as ctk
from controllers.classes.client import client
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked

class AgregarClienteWindow(ctk.CTkToplevel):
    def __init__(self, client_est, parent, colors):
        super().__init__(parent)
        self.parent = parent

        # Atributos de la ventana
        self.address_entry = None
        self.phone_entry = None
        self.gender_combobox = None
        self.last_name_entry = None
        self.name_entry = None
        self.dpi_entry = None
        self.client_est:circular_doubly_linked = client_est

        self.colors = colors
        self.title("Agregar Cliente")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Agregar Cliente", font=ctk.CTkFont(size=20)).pack(pady=20)

        self.dpi_entry = self.create_input("DPI", validate="key", validatecommand=(self.register(self.validate_numeric), "%P"))
        self.name_entry = self.create_input("Nombre")
        self.last_name_entry = self.create_input("Apellido")
        self.gender_combobox = self.create_combobox("Género", ["hombre", "mujer"])
        self.phone_entry = self.create_input("Teléfono", validate="key", validatecommand=(self.register(self.validate_numeric), "%P"))
        self.address_entry = self.create_input("Dirección")

        ctk.CTkButton(self, text="Guardar", command=self.save_client, fg_color=self.colors['primary']).pack(pady=20)

    def create_input(self, placeholder, **kwargs):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=5, padx=20, fill="x")
        ctk.CTkLabel(frame, text=placeholder, width=100, anchor="w").pack(side="left")
        entry = ctk.CTkEntry(frame, **kwargs)
        entry.pack(side="left", fill="x", expand=True)
        return entry

    def create_combobox(self, placeholder, values):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=5, padx=20, fill="x")
        ctk.CTkLabel(frame, text=placeholder, width=100, anchor="w").pack(side="left")
        combobox = ctk.CTkComboBox(frame, values=values)
        combobox.pack(side="left", fill="x", expand=True)
        return combobox

    def validate_numeric(self, value_if_allowed):
        if value_if_allowed.isdigit() or value_if_allowed == "":
            return True
        else:
            return False

    def save_client(self):
        name = self.name_entry.get()
        dpi = int(self.dpi_entry.get())
        last_name = self.last_name_entry.get()
        gender = self.gender_combobox.get()
        phone = int(self.phone_entry.get())
        address = self.address_entry.get()

        new_client = client(dpi, name, last_name, gender, phone, address)
        self.client_est.insert(new_client)
        self.parent.update_user_list()
        self.destroy()  # Close the window after saving the client



        # Aquí puedes agregar la lógica para guardar el cliente