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

def plot_nucleotide_proportions(a_count, t_count, g_count, c_count):
    """Plot the proportions of nucleotides in a pie chart."""
    labels = ['A', 'T', 'G', 'C']
    counts = [a_count, t_count, g_count, c_count]
    
    # Create a pie chart
    plt.figure(figsize=(8, 6))
    plt.pie(counts, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Nucleotide Proportions in DNA Sequence')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
    plt.show()

def analyze_dna():
    """Get the DNA sequence from the input and perform analysis."""
    dna_sequence = entry.get().upper().strip()
    
    if not all(nucleotide in 'ATCG' for nucleotide in dna_sequence):
        messagebox.showerror("Invalid Input", "Please enter a valid DNA sequence (A, T, C, G).")
        return

    a_count, t_count, g_count, c_count = count_nucleotides(dna_sequence)

    # Show results in a message box with a detailed explanation
    total_nucleotides = len(dna_sequence)
    proportion_a = (a_count / total_nucleotides) * 100 if total_nucleotides > 0 else 0
    proportion_t = (t_count / total_nucleotides) * 100 if total_nucleotides > 0 else 0
    proportion_g = (g_count / total_nucleotides) * 100 if total_nucleotides > 0 else 0
    proportion_c = (c_count / total_nucleotides) * 100 if total_nucleotides > 0 else 0

    result_message = (
        f"Nucleotide Counts:\n"
        f"A: {a_count}\n"
        f"T: {t_count}\n"
        f"G: {g_count}\n"
        f"C: {c_count}\n\n"
        f"Total Nucleotides: {total_nucleotides}\n\n"
        f"Nucleotide Proportions:\n"
        f"A: {proportion_a:.1f}%\n"
        f"T: {proportion_t:.1f}%\n"
        f"G: {proportion_g:.1f}%\n"
        f"C: {proportion_c:.1f}%\n\n"
        "The pie chart displays the proportion of each nucleotide in the DNA sequence. "
        "A higher percentage of a nucleotide indicates its dominance in the sequence."
    )
    messagebox.showinfo("Nucleotide Frequencies", result_message)

    # Plot the nucleotide proportions
    plot_nucleotide_proportions(a_count, t_count, g_count, c_count)

# Create the main window
root = tk.Tk()
root.title("DNA Nucleotide Proportion Analyzer")

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
