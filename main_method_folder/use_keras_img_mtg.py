# uses Keras model once for manual prediction


import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
import os

# Load the saved model (update the path if needed)
model = tf.keras.models.load_model('magic_card_model.keras')  # Use .h5 file or 'keras_model_1' if SavedModel format

# Define the data directory and class names
data_dir = './organized_magic_cards'
class_names = sorted(os.listdir(data_dir))

# Prepare the input image
img_path = './organized_magic_cards/flagstones_of_trokair/031_flagstones_of_trokair.jpg'  # Replace with the path to your image
# take a random one
img_height, img_width = 680, 488  # Replace with the size expected by your model

# Load and preprocess the image
img = image.load_img(img_path, target_size=(img_height, img_width))
img_array = image.img_to_array(img)
img_array = np.expand_dims(img_array, axis=0)  # Add batch dimension
img_array /= 255.0  # Normalize pixel values (if required by your model)

# Make predictions
predictions = model.predict(img_array)
predicted_class_index = np.argmax(predictions, axis=-1)[0]  # Get the predicted class index

# Map the index to the class name
predicted_class_name = class_names[predicted_class_index]

# Print the results
print("Predicted Class Index:", predicted_class_index)
print(img_path)
print("Predicted Class Name:", predicted_class_name)
