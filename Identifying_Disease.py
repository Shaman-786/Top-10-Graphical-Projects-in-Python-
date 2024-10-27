import tkinter as tk
from tkinter import messagebox
import matplotlib.pyplot as plt

# Sample disease data with symptoms and probabilities
disease_data = {
    "Flu": {"symptoms": ["fever", "cough", "sore throat", "body aches"], "probability": 70},
    "Cold": {"symptoms": ["cough", "sore throat", "runny nose"], "probability": 50},
    "COVID-19": {"symptoms": ["fever", "cough", "difficulty breathing", "fatigue"], "probability": 80},
    "Allergy": {"symptoms": ["sneezing", "runny nose", "itchy eyes"], "probability": 60},
    "Migraine": {"symptoms": ["headache", "nausea", "sensitivity to light"], "probability": 40},
}

def identify_disease(input_symptoms):
    """Identify potential diseases based on input symptoms."""
    identified_diseases = {}
    
    for disease, data in disease_data.items():
        match_count = sum(1 for symptom in input_symptoms if symptom in data["symptoms"])
        if match_count > 0:
            identified_diseases[disease] = data["probability"] * match_count / len(data["symptoms"])
    
    return identified_diseases

def plot_disease_probabilities(disease_probs):
    """Plot the probabilities of identified diseases in a pie chart."""
    labels = list(disease_probs.keys())
    probabilities = list(disease_probs.values())

    plt.figure(figsize=(8, 6))
    plt.pie(probabilities, labels=labels, autopct='%1.1f%%', startangle=140)
    plt.title('Probability of Identified Diseases Based on Symptoms')
    plt.axis('equal')  # Equal aspect ratio ensures that pie chart is a circle.
    plt.show()

def analyze_symptoms():
    """Get symptoms from input and perform disease identification."""
    symptoms_input = entry.get().lower().strip().split(",")
    input_symptoms = [symptom.strip() for symptom in symptoms_input]

    if not input_symptoms or any(not symptom for symptom in input_symptoms):
        messagebox.showerror("Invalid Input", "Please enter valid symptoms separated by commas.")
        return

    identified_diseases = identify_disease(input_symptoms)

    if not identified_diseases:
        messagebox.showinfo("Result", "No diseases identified based on the provided symptoms.")
        return

    # Show results in a message box
    result_message = "Identified Diseases and their probabilities:\n"
    for disease, prob in identified_diseases.items():
        result_message += f"{disease}: {prob:.1f}%\n"

    result_message += "\nThe pie chart displays the probabilities of identified diseases based on the symptoms provided."
    messagebox.showinfo("Identified Diseases", result_message)

    # Plot the disease probabilities
    plot_disease_probabilities(identified_diseases)

# Create the main window
root = tk.Tk()
root.title("Disease Identifier")

# Create and place the label and entry for symptom input
label = tk.Label(root, text="Enter Symptoms (comma-separated):")
label.pack(pady=10)

entry = tk.Entry(root, width=50)
entry.pack(pady=10)

# Create and place the Analyze button
analyze_button = tk.Button(root, text="Identify Disease", command=analyze_symptoms)
analyze_button.pack(pady=20)

# Start the GUI event loop
root.mainloop()
    