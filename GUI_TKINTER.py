import customtkinter as ctk
import cv2
from PIL import Image, ImageTk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_WIDTH = 1600
APP_HEIGHT = 900


class ChairGuardianApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chair Guardian AI")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")

        self.cap = cv2.VideoCapture(0)
        self.current_frame = None

        self.setup_ui()


if __name__ == "__main__":
    app = ChairGuardianApp()
    app.mainloop()
