import customtkinter as ctk
from GUI.trips.add_trip import AgregarViajeWindow
from controllers.data_structure.trip_linked_linked import trip_linked_linked
from controllers.nodes.b_tree_node import BTreeNode
from controllers.nodes.trip_linked_node import trip_linked_node
from GUI.trips.show_data_struct import MostrarEstructuraWindow

class ViajesPage(ctk.CTkFrame):
    def __init__(self, trips_estr, parent, colors, clients, vehicles, adjacency):
        self.trips_estr: trip_linked_linked = trips_estr
        super().__init__(parent, fg_color=colors['white'])
        self.colors = colors
        self.pack(fill="both", expand=True)
        self.create_widgets()

        self.clients = clients
        self.vehicles = vehicles
        self.adjacency = adjacency

    def create_widgets(self):
        self.show_page_content("Viajes")

    def show_page_content(self, page_name):
        self.create_action_buttons()
        self.content_frame = ctk.CTkFrame(self, fg_color=self.colors['light_gray'])
        self.content_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.table_frame = ctk.CTkFrame(self.content_frame, fg_color=self.colors['white'])
        self.table_frame.pack(pady=20, padx=20, fill="both", expand=True)
        self.display_trips()

    def create_action_buttons(self):
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20, padx=20, fill="x")

        buttons = [
            ("➕ Agregar", self.open_add_trip_window),
            ("ℹ️ Mostrar Información", "self.open_view_vehicle_window"),
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

    def open_add_trip_window(self):
        AgregarViajeWindow(self.trips_estr, self, self.colors, self.clients, self.vehicles, self.adjacency)

    def open_show_structure_window(self):
        self.trips_estr.generate_graph()
        MostrarEstructuraWindow(self, self.colors)


    def display_trips(self):
        headers = ["", "ID", "Origen", "Destino", "Hora de Inicio", "Cliente", "Vehículo", "Costo"]
        header_frame = ctk.CTkFrame(self.table_frame, fg_color=self.colors['primary'])
        header_frame.pack(fill="x", padx=5, pady=(0, 5))

        for i, header in enumerate(headers):
            header_frame.grid_columnconfigure(i, weight=1)
            ctk.CTkLabel(
                header_frame,
                text=header,
                font=ctk.CTkFont(size=14, weight="bold"),
                text_color=self.colors['white']
            ).grid(row=0, column=i, padx=10, pady=8, sticky="ew")

        self.table_content = ctk.CTkScrollableFrame(
            self.table_frame,
            fg_color=self.colors['white']
        )
        self.table_content.pack(fill="both", expand=True, padx=5)

        for i in range(8):
            self.table_content.grid_columnconfigure(i, weight=1)

        self.update_trip_list()

    def update_trip_list(self):
        for widget in self.table_content.winfo_children():
            widget.destroy()

        row = 0
        current: trip_linked_node = self.trips_estr.head
        while current is not None:
            trip = current.value
            bg_color = self.colors['light_gray'] if row % 2 == 0 else self.colors['white']

            ctk.CTkLabel(
                self.table_content,
                text="🗺",
                font=ctk.CTkFont(size=30),
                text_color=self.colors['primary'],
            ).grid(row=row, column=0, padx=10, pady=8, sticky="w")

            trip_data = [
                trip.id,
                trip.origin,
                trip.destination,
                trip.start_time,
                trip.client.name,
                trip.vehicle.plate,
                trip.cost_trip
            ]

            columna = 1
            for data in trip_data:
                entry = ctk.CTkEntry(self.table_content, font=ctk.CTkFont(size=16), text_color=self.colors['primary'],
                                     fg_color="white", border_color="white")
                entry.insert(0, data)
                entry.configure(state="readonly")
                entry.grid(row=row, column=columna, padx=10, pady=8, sticky="w")
                columna += 1

            row += 1
            current = current.next