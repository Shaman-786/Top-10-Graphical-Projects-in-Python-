import tkinter as tk
from tkinter.colorchooser import askcolor

def choose_color():
    color = askcolor()[1]  # Get the color as a hex string
    if color:
        color_display.config(bg=color)

root = tk.Tk()
root.title("Color Picker")

choose_button = tk.Button(root, text="Choose Color", command=choose_color)
choose_button.pack(pady=20)

color_display = tk.Label(root, text="Color Display", width=30, height=5)
color_display.pack(pady=20)

root.mainloop()
