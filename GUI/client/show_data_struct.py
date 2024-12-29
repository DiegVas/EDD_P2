import customtkinter as ctk
from PIL import Image
from customtkinter import CTkImage

class MostrarEstructuraWindow(ctk.CTkToplevel):
    def __init__(self, parent, colors):
        super().__init__(parent)
        self.colors = colors
        self.title("Mostrar Estructura")
        self.geometry("600x600")
        self.create_widgets()

    def create_widgets(self):
        ctk.CTkLabel(self, text="Estructura de Datos", font=ctk.CTkFont(size=20)).pack(pady=20)

        # Load and display the image using CTkImage
        image = Image.open("src/circular_doubly_linked_list.png")
        ctk_image = CTkImage(light_image=image, dark_image=image, size=(600, 600))
        image_label = ctk.CTkLabel(self, image=ctk_image, text="")
        image_label.pack(pady=20)