import customtkinter as ctk
from GUI.vehicles.add_vehicle import AgregarVehiculoWindow
from GUI.vehicles.modify_vehicle import ModificarVehiculoWindow
from GUI.vehicles.delete_vehicle import EliminarVehiculoWindow
from GUI.vehicles.view_vehicle import VerVehiculoWindow
from GUI.vehicles.import_vehicles import ImportarVehiculosWindow
from GUI.vehicles.show_data_struct import MostrarEstructuraWindow
from controllers.nodes.b_tree_node import BTreeNode
from controllers.data_structure.b_tree import bTree

class VehiculosPage(ctk.CTkFrame):
    def __init__(self, vehicles_estr, parent, colors):
        self.vehicles_estr: bTree = vehicles_estr
        super().__init__(parent, fg_color=colors['white'])
        self.colors = colors
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.show_page_content("Vehículos")

    def show_page_content(self, page_name):
        self.create_action_buttons()
        self.content_frame = ctk.CTkFrame(self, fg_color=self.colors['light_gray'])
        self.content_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.display_vehicles()

    def create_action_buttons(self):
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20, padx=20, fill="x")

        buttons = [
            ("➕ Agregar", self.open_add_vehicle_window),
            ("📁 Importar", self.open_import_vehicle_window),
            ("✏️ Modificar", self.open_modify_vehicle_window),
            ("🗑️ Eliminar", self.open_delete_vehicle_window),
            ("ℹ️ Mostrar Información", self.open_view_vehicle_window),
            ("📊 Mostrar Estructura", self.open_show_structure_window)
        ]

        for text, command in buttons:
            ctk.CTkButton(
                button_frame,
                text=text,
                fg_color=self.colors['primary'],
                hover_color=self.colors['hover'],
                height=35,
                command=command if callable(command) else None
            ).pack(side="left", padx=5)

    def open_add_vehicle_window(self):
        pass
        AgregarVehiculoWindow(self.vehicles_estr, self, self.colors)

    def open_delete_vehicle_window(self):
        pass
        EliminarVehiculoWindow(self.vehicles_estr, self, self.colors)

    def open_modify_vehicle_window(self):
        pass
        ModificarVehiculoWindow(self.vehicles_estr, self, self.colors)

    def open_show_structure_window(self):
        self.vehicles_estr.render_b_tree()
        MostrarEstructuraWindow(self, self.colors)

    def open_view_vehicle_window(self):
        pass
        VerVehiculoWindow(self.vehicles_estr, self, self.colors)

    def open_import_vehicle_window(self):
        pass
        ImportarVehiculosWindow(self.vehicles_estr, self, self.colors)

    def display_vehicles(self):
        # Frame principal para la tabla
        self.table_frame = ctk.CTkFrame(self.content_frame, fg_color=self.colors['white'])
        self.table_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Crear encabezados de la tabla
        headers = ["", "Placa", "Marca", "Modelo", "Año", "Precio"]
        header_frame = ctk.CTkFrame(self.table_frame, fg_color=self.colors['primary'])
        header_frame.pack(fill="x", padx=5, pady=(0, 5))

        # Configurar el peso de las columnas
        for i, header in enumerate(headers):
            header_frame.grid_columnconfigure(i, weight=1)
            ctk.CTkLabel(
                header_frame,
                text=header,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=self.colors['white']
            ).grid(row=0, column=i, padx=10, pady=8, sticky="ew")

        # Frame para el contenido de la tabla con scroll
        self.table_content = ctk.CTkScrollableFrame(
            self.table_frame,
            fg_color=self.colors['white']
        )
        self.table_content.pack(fill="both", expand=True, padx=5)

        # Configurar el peso de las columnas en el contenido
        for i in range(6):
            self.table_content.grid_columnconfigure(i, weight=1)

        self.update_vehicle_list()

    def update_vehicle_list(self):
        # Limpiar tabla existente
        for widget in self.table_content.winfo_children():
            widget.destroy()

        def traverse_b_tree(node: BTreeNode, row: int):
            if node is not None:
                for i, vehicle in enumerate(node.keys):
                    # Alternar colores de fondo para las filas
                    bg_color = self.colors['light_gray'] if row % 2 == 0 else self.colors['white']

                    # Icono de vehículo
                    ctk.CTkLabel(
                        self.table_content,
                        text="🚘",
                        font=ctk.CTkFont(size=30),
                        text_color=self.colors['primary'],
                    ).grid(row=row, column=0, padx=10, pady=8, sticky="w")

                    vehicle_data = [
                        vehicle.plate,
                        vehicle.brand,
                        vehicle.model,
                        vehicle.year,
                        vehicle.price
                    ]

                    columna = 1
                    for data in vehicle_data:
                        entry = ctk.CTkEntry(self.table_content, font=ctk.CTkFont(size=16), text_color=self.colors['primary'], fg_color="white", border_color="white")
                        entry.insert(0, data)
                        entry.configure(state="readonly")  # Hacer el texto solo lectura
                        entry.grid(row=row, column=columna, padx=10, pady=8, sticky="w")
                        columna += 1

                    row += 1

                for child in node.children:
                    row = traverse_b_tree(child, row)

            return row

        traverse_b_tree(self.vehicles_estr.root, 0)