import os
import numpy as np
from tensorflow.keras.preprocessing.image import load_img, img_to_array
from tensorflow.keras.utils import to_categorical
from tensorflow.keras import layers, models

# Directory containing the organized card images
DATA_DIR = './organized_magic_cards'

# Set the target image dimensions
IMG_HEIGHT, IMG_WIDTH = 680, 488  # Adjust based on your images

# List all subdirectories as class names (each subdirectory is a class)
class_names = sorted(os.listdir(DATA_DIR))
class_to_label = {class_name: idx for idx, class_name in enumerate(class_names)}

# Function to load and preprocess images
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

# Load dataset
images, labels = prepare_dataset(DATA_DIR)

# Shuffle the dataset
shuffle_idx = np.random.permutation(len(images))
images, labels = images[shuffle_idx], labels[shuffle_idx]

# Split into training and validation sets
split_idx = int(0.8 * len(images))  # 80% training, 20% validation
train_images, train_labels = images[:split_idx], labels[:split_idx]
val_images, val_labels = images[split_idx:], labels[split_idx:]

# Build the model
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
model.compile(
    optimizer='adam',
    loss='categorical_crossentropy',
    metrics=['accuracy']
)

# Train the model
model.fit(
    train_images, train_labels,
    validation_data=(val_images, val_labels),
    batch_size=32,
    epochs=10
)

# Save the model
model.save('magic_card_model.keras')
