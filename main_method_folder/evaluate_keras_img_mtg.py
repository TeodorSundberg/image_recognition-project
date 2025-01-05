import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# Load the saved model
model = tf.keras.models.load_model('magic_card_model.keras')  # Update with your model path

# Define the data directory and class names
data_dir = './organized_magic_cards'  # Replace with your dataset path
class_names = sorted(os.listdir(data_dir))  # Folder names represent class names

# Define image dimensions
img_height, img_width = 680, 488  # Replace with the size expected by your model


# Function to predict a single image
def predict_image(img_path):
    # Load and preprocess the image
    img = image.load_img(img_path, target_size=(img_height, img_width))
    img_array = image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
    img_array /= 255.0  # Normalize pixel values (if required by your model)

    # Make predictions
    predictions = model.predict(img_array)
    predicted_class_index = np.argmax(predictions, axis=-1)[0]  # Get the predicted class index
    predicted_class_name = class_names[predicted_class_index]

    return predicted_class_index, predicted_class_name


# Initialize counters
total_predictions = 0
correct_predictions = 0

# Evaluate all images in the dataset
for class_name in class_names:
    class_folder = os.path.join(data_dir, class_name)
    for img_file in os.listdir(class_folder):
        img_path = os.path.join(class_folder, img_file)
        predicted_index, predicted_name = predict_image(img_path)
        total_predictions += 1  # Increment total predictions count

        # Check if the prediction is correct
        if predicted_name == class_name:
            correct_predictions += 1
            print(f"[Correct] Image: {img_file}")
        else:
            print(f"[Incorrect] Image: {img_file}")

        print(f"True Class: {class_name}")
        print(f"Predicted Class: {predicted_name}\n")

# Print summary
print("Summary:")
print(f"Total Predictions: {total_predictions}")
print(f"Correct Predictions: {correct_predictions}")
print(f"Accuracy: {correct_predictions / total_predictions:.2%}")
