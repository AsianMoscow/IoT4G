import tkinter as tk


def main():
    root = tk.Tk()
    root.title("IoT4G — Auto Update Test")
    root.geometry("300x200")

    label = tk.Label(root, text="Hello world! 6", font=("Arial", 20))
    label.pack(expand=True)

    root.mainloop()


if __name__ == "__main__":
    main()