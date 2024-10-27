import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import classification_report, accuracy_score

# Step 1: Load the dataset
# Make sure to place the 'milk_purity.csv' file in the same directory as this script
data = pd.read_csv('milk_purity.csv')  # Ensure the CSV file is in the same directory or provide the full path

# Step 2: Preprocess the data
X = data.iloc[:, :-1]  # Features (all columns except the last)
y = data.iloc[:, -1]   # Target (last column)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Step 3: Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Step 4: Evaluate the model
y_pred = model.predict(X_test)
print(classification_report(y_test, y_pred))
print("Accuracy:", accuracy_score(y_test, y_pred))

# Step 5: Function to predict purity
def predict_purity(sample):
    sample = np.array(sample).reshape(1, -1)  # Reshape the input for prediction
    return model.predict(sample)

# Example usage
if __name__ == "__main__":
    new_sample = [3.5, 3.2, 4.5, 1.025, 6.8]  # Replace with actual feature values
    predicted_purity = predict_purity(new_sample)
    print("Predicted Purity:", predicted_purity)
