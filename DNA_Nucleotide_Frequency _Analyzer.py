import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

def count_nucleotides(dna_sequence):
    """Count occurrences of each nucleotide in the DNA sequence."""
    a_count = dna_sequence.count('A')
    t_count = dna_sequence.count('T')
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    return a_count, t_count, g_count, c_count

def plot_nucleotide_frequencies(a_count, t_count, g_count, c_count):
    """Plot the frequencies of nucleotides in a bar chart."""
    nucleotides = ['A', 'T', 'G', 'C']
    counts = [a_count, t_count, g_count, c_count]

    plt.bar(nucleotides, counts, color=['blue', 'orange', 'green', 'red'])
    plt.xlabel('Nucleotides')
    plt.ylabel('Frequency')
    plt.title('Nucleotide Frequency in DNA Sequence')
    plt.ylim(0, max(counts) + 1)
    plt.show()

def analyze_dna():
    """Get the DNA sequence from the input and perform analysis."""
    dna_sequence = entry.get().upper().strip()
    
    if not all(nucleotide in 'ATCG' for nucleotide in dna_sequence):
        messagebox.showerror("Invalid Input", "Please enter a valid DNA sequence (A, T, C, G).")
        return

    a_count, t_count, g_count, c_count = count_nucleotides(dna_sequence)

    # Show results in a message box
    result = f"A: {a_count}\nT: {t_count}\nG: {g_count}\nC: {c_count}\n"
    messagebox.showinfo("Nucleotide Frequencies", result)

    # Plot the nucleotide frequencies
    plot_nucleotide_frequencies(a_count, t_count, g_count, c_count)

# Create the main window
root = tk.Tk()
root.title("DNA Nucleotide Frequency Analyzer")

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
