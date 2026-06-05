import customtkinter as ctk
import cv2
from PIL import Image, ImageTk
import threading
import time
import os
import shutil
from tkinter import messagebox

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

APP_WIDTH = 1600
APP_HEIGHT = 900

EVENTS_DIR = "events"


class ChairGuardianApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Chair Guardian AI")
        self.geometry(f"{APP_WIDTH}x{APP_HEIGHT}")

        self.armed = False
        self.alarm_active = False

        self.cap = cv2.VideoCapture(0)

        self.current_frame = None
        self.events = []

        self.bg_subtractor = cv2.createBackgroundSubtractorMOG2()

        self.setup_ui()
        self.update_camera()

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
            self.status_label.configure(text="Status: ARMED", text_color="red")
        else:
            self.arm_btn.configure(text="ARM SYSTEM", fg_color="green")
            self.status_label.configure(text="Status: UNARMED", text_color="gray")

    def update_camera(self):
        ret, frame = self.cap.read()

        if ret:
            self.current_frame = frame

            fg_mask = self.bg_subtractor.apply(frame)
            motion_level = cv2.countNonZero(fg_mask)

            if self.armed and motion_level > 5000:
                self.on_motion_detected()

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            img = Image.fromarray(frame_rgb)
            imgtk = ImageTk.PhotoImage(image=img)

            self.video_label.configure(image=imgtk)
            self.video_label.image = imgtk

        self.after(15, self.update_camera)

    def on_motion_detected(self):
        if not self.armed:
            return

        if self.alarm_active:
            return

        self.alarm_active = True

        # UI ALERT
        self.alert_bar.configure(
            text=" CRIMINAL IDENTIFIED",
            fg_color="red",
            text_color="white"
        )

        event_id = len(self.events) + 1
        event_folder = f"{EVENTS_DIR}/event_{event_id}"
        os.makedirs(event_folder, exist_ok=True)

        if self.current_frame is not None:
            cv2.imwrite(f"{event_folder}/frame.jpg", self.current_frame)

        self.events.append(event_folder)

        self.blink_alarm()

    def blink_alarm(self):
        def run():
            for _ in range(10):
                if not self.alarm_active:
                    break

                self.alert_bar.configure(fg_color="red")
                time.sleep(0.3)

                self.alert_bar.configure(fg_color="darkred")
                time.sleep(0.3)

            self.alert_bar.configure(
                text="SYSTEM ARMED",
                fg_color="gray20",
                text_color="white"
            )

            self.alarm_active = False

        threading.Thread(target=run, daemon=True).start()

    def open_gallery(self):
        win = ctk.CTkToplevel(self)
        win.geometry("1000x700")
        win.title("Event Gallery")

        scroll = ctk.CTkScrollableFrame(win)
        scroll.pack(fill="both", expand=True)

        for i, event in enumerate(self.events):

            card = ctk.CTkFrame(scroll)
            card.pack(pady=10, padx=10, fill="x")

            ctk.CTkLabel(card, text=f"Event {i+1}").pack(side="left", padx=10)

            def make_keep(e=event):
                return lambda: messagebox.showinfo("Saved", f"Kept {e}")

            def make_delete(e=event):
                def delete():
                    if os.path.exists(e):
                        shutil.rmtree(e)
                    self.events.remove(e)
                    win.destroy()
                return delete

            ctk.CTkButton(
                card,
                text="Keep",
                fg_color="green",
                command=make_keep()
            ).pack(side="right", padx=5)

            ctk.CTkButton(
                card,
                text="Delete",
                fg_color="red",
                command=make_delete()
            ).pack(side="right", padx=5)


if __name__ == "__main__":
    os.makedirs(EVENTS_DIR, exist_ok=True)

    app = ChairGuardianApp()
    app.mainloop()
