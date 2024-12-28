import customtkinter as ctk
from GUI.client.add_client import AgregarClienteWindow
from controllers.nodes.doubly_linked_node import Node


class ClientesPage(ctk.CTkFrame):
    def __init__(self, clients_ester, parent, colors):
        self.clients_est = clients_ester
        super().__init__(parent, fg_color=colors['white'])
        self.colors = colors
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.show_page_content("Clientes")

    def show_page_content(self, page_name):
        self.create_action_buttons()
        self.content_frame = ctk.CTkFrame(self, fg_color=self.colors['light_gray'])
        self.content_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.display_users()

    def create_action_buttons(self):
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20, padx=20, fill="x")

        buttons = [
            ("➕ Agregar", self.open_add_client_window),
            ("📁 Importar", "import"),
            ("✏️ Modificar", "edit"),
            ("🗑️ Eliminar", "delete"),
            ("ℹ️ Mostrar Información", "info"),
            ("📊 Mostrar Estructura", "structure")
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

    def open_add_client_window(self):
        AgregarClienteWindow(self.clients_est, self, self.colors)

    def display_users(self):
        # Frame principal para la tabla
        self.table_frame = ctk.CTkFrame(self.content_frame, fg_color=self.colors['white'])
        self.table_frame.pack(pady=20, padx=20, fill="both", expand=True)

        # Crear encabezados de la tabla
        headers = ["", "DPI", "Nombre", "Apellido", "Telefono"]
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
        for i in range(5):
            self.table_content.grid_columnconfigure(i, weight=1)

        self.update_user_list()

    def update_user_list(self):
        # Limpiar tabla existente
        for widget in self.table_content.winfo_children():
            widget.destroy()

        current: Node = self.clients_est.head
        row = 0

        while current:
            # Alternar colores de fondo para las filas
            bg_color = self.colors['light_gray'] if row % 2 == 0 else self.colors['white']

            # Icono de usuario
            ctk.CTkLabel(
                self.table_content,
                text="👤",
                font=ctk.CTkFont(size=30),
                text_color=self.colors['primary'],

            ).grid(row=row, column=0, padx=10, pady=8, sticky="w")

            client_data = [
                current.client.dpi,
                current.client.name,
                current.client.lastName,
                current.client.phone,
            ]


            columna:int = 1
            for data in client_data:
                entry = ctk.CTkEntry(self.table_content, font=ctk.CTkFont(size=16), text_color=self.colors['primary'], fg_color="white", border_color="white")
                entry.insert(0, data)
                entry.configure(state="readonly")  # Hacer el texto solo lectura
                entry.grid(row=row, column=columna, padx=10, pady=8, sticky="w")
                columna += 1

            row += 1
            current = current.next
            if current == self.clients_est.head:
                break