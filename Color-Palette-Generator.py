import tkinter as tk
import random

def generate_palette():
    colors = ['#%06X' % random.randint(0, 0xFFFFFF) for _ in range(5)]
    for i, color in enumerate(colors):
        frame = tk.Frame(root, width=100, height=100, bg=color)
        frame.grid(row=1, column=i, padx=5, pady=5)

root = tk.Tk()
root.title("Color Palette Generator")

button_generate = tk.Button(root, text="Generate Palette", command=generate_palette)
button_generate.pack(pady=20)

root.mainloop()
