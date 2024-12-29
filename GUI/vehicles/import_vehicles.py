import customtkinter as ctk
from tkinter import filedialog
from controllers.classes.vehicles import vehicles
from controllers.data_structure.b_tree import bTree

class ImportarVehiculosWindow(ctk.CTkToplevel):
    def __init__(self, vehicles_estr, parent, colors):
        super().__init__(parent)
        self.parent = parent
        self.vehicles_estr: bTree = vehicles_estr
        self.colors = colors
        self.title("Importar Vehículos")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Importar Vehículos", font=ctk.CTkFont(size=20)).pack(pady=20)
        ctk.CTkButton(self, text="Seleccionar Archivo", command=self.select_file, fg_color=self.colors['primary']).pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.process_file(file_path)

    def process_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().strip(';').split(':')
                if len(data) == 4:
                    plate, brand, year, price = data
                    year = int(year)
                    price = float(price)
                    new_vehicle = vehicles(plate, brand, "", year, price)
                    self.vehicles_estr.insert(new_vehicle)
        self.parent.update_vehicle_list()
        self.destroy()