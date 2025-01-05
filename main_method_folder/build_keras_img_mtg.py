# Builds the keras model we will use to try to predict cards
# I have some variables that are set and rows 10 - 20 are basically just stating these and creating some help for human study later


import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers, models

os.environ['TF_CPP_MIN_LOG_LEVEL'] = '2'
# Directory containing the organized card images
DATA_DIR = './augmented_organized_cards'

# Set the target image dimensions
IMG_HEIGHT, IMG_WIDTH = 680, 488  # Adjust based on your images

# List all subdirectories as class names (each subdirectory is a class)
class_names = sorted(os.listdir(DATA_DIR))
class_to_label = {class_name: idx for idx, class_name in enumerate(class_names)}

# Function to load and preprocess images
# Normalizes data
def load_and_preprocess_image(image_path, target_size=(IMG_HEIGHT, IMG_WIDTH)):
    """Load and preprocess an image."""
    img = load_img(image_path, target_size=target_size)
    img_array = img_to_array(img) / 255.0  # Normalize pixel values
    return img_array

# Prepare the dataset
def prepare_dataset(data_dir):
    """Load images and their labels from the dataset directory."""
    images = []
    labels = []
    for class_name in class_names:
        class_dir = os.path.join(data_dir, class_name)
        if os.path.isdir(class_dir):
            for image_name in os.listdir(class_dir):
                image_path = os.path.join(class_dir, image_name)
                if image_name.lower().endswith(('jpg', 'jpeg', 'png')):
                    images.append(load_and_preprocess_image(image_path))
                    labels.append(class_to_label[class_name])
    return np.array(images), to_categorical(np.array(labels), num_classes=len(class_names))

# Prepares the dataset into training and validation data
images, labels = prepare_dataset(DATA_DIR)
shuffle_idx = np.random.permutation(len(images))
images, labels = images[shuffle_idx], labels[shuffle_idx]

split_idx = int(0.8 * len(images))  # 80% training, 20% validation
train_images, train_labels = images[:split_idx], labels[:split_idx]
val_images, val_labels = images[split_idx:], labels[split_idx:]

# Build the model
# I considered removing dropout of increasing the amount of training data since
# I will in the real life application always have access to all data, but I decided that
# adding more pictures that were augmented was a better final solution.
# My first coding and evaluation was based more on a dataset where I was just having 1 picture per class which was very innaccruate.
model = models.Sequential([
    layers.InputLayer(input_shape=(IMG_HEIGHT, IMG_WIDTH, 3)),  # Input layer for RGB images
    layers.Conv2D(32, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(64, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),
    layers.Conv2D(128, (3, 3), activation='relu', padding='same'),
    layers.MaxPooling2D((2, 2)),
    layers.Flatten(),
    layers.Dense(128, activation='relu'),
    layers.Dropout(0.1),  # Reduced dropout for potential overfitting on small datasets
    layers.Dense(len(class_names), activation='softmax')  # Output layer
])

# Compile the model
# I just got this from chat gpt, I have not researched exactly what the compile means
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
# I use a very small batch size due to an old computer
model.fit(
    train_images, train_labels,
    validation_data=(val_images, val_labels),
    batch_size=10,
    epochs=8
)

# Saves the model and uses this model for evaluation and running keras later
model.save('magic_card_model.keras')
