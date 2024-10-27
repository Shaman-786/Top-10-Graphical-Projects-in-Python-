import tkinter as tk
import time

def update_time():
    current_time = time.strftime("%H:%M:%S")
    label.config(text=current_time)
    label.after(1000, update_time)  # Update the time every second

root = tk.Tk()
root.title("Digital Clock")

label = tk.Label(root, font=('Arial', 40), fg='black')
label.pack(pady=20)

update_time()  # Start updating the time
root.mainloop()
