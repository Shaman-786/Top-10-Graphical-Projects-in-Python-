import cv2
import mediapipe as mp
import numpy as np

# Initialize Mediapipe Face Mesh solution
mp_face_mesh = mp.solutions.face_mesh
face_mesh = mp_face_mesh.FaceMesh()

# Load earring image (ensure it has an alpha channel for transparency)
earring_path = 'earring.png'  # Update this path if necessary
earring = cv2.imread(earring_path, cv2.IMREAD_UNCHANGED)

# Check if the earring image was loaded correctly
if earring is None:
    raise ValueError(f"Error loading earring image from {earring_path}. Please check the file path.")

# Check if the earring image has an alpha channel
if earring.shape[2] != 4:
    raise ValueError("Earring image must have an alpha channel (RGBA). Please use a PNG image.")

# Start webcam capture
cap = cv2.VideoCapture(0)

def overlay_image_alpha(img, img_overlay, pos, alpha_mask):
    """Overlay img_overlay on top of img at the position specified by pos and blend using alpha_mask."""
    x, y = pos

    # Image ranges
    y1, y2 = max(0, y), min(img.shape[0], y + img_overlay.shape[0])
    x1, x2 = max(0, x), min(img.shape[1], x + img_overlay.shape[1])

    # Overlay ranges
    y1o, y2o = max(0, -y), min(img_overlay.shape[0], img.shape[0] - y)
    x1o, x2o = max(0, -x), min(img_overlay.shape[1], img.shape[1] - x)

    # Exit if nothing to overlay
    if y1 >= y2 or x1 >= x2 or y1o >= y2o or x1o >= x2o:
        return

    # Blend overlay within the determined ranges
    img_crop = img[y1:y2, x1:x2]
    img_overlay_crop = img_overlay[y1o:y2o, x1o:x2o]
    alpha = alpha_mask[y1o:y2o, x1o:x2o] / 255.0  # Normalize alpha values

    img_crop[:] = alpha[:, :, np.newaxis] * img_overlay_crop[:, :, :3] + \
                  (1.0 - alpha[:, :, np.newaxis]) * img_crop

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        print("Error capturing frame from webcam.")
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame to detect face landmarks
    results = face_mesh.process(frame_rgb)

    if results.multi_face_landmarks:
        for face_landmarks in results.multi_face_landmarks:
            # Get the coordinates for both earlobes (landmarks 234 for left ear, 454 for right ear)
            left_ear = face_landmarks.landmark[234]
            right_ear = face_landmarks.landmark[454]

            # Convert normalized coordinates to image coordinates
            h, w, _ = frame.shape
            left_ear_pos = (int(left_ear.x * w), int(left_ear.y * h))
            right_ear_pos = (int(right_ear.x * w), int(right_ear.y * h))

            # Resize the earring image to fit the face
            earring_resized = cv2.resize(earring, (50, 50))

            # Overlay earrings on the earlobes
            overlay_image_alpha(frame, earring_resized, left_ear_pos, earring_resized[:, :, 3])
            overlay_image_alpha(frame, earring_resized, right_ear_pos, earring_resized[:, :, 3])

    # Display the result
    cv2.imshow('Earring Placement with Mediapipe', frame)

    if cv2.waitKey(5) & 0xFF == 27:  # Escape key to exit
        break

# Release the webcam and close all windows
cap.release()
cv2.destroyAllWindows()
