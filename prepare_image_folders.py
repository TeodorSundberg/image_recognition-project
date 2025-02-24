import os
import shutil


def organize_images_by_class(input_dir, output_dir):
    """Organize images into subdirectories by card name."""
    os.makedirs(output_dir, exist_ok=True)

    for file_name in os.listdir(input_dir):
        if file_name.endswith(".jpg"):
            # Extract the card name from the file name (assumes format: 'NNN_cardname.jpg')
            card_name = "_".join(file_name.split("_")[1:]).replace(".jpg", "").strip()
            card_dir = os.path.join(output_dir, card_name)

            # Create the card's directory if it doesn't exist
            os.makedirs(card_dir, exist_ok=True)

            # Move the file to the respective directory
            shutil.move(os.path.join(input_dir, file_name), os.path.join(card_dir, file_name))


input_dir = "magic_card_images"  # Original folder with flat structure
output_dir = "organized_magic_cards"  # Target folder with structured data

organize_images_by_class(input_dir, output_dir)
