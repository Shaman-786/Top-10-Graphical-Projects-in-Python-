import matplotlib.pyplot as plt

def gc_content(dna_sequence):
    """Calculate GC content of a DNA sequence."""
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    gc_percentage = ((g_count + c_count) / len(dna_sequence)) * 100
    return gc_percentage

def find_motif(dna_sequence, motif):
    """Find all occurrences of a motif in the DNA sequence."""
    positions = []
    start = 0
    while True:
        start = dna_sequence.find(motif, start)
        if start == -1:
            break
        positions.append(start)
        start += 1  # Move to the next position
    return positions

def visualize_sequence(dna_sequence):
    """Visualize the DNA sequence as a bar plot."""
    nucleotide_counts = {nucleotide: dna_sequence.count(nucleotide) for nucleotide in "ACGT"}
    
    plt.bar(nucleotide_counts.keys(), nucleotide_counts.values())
    plt.xlabel('Nucleotides')
    plt.ylabel('Count')
    plt.title('Nucleotide Distribution')
    plt.show()

def main():
    dna_sequence = input("Enter a DNA sequence: ").upper()
    
    # Calculate GC content
    gc_percentage = gc_content(dna_sequence)
    print(f"GC Content: {gc_percentage:.2f}%")
    
    # Prompt to enter a motif
    motif = input("Enter a motif to find: ").upper()  # This is where the prompt is used
    positions = find_motif(dna_sequence, motif)
    if positions:
        print(f"Motif '{motif}' found at positions: {positions}")
    else:
        print(f"Motif '{motif}' not found in the sequence.")
    
    # Visualize sequence
    visualize_sequence(dna_sequence)

if __name__ == "__main__":
    main()
