import tkinter as tk
from tkinter import ttk

# Для демонстрации случайные значения температуры и влажности
import random

def toggle_light(label):
    current = label.cget("text")
    if current == "Выключено":
        label.config(text="Включено")
    else:
        label.config(text="Выключено")

def create_tab(notebook, name):
    frame = ttk.Frame(notebook)
    notebook.add(frame, text=name)

    # Кнопка переключения света
    light_status = tk.Label(frame, text="Выключено", font=("Arial", 14))
    light_status.pack(pady=10)

    btn_toggle = tk.Button(frame, text="Переключить свет", font=("Arial", 12),
                           command=lambda: toggle_light(light_status))
    btn_toggle.pack(pady=5)

    # Метки для температуры и влажности
    temp_label = tk.Label(frame, text=f"Температура: {random.randint(20, 25)} °C", font=("Arial", 12))
    temp_label.pack(pady=5)

    hum_label = tk.Label(frame, text=f"Влажность: {random.randint(40, 60)}%", font=("Arial", 12))
    hum_label.pack(pady=5)

    return frame

def main():
    root = tk.Tk()
    root.title("IoT4G — Автообновление Тест")
    root.geometry("400x250")

    notebook = ttk.Notebook(root)
    notebook.pack(expand=True, fill='both')

    # Создаем вкладки
    create_tab(notebook, "Комната")
    create_tab(notebook, "Коридор")
    create_tab(notebook, "Кухня")

    root.mainloop()

if __name__ == "__main__":
    main()
