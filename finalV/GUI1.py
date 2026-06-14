import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import threading
import time
import os
import shutil
from tkinter import messagebox
import subprocess
import sys
import systemArmed
from systemArmed import bundle_motion_event, generate_video_from_event, main

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_WIDTH = 500
APP_HEIGHT = 500

EVENTS_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "events")
EVENTS2_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "events2")
TEMP_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "temporary")
SAVE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "saved")


class ChairGuardianApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chair Guardian AI")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")

        self.armed = False
        self.alarm_active = False
        self.detection_thread = None

        self.cap = cv2.VideoCapture(0)

        self.current_frame = None
        self.events = []

        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2()

        self.setup_ui()

    def setup_ui(self):

        self.sidebar = ctk.CTkFrame(self, width=250)
        self.sidebar.pack(side="left", fill="y")

        self.title_label = ctk.CTkLabel(
            self.sidebar,
            text="🪑 Chair Guardian",
            font=("Arial", 22, "bold")
        )
        self.title_label.pack(pady=20)

        self.arm_btn = ctk.CTkButton(
            self.sidebar,
            text="ARM SYSTEM",
            fg_color="green",
            command=self.toggle_arm
        )
        self.arm_btn.pack(pady=10)

        self.status_label = ctk.CTkLabel(
            self.sidebar,
            text="Status: UNARMED",
            text_color="gray",
            font=("Arial", 14)
        )
        self.status_label.pack(pady=10)

        self.view_events_btn = ctk.CTkButton(
            self.sidebar,
            text="View Events",
            command=self.open_gallery
        )
        self.view_events_btn.pack(pady=10)

        self.warning_label = ctk.CTkLabel(
            self.sidebar,
            text="⚠️ Clear all media\nONLY if chair is\nNOT stolen",
            text_color="orange",
            font=("Arial", 10),
            justify="center"
        )
        self.warning_label.pack(pady=10)

        self.clear_media_btn = ctk.CTkButton(
            self.sidebar,
            text="CLEAR ALL MEDIA",
            fg_color="red",
            command=self.clear_all_media
        )
        self.clear_media_btn.pack(pady=10)

        self.main_frame = ctk.CTkFrame(self)
        self.main_frame.pack(side="right", expand=True, fill="both")

        self.video_label = ctk.CTkLabel(self.main_frame, text="")
        self.video_label.pack(expand=True)

        self.alert_bar = ctk.CTkLabel(
            self.main_frame,
            text="SYSTEM READY",
            height=40,
            fg_color="gray20",
            text_color="white",
            font=("Arial", 16, "bold")
        )
        self.alert_bar.pack(fill="x", side="bottom")

    def toggle_arm(self):
        self.armed = not self.armed

        if self.armed:
            self.arm_btn.configure(text="DISARM SYSTEM", fg_color="red")
            self.status_label.configure(text="Status: ARMED\nYou may minimize this window.", text_color="red")
            # Pass directory constants to systemArmed
            systemArmed.TEMP_DIR = TEMP_DIR
            systemArmed.SAVE_DIR = SAVE_DIR
            systemArmed.EVENTS_DIR = EVENTS_DIR
            systemArmed.EVENTS2_DIR = EVENTS2_DIR
            systemArmed.keep_running = True
            self.detection_thread = threading.Thread(target=main, daemon=False)
            self.detection_thread.start()
        else:
            self.arm_btn.configure(text="ARM SYSTEM", fg_color="green")
            self.status_label.configure(text="Status: UNARMED", text_color="gray")
            systemArmed.keep_running = False
            if self.detection_thread:
                self.detection_thread.join(timeout=5)  # Wait up to 5s for thread to finish
            bundle_motion_event()

    def open_gallery(self):
        script_dir = os.path.dirname(os.path.abspath(__file__))
        path = os.path.join(script_dir, "events2")
        os.startfile(path)

    def clear_all_media(self):
        response = messagebox.askyesno(
            "Confirm Clear Media",
            "Are you sure you want to delete all saved media?\n\nOnly proceed if the chair is NOT stolen."
        )
        if response:
            script_dir = os.path.dirname(os.path.abspath(__file__))
            clear_script = os.path.join(script_dir, "clearMedia.py")
            try:
                subprocess.run([sys.executable, clear_script], check=True)
                messagebox.showinfo("Success", "All media cleared successfully.")
            except Exception as e:
                messagebox.showerror("Error", f"Failed to clear media: {str(e)}")

if __name__ == "__main__":
    os.makedirs(EVENTS_DIR, exist_ok=True)
    os.makedirs(EVENTS2_DIR, exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)
    os.makedirs(SAVE_DIR, exist_ok=True)

    app = ChairGuardianApp()
    app.mainloop()
