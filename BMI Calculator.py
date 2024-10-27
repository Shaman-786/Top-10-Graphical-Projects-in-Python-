import tkinter as tk

def calculate_bmi():
    weight = float(entry_weight.get())
    height = float(entry_height.get()) / 100  # Convert cm to meters
    bmi = weight / (height ** 2)
    label_result.config(text=f"BMI: {bmi:.2f}")

root = tk.Tk()
root.title("BMI Calculator")

tk.Label(root, text="Weight (kg):").pack(pady=10)
entry_weight = tk.Entry(root)
entry_weight.pack()

tk.Label(root, text="Height (cm):").pack(pady=10)
entry_height = tk.Entry(root)
entry_height.pack()

button_calculate = tk.Button(root, text="Calculate BMI", command=calculate_bmi)
button_calculate.pack(pady=20)

label_result = tk.Label(root, text="")
label_result.pack(pady=10)

root.mainloop()
