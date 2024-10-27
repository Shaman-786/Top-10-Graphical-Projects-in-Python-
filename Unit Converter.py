import tkinter as tk

def convert():
    value = float(entry_value.get())
    if var.get() == 1:  # Celsius to Fahrenheit
        converted_value = (value * 9/5) + 32
        label_result.config(text=f"Result: {converted_value:.2f} °F")
    else:  # Fahrenheit to Celsius
        converted_value = (value - 32) * 5/9
        label_result.config(text=f"Result: {converted_value:.2f} °C")

root = tk.Tk()
root.title("Unit Converter")

entry_value = tk.Entry(root)
entry_value.pack(pady=10)

var = tk.IntVar()
tk.Radiobutton(root, text="Celsius to Fahrenheit", variable=var, value=1).pack(pady=5)
tk.Radiobutton(root, text="Fahrenheit to Celsius", variable=var, value=2).pack(pady=5)

button_convert = tk.Button(root, text="Convert", command=convert)
button_convert.pack(pady=20)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
