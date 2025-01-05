# Main purpose of the code is to prepare additional augmented pictures
# The additional nr of pictures helps the model come up with a relevant sized data set and further improvements likely would depend on this
# Method on how to improve the test data.


import os
from tqdm import tqdm
import albumentations as A
import cv2

# Creates different angles of the card
# Causes some blur
# Adjusts brightness
def get_augmentations():
    return A.Compose([
        A.HorizontalFlip(p=0.5),
        A.VerticalFlip(p=0.3),
        A.GaussianBlur(blur_limit=(3, 7), p=0.5),
        A.RandomBrightnessContrast(p=0.5),
        A.Rotate(limit=20, p=0.5),
    ])

# Paths
input_dir = "organized_magic_cards"
output_dir = "augmented_organized_cards"
os.makedirs(output_dir, exist_ok=True)

# Get augmentation pipeline
augment = get_augmentations()

# Loop through all card directories and images
for card_dir in tqdm(os.listdir(input_dir)):
    card_dir_path = os.path.join(input_dir, card_dir)
    output_card_dir_path = os.path.join(output_dir, card_dir)

    # Skip if not a directory
    if not os.path.isdir(card_dir_path):
        continue

    # Create corresponding output subdirectory
    os.makedirs(output_card_dir_path, exist_ok=True)

    # Process each image in the subdirectory
    for img_file in os.listdir(card_dir_path):
        img_path = os.path.join(card_dir_path, img_file)

        # Read image
        image = cv2.imread(img_path)
        if image is None:
            print(f"Skipping invalid file: {img_path}")
            continue

        # Save one non-augmented (original) copy
        original_output_path = os.path.join(output_card_dir_path, f"{os.path.splitext(img_file)[0]}_original.jpg")
        cv2.imwrite(original_output_path, image)

        # Generate augmented images
        for i in range(5):  # Create 5 augmented versions per image
            augmented = augment(image=image)
            augmented_image = augmented["image"]

            # Save the augmented image
            output_filename = f"{os.path.splitext(img_file)[0]}_aug_{i}.jpg"
            output_path = os.path.join(output_card_dir_path, output_filename)
            cv2.imwrite(output_path, augmented_image)

print("Augmentation completed!")
