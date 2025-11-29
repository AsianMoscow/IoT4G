import tkinter as tk
import random

# Цвета
BG_COLOR = "#1e1e1e"
TILE_BG = "#2a2a2a"
TILE_BORDER = "#9b30ff"   # неоновая рамка
TEXT_COLOR = "#00bfff"    # синий
BUTTON_BG = "#2a2a2a"
BUTTON_FG = "#00bfff"

# Иконки (можно заменить на изображения PNG)
ICONS = {
    "Свет": "💡",
    "Комнаты": "🛋️",
    "Шторы": "🪟",
    "Климат": "🔥",
    "Музыка": "🎵",
    "Т. полы": "❄️",
    "Настройки": "⚙️"
}

def toggle_light(label):
    if label.cget("text") == "Выключено":
        label.config(text="Включено")
    else:
        label.config(text="Выключено")

def create_tile(parent, name, is_light=False, value=None):
    tile = tk.Frame(parent, bg=TILE_BG, bd=4, relief="solid",
                    highlightbackground=TILE_BORDER, highlightcolor=TILE_BORDER, highlightthickness=3)
    tile.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    icon_label = tk.Label(tile, text=ICONS.get(name, ""), font=("Arial", 30), fg=TEXT_COLOR, bg=TILE_BG)
    icon_label.pack(pady=(20,10))

    if is_light:
        status_label = tk.Label(tile, text="Выключено", font=("Arial", 18), fg=TEXT_COLOR, bg=TILE_BG)
        status_label.pack()
        btn = tk.Button(tile, text=name, font=("Arial", 18), bg=BUTTON_BG, fg=BUTTON_FG,
                        activebackground=TILE_BORDER, command=lambda: toggle_light(status_label))
        btn.pack(pady=10)
    else:
        text_label = tk.Label(tile, text=name, font=("Arial", 18), fg=TEXT_COLOR, bg=TILE_BG)
        text_label.pack()
        if value is not None:
            value_label = tk.Label(tile, text=value, font=("Arial", 18), fg=TEXT_COLOR, bg=TILE_BG)
            value_label.pack(pady=5)

    return tile

def main():
    root = tk.Tk()
    root.title("IoT4G — Панель умного дома")
    root.configure(bg=BG_COLOR)
    root.attributes("-fullscreen", True)

    # Контейнер плиток
    container = tk.Frame(root, bg=BG_COLOR)
    container.pack(expand=True, fill="both", padx=20, pady=20)

    # Верхняя строка: большая температура + плитки
    top_frame = tk.Frame(container, bg=BG_COLOR)
    top_frame.pack(expand=True, fill="both")

    # Большая температура слева
    temp_frame = tk.Frame(top_frame, bg=TILE_BG, bd=4, relief="solid",
                          highlightbackground=TILE_BORDER, highlightcolor=TILE_BORDER, highlightthickness=3)
    temp_frame.pack(side="left", expand=True, fill="both", padx=5, pady=5)

    temp_label = tk.Label(temp_frame, text=f"{random.randint(17,20)}°C", font=("Arial", 50, "bold"),
                          fg=TEXT_COLOR, bg=TILE_BG)
    temp_label.pack(expand=True)

    # Плитки справа
    right_tiles_frame = tk.Frame(top_frame, bg=BG_COLOR)
    right_tiles_frame.pack(side="left", expand=True, fill="both")

    create_tile(right_tiles_frame, "Свет", is_light=True)
    create_tile(right_tiles_frame, "Комнаты")
    create_tile(right_tiles_frame, "Шторы")

    # Нижняя строка плиток
    bottom_frame = tk.Frame(container, bg=BG_COLOR)
    bottom_frame.pack(expand=True, fill="both")

    create_tile(bottom_frame, "Климат")
    create_tile(bottom_frame, "Музыка")
    create_tile(bottom_frame, "Т. полы", value=f"{random.randint(0,5)}°C")
    create_tile(bottom_frame, "Настройки")

    # Выход по ESC
    root.bind("<Escape>", lambda e: root.destroy())

    root.mainloop()

if __name__ == "__main__":
    main()
