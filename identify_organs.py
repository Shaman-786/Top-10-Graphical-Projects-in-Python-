import os
import cv2
import numpy as np
import tensorflow as tf

# Set environment variable to disable oneDNN optimizations
os.environ["TF_ENABLE_ONEDNN_OPTS"] = "0"

# Load pre-trained model (replace with your actual model file path)
model_path = 'E:/Python/models/my_model.h5'  # Update with your actual model path
try:
    model = tf.keras.models.load_model(model_path)
except Exception as e:
    print(f"Error loading the model: {e}")
    exit()

# Define a list of labels that the model can identify (e.g., organs like heart, lungs, liver, etc.)
labels = ['heart', 'lungs', 'liver', 'kidney', 'brain']  # Update with your actual labels

# Load the image
image_path = 'E:/Python/images/my_image.jpg'  # Replace with the path to your image
try:
    image = cv2.imread(image_path)
    if image is None:
        raise FileNotFoundError(f"Image not found at path: {image_path}")
except Exception as e:
    print(f"Error loading the image: {e}")
    exit()

# Resize image to match model input size
image_resized = cv2.resize(image, (224, 224))  
image_array = np.expand_dims(image_resized, axis=0) / 255.0  # Normalize the image

# Perform prediction
try:
    predictions = model.predict(image_array)
    predicted_index = np.argmax(predictions, axis=1)[0]
    predicted_label = labels[predicted_index]
except Exception as e:
    print(f"Error during prediction: {e}")
    exit()

# Display the image with the identified organ name
cv2.putText(image, f'Organ: {predicted_label}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
cv2.imshow('Identified Organ', image)
cv2.waitKey(0)
cv2.destroyAllWindows()
