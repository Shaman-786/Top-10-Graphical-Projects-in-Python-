import tkinter as tk

# Function to update the expression in the input field
def update_expression(value):
    current_text = entry.get()
    entry.delete(0, tk.END)  # Clear the current text
    entry.insert(tk.END, current_text + str(value))  # Append the new value

# Function to evaluate the expression and show the result
def evaluate_expression():
    try:
        result = str(eval(entry.get()))  # Evaluate the expression
        entry.delete(0, tk.END)  # Clear the entry field
        entry.insert(tk.END, result)  # Show the result
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")  # Show an error if evaluation fails

# Function to clear the input field
def clear_expression():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Calculator")

# Create the input field
entry = tk.Entry(root, width=16, font=('Arial', 24), justify='right')
entry.grid(row=0, column=0, columnspan=4)

# Create buttons
buttons = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

# Arrange buttons in a grid layout
row_val = 1
col_val = 0
for button in buttons:
    if button == '=':
        tk.Button(root, text=button, width=5, height=2, command=evaluate_expression).grid(row=row_val, column=col_val)
    elif button == 'C':
        tk.Button(root, text=button, width=5, height=2, command=clear_expression).grid(row=row_val, column=col_val)
    else:
        tk.Button(root, text=button, width=5, height=2, command=lambda value=button: update_expression(value)).grid(row=row_val, column=col_val)

    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

# Start the Tkinter event loop
root.mainloop()
