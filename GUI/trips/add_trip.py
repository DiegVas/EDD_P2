import customtkinter as ctk
from tkinter import messagebox
from controllers.data_structure.adyance_list import adjacency_list
from controllers.classes.trips import trips
from controllers.data_structure.cicular_doubly_linked import circular_doubly_linked
from controllers.data_structure.b_tree import bTree
from controllers.nodes.b_tree_node import BTreeNode
from controllers.data_structure.trip_linked_linked import trip_linked_linked

class AgregarViajeWindow(ctk.CTkToplevel):
    def __init__(self, trips_estr, parent, colors, clients, vehicles, adjacency):
        super().__init__(parent)
        self.parent = parent
        self.trips_estr:trip_linked_linked = trips_estr
        self.colors = colors
        self.clients: circular_doubly_linked = clients
        self.vehicles: bTree = vehicles
        self.adjacency: adjacency_list = adjacency
        self.title("Agregar Viaje")
        self.geometry("400x400")
        self.configure(fg_color=colors['white'])
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Agregar Viaje", font=ctk.CTkFont(size=20, weight="bold")).pack(pady=10)

        # Client ComboBox
        ctk.CTkLabel(self, text="Cliente:", font=ctk.CTkFont(size=14)).pack(pady=5)
        self.client_combobox = ctk.CTkComboBox(self, values=self.get_clients_list())
        self.client_combobox.pack(pady=5)

        # Vehicle ComboBox
        ctk.CTkLabel(self, text="Vehículo:", font=ctk.CTkFont(size=14)).pack(pady=5)
        self.vehicle_combobox = ctk.CTkComboBox(self, values=self.get_vehicles_list())
        self.vehicle_combobox.pack(pady=5)

        # Origin ComboBox
        ctk.CTkLabel(self, text="Origen:", font=ctk.CTkFont(size=14)).pack(pady=5)
        self.origin_combobox = ctk.CTkComboBox(self, values=self.get_nodes_list())
        self.origin_combobox.pack(pady=5)

        # Destination ComboBox
        ctk.CTkLabel(self, text="Destino:", font=ctk.CTkFont(size=14)).pack(pady=5)
        self.destination_combobox = ctk.CTkComboBox(self, values=self.get_nodes_list())
        self.destination_combobox.pack(pady=5)

        # Start Time Entry
        ctk.CTkLabel(self, text="Hora de Inicio:", font=ctk.CTkFont(size=14)).pack(pady=5)
        self.start_time_entry = ctk.CTkEntry(self)
        self.start_time_entry.pack(pady=5)

        # Add Button
        ctk.CTkButton(self, text="Agregar", command=self.add_trip).pack(pady=20)

    def get_clients_list(self):
        clients_list = []
        current = self.clients.head
        if current is not None:
            while True:
                clients_list.append(f"{current.client.dpi} - {current.client.name}")
                current = current.next
                if current == self.clients.head:
                    break
        return clients_list

    def get_vehicles_list(self):
        vehicles_list = []
        def traverse_b_tree(node: BTreeNode):
            if node is not None:
                for vehicle in node.keys:
                    vehicles_list.append(f"{vehicle.plate} - {vehicle.brand}")
                for child in node.children:
                    traverse_b_tree(child)
        traverse_b_tree(self.vehicles.root)
        return vehicles_list

    def get_nodes_list(self):
        nodes_list = []
        current = self.adjacency.vertices.head
        while current is not None:
            nodes_list.append(current.value.value)
            current = current.next
        return nodes_list

    def add_trip(self):
        client = self.client_combobox.get()
        vehicle = self.vehicle_combobox.get()
        origin = self.origin_combobox.get()
        destination = self.destination_combobox.get()
        start_time = self.start_time_entry.get()

        if not client or not vehicle or not origin or not destination or not start_time:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        # Extract client and vehicle objects
        client_dpi = int(client.split(" - ")[0])
        vehicle_plate = vehicle.split(" - ")[0]

        client_obj = self.clients.search(client_dpi)
        vehicle_obj = self.vehicles.search_key(vehicle_plate)

        if not client_obj or not vehicle_obj:
            messagebox.showerror("Error", "Cliente o vehículo no válido")
            return

        # Create and add the trip
        new_trip = trips(origin, destination, start_time, client_obj, vehicle_obj, self.adjacency)
        self.trips_estr.insert(new_trip)
        messagebox.showinfo("Éxito", "Viaje agregado exitosamente")
        self.parent.update_trip_list()
        self.destroy()