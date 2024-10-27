import tkinter as tk
import random

quotes = [
    "The best way to predict the future is to invent it.",
    "Life is 10% what happens to us and 90% how we react to it.",
    "Your time is limited, so don't waste it living someone else's life.",
    "The only way to do great work is to love what you do.",
]

def generate_quote():
    quote = random.choice(quotes)
    label_quote.config(text=quote)

root = tk.Tk()
root.title("Random Quote Generator")

label_quote = tk.Label(root, text="", wraplength=300, font=("Arial", 14))
label_quote.pack(pady=20)

button_generate = tk.Button(root, text="Generate Quote", command=generate_quote)
button_generate.pack(pady=20)

root.mainloop()
