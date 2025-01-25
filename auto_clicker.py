import tkinter as tk
from tkinter import messagebox
import pyautogui
import time
import threading
import keyboard

class AutoClicker:
    def __init__(self):
        self.running = False
        self.interval_seconds = 0.5
        self.thread = None
        self.num_clicks = 0
        self.cached_interval = 500

    def start_clicking(self, interval_ms):
        if self.running:
            return
        self.running = True
        self.interval_seconds = max(interval_ms / 1000, 0.5)

        def click_loop():
            while self.running:
                pyautogui.click()
                self.num_clicks += 1
                time.sleep(self.interval_seconds)

        self.thread = threading.Thread(target=click_loop, daemon=True)
        self.thread.start()

    def stop_clicking(self):
        self.running = False
        if self.thread and self.thread.is_alive():
            self.thread.join()

    def reset_clicks(self):
        self.num_clicks = 0

    def save_settings(self, interval_ms):
        self.cached_interval = interval_ms

    def load_settings(self):
        return self.cached_interval

def update_status():
    if auto_clicker.running:
        status_label.config(text=f"Status: Clicking | Clicks: {auto_clicker.num_clicks}")
    else:
        status_label.config(text="Status: Stopped")
    root.after(100, update_status)

def save_settings():
    try:
        interval_ms = int(entry_interval.get())
        auto_clicker.save_settings(interval_ms)
        messagebox.showinfo("Success", "Settings saved successfully!")
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid interval (ms)!")

def start_clicking():
    try:
        interval_ms = int(entry_interval.get())
        if interval_ms < 500:
            messagebox.showerror("Error", "Interval must be at least 500ms!")
            return
        auto_clicker.start_clicking(interval_ms)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid interval (ms)!")

def stop_clicking():
    auto_clicker.stop_clicking()

def load_settings():
    interval_ms = auto_clicker.load_settings()
    entry_interval.delete(0, tk.END)
    entry_interval.insert(0, str(interval_ms))

def bind_hotkeys():
    keyboard.add_hotkey("F8", lambda: start_clicking())
    keyboard.add_hotkey("F9", lambda: stop_clicking())

root = tk.Tk()
root.title("Auto Clicker")
root.geometry("300x250")
root.config(bg="#f0f0f0")

auto_clicker = AutoClicker()

label_interval = tk.Label(root, text="Interval (ms):", bg="#f0f0f0")
label_interval.pack(pady=10)

entry_interval = tk.Entry(root)
entry_interval.pack(pady=5)

status_label = tk.Label(root, text="Status: Stopped", bg="#f0f0f0")
status_label.pack(pady=10)

start_button = tk.Button(root, text="Start (F8)", command=start_clicking)
start_button.pack(pady=5)

stop_button = tk.Button(root, text="Stop (F9)", command=stop_clicking)
stop_button.pack(pady=5)

save_button = tk.Button(root, text="Save Settings", command=save_settings)
save_button.pack(pady=5)

bind_hotkeys()
load_settings()
update_status()

root.mainloop()
