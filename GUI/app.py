import customtkinter as ctk
from GUI.client.client_gui import ClientesPage
from GUI.vehicles.vehicle_gui import VehiculosPage
from GUI.routes.routes_gui import RutasPage
from GUI.trips.trips_gui import ViajesPage
from GUI.Reports.report_gui import TopOptionsPage


class ModernDashboard(ctk.CTk):
    def __init__(self, clients_estr, vehicles_estr, routes_estr, trips_estr):
        super().__init__()
        self.clients_estr = clients_estr
        self.vehicles_estr = vehicles_estr
        self.routes_estr = routes_estr
        self.trips_estr = trips_estr

        self.colors = {
            'primary': '#0052FF',  # Azul brillante
            'white': '#FFFFFF',  # Blanco
            'light_gray': '#F5F6FA',  # Gris muy claro para el fondo
            'text_gray': '#71727A',  # Gris para texto
            'border': '#E8E8E8',  # Gris para bordes
            'hover': '#003ACC',  # Azul oscuro para hover
            'active': '#003ACC'  # Color para el botón activo
        }

        self.title("Llega Rapidito")
        self.geometry("1280x720")

        # Configurar el grid principal
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Variable para rastrear la página actual
        self.current_page = ctk.StringVar(value="Dashboard")

        # Diccionario para almacenar los botones del menú
        self.menu_buttons = {}

        self.setup_ui()

    def setup_ui(self):
        # Sidebar
        self.sidebar = ctk.CTkFrame(self, fg_color=self.colors['primary'], width=250)
        self.sidebar.grid(row=0, column=0, sticky="nsew", rowspan=2)
        self.sidebar.grid_propagate(False)

        # Logo con icono
        logo_frame = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        logo_frame.pack(pady=(30, 50), padx=20, anchor="w")

        ctk.CTkLabel(
            logo_frame,
            text="Llega Rapidito",
            font=ctk.CTkFont(size=28, weight="bold"),
            text_color=self.colors['white']
        ).pack(anchor="w")

        # Menú items con iconos
        menu_items = [
            ("Dashboard", "📊"),
            ("Clientes", "👥"),
            ("Vehículos", "🚘"),
            ("Viajes", "🗺"),  # Cambiado a un emoji más compacto
            ("Rutas", "📍"),
            ("Reportes", "📈")
        ]

        # Frame para los botones del menú
        menu_container = ctk.CTkFrame(self.sidebar, fg_color="transparent")
        menu_container.pack(fill="x", padx=20)

        for item, icon in menu_items:
            btn = ctk.CTkButton(
                menu_container,
                text=f"{icon}  {item}",
                font=ctk.CTkFont(size=18, weight="bold"),
                fg_color="transparent",
                text_color=self.colors['white'],
                hover_color=self.colors['hover'],
                anchor="w",
                height=45,
                command=lambda x=item: self.change_page(x)
            )
            btn.pack(pady=5, fill="x")

            # Almacenar el botón en el diccionario
            self.menu_buttons[item] = btn

        # Contenedor principal
        self.main_container = ctk.CTkFrame(self, fg_color=self.colors['light_gray'])
        self.main_container.grid(row=0, column=1, sticky="nsew")
        self.main_container.grid_columnconfigure(0, weight=1)
        self.main_container.grid_rowconfigure(1, weight=1)

        # Header del contenido
        self.header = ctk.CTkFrame(self.main_container, fg_color=self.colors['white'], height=80)
        self.header.grid(row=0, column=0, sticky="ew", padx=20, pady=20)
        self.header.grid_propagate(False)

        # Título dinámico con icono
        self.title_label = ctk.CTkLabel(
            self.header,
            text="📊 Dashboard",
            font=ctk.CTkFont(size=24, weight="bold"),
            text_color=self.colors['primary']
        )
        self.title_label.grid(row=0, column=0, padx=20, pady=20, sticky="w")

        # Contenedor de contenido
        self.content_container = ctk.CTkFrame(self.main_container, fg_color=self.colors['white'])
        self.content_container.grid(row=1, column=0, sticky="nsew", padx=20, pady=(0, 20))

        # Inicializar el contenido del dashboard
        self.show_dashboard_content()

        # Actualizar el botón activo inicial
        self.update_active_button("Dashboard")

    def update_active_button(self, active_page):
        # Actualizar todos los botones
        for page, btn in self.menu_buttons.items():
            if page == active_page:
                btn.configure(fg_color=self.colors['active'])
            else:
                btn.configure(fg_color="transparent")

    def change_page(self, page_name):
        # Diccionario de iconos para cada página
        icons = {
            "Dashboard": "📊",
            "Clientes": "👥",
            "Vehículos": "🚘",
            "Viajes": "🗺",
            "Rutas": "📍",
            "Reportes": "📈"
        }

        self.current_page.set(page_name)
        self.title_label.configure(text=f"{icons[page_name]} {page_name}")
        self.clear_content()

        # Actualizar el botón activo
        self.update_active_button(page_name)

        if page_name == "Dashboard":
            self.show_dashboard_content()
        elif page_name == "Clientes":
            ClientesPage(self.clients_estr,self.content_container, self.colors)
        elif page_name == "Vehículos":
            VehiculosPage(self.vehicles_estr,self.content_container, self.colors)
        elif page_name == "Rutas":
            RutasPage(self.routes_estr, self.content_container, self.colors)
        elif page_name == "Viajes":
            ViajesPage(self.trips_estr, self.content_container, self.colors, self.clients_estr, self.vehicles_estr, self.routes_estr)
        elif page_name == "Reportes":
            TopOptionsPage(self.content_container, self.colors, self.trips_estr)
        else:
            self.show_page_content(page_name)



    def show_dashboard_content(self):
        welcome_label = ctk.CTkLabel(
            self.content_container,
            text="👋 Bienvenido al Sistema de Gestión",
            font=ctk.CTkFont(size=20)
        )
        welcome_label.pack(pady=20)

    def show_page_content(self, page_name):
        self.create_action_buttons()

        content_frame = ctk.CTkFrame(self.content_container, fg_color=self.colors['light_gray'])
        content_frame.pack(pady=20, padx=20, fill="both", expand=True)

        ctk.CTkLabel(
            content_frame,
            text=f"Contenido de {page_name}",
            font=ctk.CTkFont(size=16)
        ).pack(pady=20)

    def clear_content(self):
        for widget in self.content_container.winfo_children():
            widget.destroy()

    def create_action_buttons(self):
        button_frame = ctk.CTkFrame(self.content_container, fg_color="transparent")
        button_frame.pack(pady=20, padx=20, fill="x")

        buttons = [
            ("➕ Agregar", "add"),
            ("✏️ Modificar", "edit"),
            ("🗑️ Eliminar", "delete"),
            ("ℹ️ Mostrar Información", "info"),
            ("📊 Mostrar Estructura", "structure")
        ]

        for text, _ in buttons:
            ctk.CTkButton(
                button_frame,
                text=text,
                fg_color=self.colors['primary'],
                hover_color=self.colors['hover'],
                height=35
            ).pack(side="left", padx=5)
