import tkinter as tk
from datetime import datetime
import random

# Оптимизированная цветовая палитра для маленького дисплея
BG_COLOR = "#0a0a0a"  # глубокий черный
TILE_BG = "#1a1a1a"  # темно-серый
TILE_BORDER = "#00a8ff"  # яркий голубой
TEXT_COLOR = "#e0e0e0"  # светлый серый для текста
ACCENT_COLOR = "#00a8ff"  # акцентный голубой
SECONDARY_TEXT = "#888888"  # второстепенный текст
ACTIVE_COLOR = "#0066cc"  # синий для активного состояния

# Конфигурация для маленького дисплея 340x480
SCREEN_WIDTH = 340
SCREEN_HEIGHT = 480
TILE_FONT = ("Arial", 10)
TITLE_FONT = ("Arial", 12, "bold")
TIME_FONT = ("Arial", 11)
ICON_FONT = ("Arial", 20)
TEMP_FONT = ("Arial", 24, "bold")

# Иконки и настройки плиток
TILE_CONFIG = {
    "Свет": {"icon": "💡", "type": "toggle", "default": "Выкл"},
    "Комнаты": {"icon": "🏠", "type": "info", "value": "4 комн"},
    "Шторы": {"icon": "🪟", "type": "toggle", "default": "Закрыты"},
    "Климат": {"icon": "🌡️", "type": "info", "value": "22°C"},
    "Музыка": {"icon": "🎵", "type": "info", "value": "Выкл"},
    "Полы": {"icon": "🔥", "type": "value", "value": "0°C"},
    "Настройки": {"icon": "⚙️", "type": "info", "value": ""}
}


class SmartHomeApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Умный дом")
        self.root.configure(bg=BG_COLOR)
        self.root.geometry(f"{SCREEN_WIDTH}x{SCREEN_HEIGHT}")
        self.root.resizable(False, False)

        # Центрирование окна
        self.center_window()

        self.device_states = {}
        self.setup_ui()

    def center_window(self):
        """Центрирование окна на экране"""
        self.root.update_idletasks()
        x = (self.root.winfo_screenwidth() - SCREEN_WIDTH) // 2
        y = (self.root.winfo_screenheight() - SCREEN_HEIGHT) // 2
        self.root.geometry(f"+{x}+{y}")

    def setup_ui(self):
        # Верхняя панель с датой и временем
        self.create_top_bar()

        # Основной контейнер
        main_container = tk.Frame(self.root, bg=BG_COLOR)
        main_container.pack(fill="both", expand=True, padx=8, pady=8)

        # Виджет температуры
        self.create_temperature_widget(main_container)

        # Сетка плиток 2x3
        self.create_tile_grid(main_container)

        # Нижняя панель
        self.create_bottom_bar()

        # Горячие клавиши
        self.root.bind("<Escape>", lambda e: self.root.destroy())
        self.root.bind("<F11>", self.toggle_fullscreen)

    def create_top_bar(self):
        top_bar = tk.Frame(self.root, bg=BG_COLOR, height=40)
        top_bar.pack(fill="x", padx=8, pady=(8, 4))

        # Заголовок
        title_label = tk.Label(top_bar, text="УМНЫЙ ДОМ", font=("Arial", 12, "bold"),
                               fg=ACCENT_COLOR, bg=BG_COLOR)
        title_label.pack(side="left")

        # Время и дата
        self.time_label = tk.Label(top_bar, font=TIME_FONT, fg=TEXT_COLOR, bg=BG_COLOR)
        self.time_label.pack(side="right")
        self.update_time()

    def create_temperature_widget(self, parent):
        temp_frame = tk.Frame(parent, bg=TILE_BG, relief="flat", bd=1,
                              highlightbackground=TILE_BORDER, highlightthickness=1)
        temp_frame.pack(fill="x", pady=(0, 8))

        # Внутренний контейнер для центрирования
        inner_frame = tk.Frame(temp_frame, bg=TILE_BG)
        inner_frame.pack(expand=True, fill="both", padx=10, pady=8)

        # Иконка температуры
        temp_icon = tk.Label(inner_frame, text="🌡️", font=("Arial", 16),
                             fg=ACCENT_COLOR, bg=TILE_BG)
        temp_icon.pack(side="left")

        # Температура и город
        temp_info_frame = tk.Frame(inner_frame, bg=TILE_BG)
        temp_info_frame.pack(side="left", padx=(8, 0))

        self.temp_label = tk.Label(temp_info_frame, text=f"{random.randint(17, 20)}°C",
                                   font=TEMP_FONT, fg=TEXT_COLOR, bg=TILE_BG)
        self.temp_label.pack(anchor="w")

        city_label = tk.Label(temp_info_frame, text="Москва", font=("Arial", 9),
                              fg=SECONDARY_TEXT, bg=TILE_BG)
        city_label.pack(anchor="w")

        # Кнопка обновления
        refresh_btn = tk.Button(inner_frame, text="🔄", font=("Arial", 12),
                                bg=TILE_BG, fg=SECONDARY_TEXT, bd=0,
                                command=self.update_temperature)
        refresh_btn.pack(side="right")

    def create_tile_grid(self, parent):
        """Создает сетку плиток 2x3"""
        grid_frame = tk.Frame(parent, bg=BG_COLOR)
        grid_frame.pack(fill="both", expand=True)

        tiles = ["Свет", "Комнаты", "Шторы", "Климат", "Музыка", "Полы"]

        for i, tile_name in enumerate(tiles):
            row = i // 3
            col = i % 3

            if col == 0:
                row_frame = tk.Frame(grid_frame, bg=BG_COLOR)
                row_frame.pack(fill="both", expand=True, pady=2)

            config = TILE_CONFIG[tile_name]
            self.create_compact_tile(row_frame, tile_name, config["type"])

    def create_compact_tile(self, parent, name, tile_type):
        config = TILE_CONFIG[name]

        tile = tk.Frame(parent, bg=TILE_BG, relief="flat", bd=1,
                        highlightbackground=TILE_BORDER, highlightthickness=1,
                        width=100, height=80)
        tile.pack(side="left", expand=True, fill="both", padx=2)
        tile.pack_propagate(False)

        # Иконка
        icon_label = tk.Label(tile, text=config["icon"], font=ICON_FONT,
                              fg=ACCENT_COLOR, bg=TILE_BG)
        icon_label.pack(pady=(8, 2))

        # Название
        name_label = tk.Label(tile, text=name, font=("Arial", 9),
                              fg=TEXT_COLOR, bg=TILE_BG)
        name_label.pack()

        if tile_type == "toggle":
            status_label = tk.Label(tile, text=config["default"], font=("Arial", 8),
                                    fg=SECONDARY_TEXT, bg=TILE_BG)
            status_label.pack()

            # Прозрачная кнопка на всю плитку
            btn = tk.Button(tile, text="", bg=TILE_BG, activebackground=ACTIVE_COLOR,
                            bd=0, highlightthickness=0,
                            command=lambda: self.toggle_device(name, status_label, tile))
            btn.place(x=0, y=0, width=100, height=80)

            self.device_states[name] = {"state": False, "label": status_label, "tile": tile}

        elif tile_type == "value" and name == "Полы":
            self.floor_temp_label = tk.Label(tile, text=config["value"], font=("Arial", 9),
                                             fg=TEXT_COLOR, bg=TILE_BG)
            self.floor_temp_label.pack()

    def create_bottom_bar(self):
        bottom_bar = tk.Frame(self.root, bg=BG_COLOR, height=30)
        bottom_bar.pack(fill="x", padx=8, pady=(4, 8))

        # Кнопка настроек
        settings_btn = tk.Button(bottom_bar, text="⚙️ Настройки", font=("Arial", 9),
                                 bg=TILE_BG, fg=SECONDARY_TEXT, bd=0,
                                 command=self.show_settings)
        settings_btn.pack(side="right")

        # Статус соединения
        status_label = tk.Label(bottom_bar, text="● Онлайн", font=("Arial", 8),
                                fg="#00ff00", bg=BG_COLOR)
        status_label.pack(side="left")

    def toggle_device(self, device_name, label, tile):
        current_state = self.device_states[device_name]["state"]

        if device_name == "Свет":
            if current_state:
                label.config(text="Выкл", fg=SECONDARY_TEXT)
                tile.config(bg=TILE_BG)
            else:
                label.config(text="Вкл", fg="#00ff00")
                tile.config(bg=ACTIVE_COLOR)
        elif device_name == "Шторы":
            if current_state:
                label.config(text="Закрыты", fg=SECONDARY_TEXT)
                tile.config(bg=TILE_BG)
            else:
                label.config(text="Открыты", fg="#00ff00")
                tile.config(bg=ACTIVE_COLOR)

        self.device_states[device_name]["state"] = not current_state

    def update_temperature(self):
        new_temp = random.randint(17, 25)
        self.temp_label.config(text=f"{new_temp}°C")

        # Обновляем температуру теплых полов
        floor_temp = random.randint(0, 5)
        if hasattr(self, 'floor_temp_label'):
            self.floor_temp_label.config(text=f"{floor_temp}°C")

    def update_time(self):
        now = datetime.now()

        # Форматирование даты и времени для маленького экрана
        month_names = ["янв", "фев", "мар", "апр", "мая", "июн",
                       "июл", "авг", "сен", "окт", "ноя", "дек"]
        day_names = ["пн", "вт", "ср", "чт", "пт", "сб", "вс"]

        date_str = f"{now.day} {month_names[now.month - 1]}"
        time_str = now.strftime("%H:%M")
        day_str = day_names[now.weekday()]

        display_text = f"{date_str} {time_str} {day_str}"
        self.time_label.config(text=display_text)

        # Обновляем каждую секунду
        self.root.after(1000, self.update_time)

    def toggle_fullscreen(self, event=None):
        """Переключение полноэкранного режима"""
        current_state = self.root.attributes("-fullscreen")
        self.root.attributes("-fullscreen", not current_state)

    def show_settings(self):
        """Простое окно настроек"""
        settings_win = tk.Toplevel(self.root)
        settings_win.title("Настройки")
        settings_win.geometry("200x150")
        settings_win.configure(bg=BG_COLOR)
        settings_win.resizable(False, False)

        # Центрирование
        settings_win.transient(self.root)
        settings_win.grab_set()

        tk.Label(settings_win, text="Настройки", font=TITLE_FONT,
                 fg=TEXT_COLOR, bg=BG_COLOR).pack(pady=10)

        tk.Button(settings_win, text="Выход", font=TILE_FONT,
                  bg=ACTIVE_COLOR, fg=TEXT_COLOR,
                  command=self.root.destroy).pack(pady=5)

        tk.Button(settings_win, text="Закрыть", font=TILE_FONT,
                  bg=TILE_BG, fg=TEXT_COLOR,
                  command=settings_win.destroy).pack(pady=5)


def main():
    root = tk.Tk()
    app = SmartHomeApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()