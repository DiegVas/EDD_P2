import customtkinter as ctk
from controllers.classes.vehicles import vehicles

class AgregarVehiculoWindow(ctk.CTkToplevel):
    def __init__(self, vehicles_estr, parent, colors):
        super().__init__(parent)
        self.vehicles_estr = vehicles_estr
        self.parent = parent
        self.colors = colors
        self.title("Agregar Vehículo")
        self.geometry("400x400")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Agregar Vehículo", font=ctk.CTkFont(size=20)).pack(pady=20)

        self.entry_plate = self.create_input("Placa")
        self.entry_brand = self.create_input("Marca")
        self.entry_model = self.create_input("Modelo")
        self.entry_year = self.create_input("Año", validate="key", validatecommand=(self.register(self.validate_numeric), "%P"))
        self.entry_price = self.create_input("Precio", validate="key", validatecommand=(self.register(self.validate_numeric), "%P"))

        ctk.CTkButton(self, text="Agregar", command=self.add_vehicle, fg_color=self.colors['primary']).pack(pady=20)

    def create_input(self, placeholder, **kwargs):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=5, padx=20, fill="x")
        ctk.CTkLabel(frame, text=placeholder, width=100, anchor="w").pack(side="left")
        entry = ctk.CTkEntry(frame, **kwargs)
        entry.pack(side="left", fill="x", expand=True)
        return entry

    def validate_numeric(self, value_if_allowed):
        if value_if_allowed.isdigit() or value_if_allowed == "":
            return True
        else:
            return False

    def add_vehicle(self):
        plate = self.entry_plate.get()
        brand = self.entry_brand.get()
        model = self.entry_model.get()
        year = int(self.entry_year.get())
        price = float(self.entry_price.get())

        new_vehicle = vehicles(plate, brand, model, year, price)
        self.vehicles_estr.insert(new_vehicle)
        self.parent.update_vehicle_list()
        self.destroy()