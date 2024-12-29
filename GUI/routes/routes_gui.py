import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage
from GUI.routes.load_routes import CargarRutasWindow

class RutasPage(ctk.CTkFrame):
    def __init__(self, routes_estr, parent, colors):
        self.routes_estr = routes_estr
        super().__init__(parent, fg_color=colors['white'])
        self.colors = colors
        self.pack(fill="both", expand=True)
        self.create_widgets()

    def create_widgets(self):
        self.create_action_buttons()
        self.display_structure_image()

    def create_action_buttons(self):
        button_frame = ctk.CTkFrame(self, fg_color="transparent")
        button_frame.pack(pady=20, padx=20, fill="x")

        ctk.CTkButton(
            button_frame,
            text="📁 Carga Masiva",
            fg_color=self.colors['primary'],
            hover_color=self.colors['hover'],
            height=35,
            command=self.open_load_routes_window
        ).pack(side="left", padx=5)

    def open_load_routes_window(self):
        CargarRutasWindow(self.routes_estr, self, self.colors)
        self.update_structure_image()

    def display_structure_image(self):
        self.image_label = ctk.CTkLabel(self, text="")
        self.image_label.pack(pady=20, padx=20, fill="both", expand=True)
        self.update_structure_image()

    def update_structure_image(self):
        image_path = "src/adyance.png"  # Path to your image file
        image = Image.open(image_path)
        ctk_image = CTkImage(light_image=image, dark_image=image, size=(600, 600))
        self.image_label.configure(image=ctk_image)