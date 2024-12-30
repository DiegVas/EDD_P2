import customtkinter as ctk
from tkinter import messagebox

from customtkinter import CTkImage

from controllers.data_structure.trip_linked_linked import trip_linked_linked
from PIL import Image
class TopOptionsPage(ctk.CTkFrame):
    def __init__(self, parent, colors, routes_estr):
        super().__init__(parent, fg_color=colors['white'])
        self.colors = colors
        self.routes_estr: trip_linked_linked = routes_estr
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.create_action_buttons()

    def create_action_buttons(self):
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20, padx=20, fill="both", expand=True)

        buttons = [
            ("Top Viajes", "Top 5 de viajes más largos (por número de destinos)", "🗺", self.get_sorted_trips_by_stops),
            ("Top Ganancia", "Top 5 de viajes más caros (por tiempo)", "💰", self.get_sorted_trips_by_distance),
            ("Top Clientes", "Top 5 de clientes con mayor cantidad de viajes", "👥", "self.show_top_clientes"),
            ("Top Vehículos", "Top 5 de vehículos con mayor cantidad de viajes", "🚘", "self.show_top_vehiculos"),
            ("Mostrar ruta", "Mostrar la ruta del viaje", "📍", self.show_route)
        ]

        for i, (title, description, icon, command) in enumerate(buttons):
            frame = ctk.CTkFrame(button_frame, fg_color=self.colors['light_gray'], corner_radius=10)
            frame.grid(row=i // 2, column=i % 2, padx=10, pady=10, sticky="nsew")

            ctk.CTkLabel(frame, text=icon, font=ctk.CTkFont(size=30), text_color=self.colors['primary']).pack(pady=10)
            ctk.CTkLabel(frame, text=title, font=ctk.CTkFont(size=18, weight="bold"),
                         text_color=self.colors['primary']).pack(pady=5)
            ctk.CTkLabel(frame, text=description, font=ctk.CTkFont(size=14), text_color=self.colors['text_gray']).pack(
                pady=5)
            ctk.CTkButton(frame, text="Seleccionar", fg_color=self.colors['primary'], hover_color=self.colors['hover'],
                          command=command).pack(pady=10)

    def show_route(self):
        self.open_id_input_window()

    def open_id_input_window(self):
        id_window = ctk.CTkToplevel(self)
        id_window.title("Ingrese ID del viaje")
        id_window.geometry("300x150")

        ctk.CTkLabel(id_window, text="ID del viaje:", font=ctk.CTkFont(size=14)).pack(pady=10)
        id_entry = ctk.CTkEntry(id_window, width=200)
        id_entry.pack(pady=10)

        def on_search():
            trip_id = id_entry.get()
            if trip_id:
                trip = self.routes_estr.search(trip_id)
                if trip:
                    id_window.destroy()
                    trip.generate_graph()
                    self.open_image_window(trip_id)
                else:
                    messagebox.showerror("Error", "ID del viaje no encontrado")

        ctk.CTkButton(id_window, text="Buscar", command=on_search).pack(pady=10)

    def open_image_window(self, trip_id):
        image_window = ctk.CTkToplevel(self)
        image_window.title(f"Ruta del viaje {trip_id}")
        image_window.geometry("600x400")
        image_path = f'src/route_graph_{trip_id}.png'
        try:
            image = Image.open(image_path)
            ctk_image = CTkImage(light_image=image, dark_image=image, size=(600, 600))

            ctk.CTkLabel(image_window, image=ctk_image).pack(pady=20)
        except Exception as e:
            ctk.CTkLabel(image_window, text=f"Error al cargar la imagen: {e}", font=ctk.CTkFont(size=16)).pack(pady=20)

        ctk.CTkLabel(image_window, text=f"Mostrando ruta para el viaje con ID: {trip_id}",
                     font=ctk.CTkFont(size=16)).pack(pady=20)

    def get_sorted_trips_by_distance(self):
        print("Getting sorted trips by distance")
        # Convert linked list to a list
        current = self.routes_estr.head
        all_trips = []
        while current:
            all_trips.append(current.value)
            current = current.next

        # Sort the trips by distance
        sorted_trips = sorted(all_trips, key=lambda trip: trip.distance, reverse=True)

        # Create a new linked list and insert sorted trips
        sorted_trips = sorted_trips[:5]
        sorted_trip_list:trip_linked_linked = trip_linked_linked()
        for trip in sorted_trips:
            sorted_trip_list.insert(trip)

        sorted_trip_list.generate_graph(sorted_trip_list, "sorted_trip_list")
        self.open_image_window_report("sorted_trip_list")

    def get_sorted_trips_by_stops(self):
        current = self.routes_estr.head
        all_trips = []

        while current:
            trip = current.value
            destinations_count = 0
            route_node = trip.route_take.head
            while route_node:
                destinations_count += 1
                route_node = route_node.next

            all_trips.append((trip, destinations_count))
            current = current.next

        # Sort trips by the number of destinations in descending order
        sorted_trips = sorted(all_trips, key=lambda x: x[1], reverse=True)

        # Create a new linked list and insert sorted trips
        sorted_trips = sorted_trips[:5]
        sorted_trip_list = trip_linked_linked()
        for trip, _ in sorted_trips:
            sorted_trip_list.insert(trip)

        sorted_trip_list.generate_graph(sorted_trip_list, "sorted_trip_list_by_stops")
        self.open_image_window_report("sorted_trip_list_by_stops")

    def open_image_window_report(self, trip_id):
        image_window = ctk.CTkToplevel(self)
        image_window.title(f"Ruta del viaje {trip_id}")
        image_window.geometry("600x400")
        image_path = f'src/trip_list{trip_id}.png'
        try:
            image = Image.open(image_path)
            ctk_image = CTkImage(light_image=image, dark_image=image, size=(600, 600))
            image_label = ctk.CTkLabel(image_window, image=ctk_image)
            image_label.image = image  # Keep a reference to avoid garbage collection
            image_label.pack(pady=20)
        except Exception as e:
            ctk.CTkLabel(image_window, text=f"Error al cargar la imagen: {e}", font=ctk.CTkFont(size=16)).pack(pady=20)

        ctk.CTkLabel(image_window, text=f"Mostrando ruta para el viaje con ID: {trip_id}",
                     font=ctk.CTkFont(size=16)).pack(pady=20)