import customtkinter as ctk
from tkinter import filedialog
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked
from controllers.classes.client import client

class ImportarClientesWindow(ctk.CTkToplevel):
    def __init__(self, client_est, parent, colors):
        super().__init__(parent)
        self.parent = parent
        self.client_est: circular_doubly_linked = client_est
        self.colors = colors
        self.title("Importar Clientes")
        self.geometry("400x200")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Importar Clientes", font=ctk.CTkFont(size=20)).pack(pady=20)
        ctk.CTkButton(self, text="Seleccionar Archivo", command=self.select_file, fg_color=self.colors['primary']).pack(pady=20)

    def select_file(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.process_file(file_path)

    def process_file(self, file_path):
        with open(file_path, 'r') as file:
            for line in file:
                # Assuming the file structure is: dpi,name,lastName,gender,phone,address;
                data = line.strip().strip(';').split(',')
                if len(data) == 6:
                    dpi, name, last_name, gender, phone, address = data
                    new_client = client(int(dpi), name.strip(), last_name.strip(), gender.strip(), phone.strip(), address.strip())
                    self.client_est.insert(new_client)
        self.parent.update_user_list()
        self.destroy()