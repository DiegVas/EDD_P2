import customtkinter as ctk
from controllers.classes.vehicles import vehicles
from controllers.data_structure.b_tree import bTree

class ModificarVehiculoWindow(ctk.CTkToplevel):
    def __init__(self, vehicles_estr, parent, colors):
        super().__init__(parent)
        self.parent = parent
        self.vehicles_estr: bTree = vehicles_estr
        self.colors = colors
        self.title("Modificar Vehículo")
        self.geometry("400x500")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Modificar Vehículo", font=ctk.CTkFont(size=20)).pack(pady=20)

        self.entry_plate = self.create_input("Placa")
        self.search_button = ctk.CTkButton(self, text="Buscar", command=self.search_vehicle, fg_color=self.colors['primary'])
        self.search_button.pack(pady=10)

        self.brand_entry = self.create_input("Marca")
        self.model_entry = self.create_input("Modelo")
        self.year_entry = self.create_input("Año")
        self.price_entry = self.create_input("Precio")

        self.save_button = ctk.CTkButton(self, text="Guardar", command=self.save_vehicle, fg_color=self.colors['primary'])
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

    def search_vehicle(self):
        if not self.entry_plate.get():
            return
        plate = self.entry_plate.get()
        vehicle = self.vehicles_estr.search_key(plate)
        if vehicle:
            self.brand_entry.configure(state="normal")
            self.brand_entry.delete(0, "end")
            self.brand_entry.insert(0, vehicle.brand)

            self.model_entry.configure(state="normal")
            self.model_entry.delete(0, "end")
            self.model_entry.insert(0, vehicle.model)

            self.year_entry.configure(state="normal")
            self.year_entry.delete(0, "end")
            self.year_entry.insert(0, vehicle.year)

            self.price_entry.configure(state="normal")
            self.price_entry.delete(0, "end")
            self.price_entry.insert(0, vehicle.price)
        else:
            ctk.messagebox.showerror("Error", "Vehículo no encontrado")

    def save_vehicle(self):
        plate = self.entry_plate.get()
        brand = self.brand_entry.get()
        model = self.model_entry.get()
        year = int(self.year_entry.get())
        price = float(self.price_entry.get())

        updated_vehicle = vehicles(plate, brand, model, year, price)
        self.vehicles_estr.update(updated_vehicle)
        self.parent.update_vehicle_list()
        self.destroy()