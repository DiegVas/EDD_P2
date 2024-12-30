import customtkinter as ctk
from tkinter import filedialog
from controllers.data_structure.adyance_list import adjacency_list
from controllers.classes.routes import routes

class CargarRutasWindow(ctk.CTkToplevel):
    def __init__(self, routes_estr, parent, colors):
        super().__init__(parent)
        self.parent = parent
        self.routes_estr: adjacency_list = routes_estr
        self.colors = colors
        self.title("Carga Masiva de Rutas")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Carga Masiva de Rutas", font=ctk.CTkFont(size=20)).pack(pady=20)
        ctk.CTkButton(self, text="Seleccionar Archivo", command=self.select_file, fg_color=self.colors['primary']).pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.process_file(file_path)

    def process_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                data = line.strip().strip(';').split('/')
                if len(data) == 3:
                    origin, destination, time = data
                    time = float(time.replace('%', ''))
                    new_route = routes(origin, destination, time)
                    self.routes_estr.add_vertex(new_route)
        self.routes_estr.print()
        self.parent.update_structure_image()
        self.destroy()