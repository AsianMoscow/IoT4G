import tkinter as tk
from tkinter import ttk
import random

# === Цвета и стиль ===
BG_COLOR = "#1e1e1e"
TILE_BG = "#2a2a2a"
TILE_BORDER = "#9b30ff"   # неоновый фиолетовый
TEXT_COLOR = "#00bfff"    # синий
BUTTON_BG = "#3a3a3a"
BUTTON_FG = "#00bfff"

LIGHT_ICON = "💡"
TEMP_ICON = "🌡️"
HUM_ICON = "💧"

def toggle_light(label):
    if label.cget("text") == "Выключено":
        label.config(text="Включено")
    else:
        label.config(text="Выключено")

def create_device_tile(parent, name, value_text, is_button=False):
    """Создает плитку устройства с элементом слева и значением справа"""
    frame = tk.Frame(parent, bg=TILE_BG, bd=4, relief="solid", highlightbackground=TILE_BORDER,
                     highlightcolor=TILE_BORDER, highlightthickness=3)
    frame.pack(fill="x", pady=10, padx=20)

    left_frame = tk.Frame(frame, bg=TILE_BG)
    left_frame.pack(side="left", padx=10, pady=10)

    right_frame = tk.Frame(frame, bg=TILE_BG)
    right_frame.pack(side="right", padx=10, pady=10)

    if is_button:
        # Кнопка переключения света
        status_label = tk.Label(right_frame, text="Выключено", font=("Arial", 18), fg=TEXT_COLOR, bg=TILE_BG)
        status_label.pack()
        btn = tk.Button(left_frame, text=name, font=("Arial", 18), bg=BUTTON_BG, fg=BUTTON_FG,
                        activebackground=TILE_BORDER, command=lambda: toggle_light(status_label))
        btn.pack()
    else:
        # Метка для показателя
        label = tk.Label(left_frame, text=name, font=("Arial", 18), fg=TEXT_COLOR, bg=TILE_BG)
        label.pack()
        value_label = tk.Label(right_frame, text=value_text, font=("Arial", 18), fg=TEXT_COLOR, bg=TILE_BG)
        value_label.pack()

def create_tab(notebook, location_name):
    """Создает вкладку с устройствами"""
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=location_name)

    container = tk.Frame(frame, bg=BG_COLOR)
    container.pack(expand=True, fill="both", pady=20)

    # Пример устройств
    create_device_tile(container, f"{LIGHT_ICON} Свет", "", is_button=True)
    create_device_tile(container, f"{TEMP_ICON} Температура", f"{random.randint(20,25)} °C")
    create_device_tile(container, f"{HUM_ICON} Влажность", f"{random.randint(40,60)} %")

def main():
    root = tk.Tk()
    root.title("IoT4G — Умный дом плитки")
    root.configure(bg=BG_COLOR)
    root.attributes("-fullscreen", True)

    style = ttk.Style()
    style.theme_use("clam")
    style.configure("TNotebook", background=BG_COLOR, borderwidth=0)
    style.configure("TNotebook.Tab", background="#2e2e2e", foreground=TEXT_COLOR, padding=[20,10])
    style.map("TNotebook.Tab", background=[("selected", TILE_BORDER)], foreground=[("selected", BG_COLOR)])

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill="both", padx=20, pady=20)

    # Вкладки локаций
    create_tab(notebook, "Комната")
    create_tab(notebook, "Коридор")
    create_tab(notebook, "Кухня")

    root.bind("<Escape>", lambda e: root.destroy())
    root.mainloop()

if __name__ == "__main__":
    main()
