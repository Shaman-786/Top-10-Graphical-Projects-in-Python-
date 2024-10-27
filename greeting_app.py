import tkinter as tk
from tkinter import messagebox

def greet():
    name = entry.get()  # Get the name from the entry box
    if name:
        messagebox.showinfo("Greeting", f"Hello, {name}!")  # Display greeting
    else:
        messagebox.showwarning("Input Error", "Please enter your name.")  # Warning if empty

# Create the main window
root = tk.Tk()
root.title("Greeting App")
root.geometry("300x200")

# Create and place the label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Create and place the entry box
entry = tk.Entry(root)
entry.pack(pady=10)

# Create and place the button
button = tk.Button(root, text="Greet", command=greet)
button.pack(pady=10)

# Run the application
root.mainloop()
