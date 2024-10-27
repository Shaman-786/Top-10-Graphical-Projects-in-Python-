import tkinter as tk
from tkinter import messagebox

def calculate_gc_content(dna_sequence):
    """Calculate GC content percentage of the DNA sequence."""
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    total_count = len(dna_sequence)
    gc_content = (g_count + c_count) / total_count * 100 if total_count > 0 else 0
    return gc_content

def count_nucleotides(dna_sequence):
    """Count occurrences of each nucleotide in the DNA sequence."""
    a_count = dna_sequence.count('A')
    t_count = dna_sequence.count('T')
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    return a_count, t_count, g_count, c_count

def analyze_dna():
    """Get the DNA sequence from the input and perform analysis."""
    dna_sequence = entry.get().upper().strip()
    
    if not all(nucleotide in 'ATCG' for nucleotide in dna_sequence):
        messagebox.showerror("Invalid Input", "Please enter a valid DNA sequence (A, T, C, G).")
        return

    gc_content = calculate_gc_content(dna_sequence)
    a_count, t_count, g_count, c_count = count_nucleotides(dna_sequence)

    result = f"GC Content: {gc_content:.2f}%\n"
    result += f"A: {a_count}\nT: {t_count}\nG: {g_count}\nC: {c_count}\n"

    # Show results in a message box
    messagebox.showinfo("Analysis Result", result)

# Create the main window
root = tk.Tk()
root.title("DNA Sequence Analysis Tool")

# Create and place the label and entry for DNA sequence input
label = tk.Label(root, text="Enter a DNA Sequence (A, T, C, G):")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create and place the Analyze button
analyze_button = tk.Button(root, text="Analyze", command=analyze_dna)
analyze_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
