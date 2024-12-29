import customtkinter as ctk
from controllers.data_structure.b_tree import bTree

class EliminarVehiculoWindow(ctk.CTkToplevel):
    def __init__(self, vehicles_estr, parent, colors):
        super().__init__(parent)
        self.vehicles_estr:bTree = vehicles_estr
        self.parent = parent
        self.colors = colors
        self.title("Eliminar Vehículo")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Eliminar Vehículo", font=ctk.CTkFont(size=20)).pack(pady=20)

        self.entry_plate = self.create_input("Placa")

        ctk.CTkButton(self, text="Eliminar", command=self.delete_vehicle, fg_color=self.colors['primary']).pack(pady=20)

    def create_input(self, placeholder, **kwargs):
        frame = ctk.CTkFrame(self, fg_color="transparent")
        frame.pack(pady=5, padx=20, fill="x")
        ctk.CTkLabel(frame, text=placeholder, width=100, anchor="w").pack(side="left")
        entry = ctk.CTkEntry(frame, **kwargs)
        entry.pack(side="left", fill="x", expand=True)
        return entry

    def delete_vehicle(self):
        plate = self.entry_plate.get()
        if not plate:
            ctk.messagebox.showerror("Error", "La placa no puede estar vacía")
            return

        self.vehicles_estr.delete(self.vehicles_estr.root,plate)
        self.parent.update_vehicle_list()
        self.destroy()