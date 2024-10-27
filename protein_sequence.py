# Dictionary to store molecular weights of amino acids
amino_acid_weights = {
    'A': 89.09,  # Alanine
    'C': 121.15,  # Cysteine
    'D': 133.10,  # Aspartic acid
    'E': 147.13,  # Glutamic acid
    'F': 165.19,  # Phenylalanine
    'G': 75.07,  # Glycine
    'H': 155.16,  # Histidine
    'I': 131.17,  # Isoleucine
    'K': 146.19,  # Lysine
    'L': 131.17,  # Leucine
    'M': 149.21,  # Methionine
    'N': 132.12,  # Asparagine
    'P': 115.13,  # Proline
    'Q': 146.15,  # Glutamine
    'R': 174.20,  # Arginine
    'S': 105.09,  # Serine
    'T': 119.12,  # Threonine
    'V': 117.15,  # Valine
    'W': 204.23,  # Tryptophan
    'Y': 181.19,  # Tyrosine
}

def calculate_molecular_weight(protein_sequence):
    """Calculate the molecular weight of the protein sequence."""
    total_weight = 0.0
    for amino_acid in protein_sequence:
        total_weight += amino_acid_weights.get(amino_acid, 0)  # Default to 0 for unknown amino acids
    return total_weight

def count_amino_acids(protein_sequence):
    """Count the frequency of each amino acid in the protein sequence."""
    amino_acid_count = {}
    for amino_acid in protein_sequence:
        if amino_acid in amino_acid_count:
            amino_acid_count[amino_acid] += 1
        else:
            amino_acid_count[amino_acid] = 1
    return amino_acid_count

def main():
    # Input protein sequence from user
    protein_sequence = input("Enter a protein sequence (using single-letter codes): ").upper()

    # Calculate molecular weight
    molecular_weight = calculate_molecular_weight(protein_sequence)
    print(f"Molecular Weight: {molecular_weight:.2f} Da")

    # Count amino acid frequencies
    amino_acid_count = count_amino_acids(protein_sequence)
    print("Amino Acid Frequencies:")
    for amino_acid, count in amino_acid_count.items():
        print(f"{amino_acid}: {count}")

if __name__ == "__main__":
    main()
