import tkinter as tk
from tkinter import messagebox, StringVar, OptionMenu
import matplotlib.pyplot as plt

# Sample disease data with symptoms, probabilities, treatments, and medications
disease_data = {
    "Flu": {
        "symptoms": ["fever", "cough", "sore throat", "body aches"],
        "probability": 90,
        "treatment": "Rest, hydration, and over-the-counter pain relievers.",
        "medication": "Oseltamivir (Tamiflu), Acetaminophen (Tylenol), Ibuprofen (Advil)"
    },
    "Cold": {
        "symptoms": ["cough", "runny nose", "sore throat", "sneezing"],
        "probability": 80,
        "treatment": "Rest and hydration.",
        "medication": "Diphenhydramine (Benadryl), Pseudoephedrine (Sudafed)"
    },
    "Strep Throat": {
        "symptoms": ["sore throat", "fever", "swollen lymph nodes"],
        "probability": 85,
        "treatment": "Antibiotics.",
        "medication": "Penicillin, Amoxicillin"
    },
    "COVID-19": {
        "symptoms": ["fever", "cough", "shortness of breath", "loss of taste"],
        "probability": 95,
        "treatment": "Isolation and supportive care.",
        "medication": "Remdesivir, Dexamethasone, supportive therapies"
    },
    "Diabetes": {
        "symptoms": ["increased thirst", "frequent urination", "fatigue"],
        "probability": 75,
        "treatment": "Diet, exercise, and medication.",
        "medication": "Metformin, Insulin"
    },
    "Skin Cancer": {
        "symptoms": ["mole changes", "skin growths", "non-healing sores"],
        "probability": 75,
        "treatment": "Surgery, chemotherapy, and radiation therapy.",
        "medication": "Topical chemotherapy (e.g., 5-fluorouracil), Immunotherapy"
    }
}

def identify_disease(symptoms):
    """Identify diseases based on input symptoms and return their probabilities, treatments, and medications."""
    identified_diseases = {}
    for disease, data in disease_data.items():
        match_count = sum(1 for symptom in symptoms if symptom in data["symptoms"])
        if match_count > 0:
            probability = min(100, match_count * data["probability"] / len(data["symptoms"]))
            identified_diseases[disease] = {
                "probability": probability,
                "treatment": data["treatment"],
                "medication": data["medication"]
            }
    return identified_diseases

def plot_disease_probabilities(disease_probs, chart_type):
    """Plot disease probabilities based on the selected chart type."""
    diseases = list(disease_probs.keys())
    probabilities = [data["probability"] for data in disease_probs.values()]

    plt.figure(figsize=(10, 6))

    if chart_type == "Pie Chart":
        plt.pie(probabilities, labels=diseases, autopct='%1.1f%%', startangle=140)
        plt.title("Disease Probability Distribution")
    elif chart_type == "Bar Chart":
        plt.bar(diseases, probabilities, color='skyblue')
        plt.title("Disease Probability Bar Chart")
        plt.xticks(rotation=45, ha='right')
    elif chart_type == "Line Chart":
        plt.plot(diseases, probabilities, marker='o', linestyle='-')
        plt.title("Disease Probability Line Chart")
    elif chart_type == "Area Chart":
        plt.fill_between(diseases, probabilities, color='lightblue')
        plt.title("Disease Probability Area Chart")
    elif chart_type == "Histogram":
        plt.hist(probabilities, bins=10, color='orange', alpha=0.7)
        plt.title("Disease Probability Histogram")
    elif chart_type == "Scatter Plot":
        plt.scatter(diseases, probabilities, color='red')
        plt.title("Disease Probability Scatter Plot")
    elif chart_type == "Box Plot":
        plt.boxplot(probabilities, vert=False)
        plt.title("Disease Probability Box Plot")
    elif chart_type == "Step Chart":
        plt.step(diseases, probabilities, where='mid')
        plt.title("Disease Probability Step Chart")
    elif chart_type == "Violin Plot":
        plt.violinplot(probabilities)
        plt.title("Disease Probability Violin Plot")
    elif chart_type == "Error Bar Chart":
        plt.bar(diseases, probabilities, yerr=10, capsize=5, color='green', alpha=0.7)
        plt.title("Disease Probability Error Bar Chart")

    plt.ylabel("Probability (%)")
    plt.tight_layout()
    plt.show()

def analyze_symptoms():
    """Analyze input symptoms and display the results."""
    input_symptoms = entry.get().lower().split(',')
    input_symptoms = [symptom.strip() for symptom in input_symptoms]
    
    disease_probs = identify_disease(input_symptoms)

    if disease_probs:
        chart_type = chart_type_var.get()
        plot_disease_probabilities(disease_probs, chart_type)

        result_message = "\n".join([f"{disease}: {prob['probability']:.2f}%\n" 
                                     f"Treatment: {prob['treatment']}\n"
                                     f"Medication: {prob['medication']}" 
                                     for disease, prob in disease_probs.items()])
        messagebox.showinfo("Analysis Result", f"Identified Diseases:\n{result_message}")
    else:
        messagebox.showinfo("Analysis Result", "No diseases identified based on the symptoms.")

# Create the main GUI window
root = tk.Tk()
root.title("Disease Identifier")

# Create input field for symptoms
entry = tk.Entry(root, width=50)
entry.pack(pady=20)
entry.insert(0, "Enter symptoms separated by commas (e.g., fever, cough)")

# Create variable for chart type selection
chart_type_var = StringVar(root)
chart_type_var.set("Pie Chart")  # Default chart type

# Create a dropdown menu for selecting chart type
chart_type_menu = OptionMenu(root, chart_type_var, 
    "Pie Chart", "Bar Chart", "Line Chart", "Area Chart", "Histogram",
    "Scatter Plot", "Box Plot", "Step Chart", "Violin Plot", "Error Bar Chart"
)
chart_type_menu.pack(pady=10)

# Style the dropdown menu
chart_type_menu.config(bg='lightblue', fg='black', font=('Arial', 12))

# Create analyze button
analyze_button = tk.Button(root, text="Analyze Symptoms", command=analyze_symptoms, 
                            bg='blue', fg='white', font=('Arial', 12, 'bold'), 
                            padx=10, pady=5)
analyze_button.pack(pady=20)

# Run the application
root.mainloop()
