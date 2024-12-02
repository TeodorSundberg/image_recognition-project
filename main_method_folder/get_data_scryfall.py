import requests
import os

# Directory to save downloaded images
output_dir = "./magic_card_images"
os.makedirs(output_dir, exist_ok=True)

# Function to download an image for a specific MTG card
def download_card_image(card_name, card_number):
    api_url = f"https://api.scryfall.com/cards/named?fuzzy={card_name}"

    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            card_data = response.json()
            image_url = card_data.get("image_uris", {}).get("normal")
            if image_url:
                response = requests.get(image_url)
                if response.status_code == 200:
                    filename = f"{card_number:03d}_{card_name.replace(' ', '_').replace('/', '_')}.jpg"
                    filepath = os.path.join(output_dir, filename)
                    with open(filepath, "wb") as img_file:
                        img_file.write(response.content)
                    print(f"Downloaded: {filename}")
                else:
                    print(f"Failed to download image for card {card_name}.")
            else:
                print(f"Card '{card_name}' does not have a standard image.")
        else:
            print(f"Failed to fetch card data for '{card_name}'. Status code: {response.status_code}")
    except Exception as e:
        print(f"Error downloading image for {card_name}: {e}")

# Function to read the list of unique card names from the text file
def read_card_names(input_file):
    try:
        with open(input_file, "r", encoding="utf-8") as file:
            return [line.strip().lower() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading file {input_file}: {e}")
        return []

# Main function to download images for all cards in the file
def download_images_for_all_cards(input_file):
    # Read the list of unique card names from the text file
    card_names = read_card_names(input_file)
    print(f"Found {len(card_names)} cards to download.")

    # Download images for each card
    for i, card_name in enumerate(card_names, start=1):
        download_card_image(card_name, i)

    print(f"Downloaded images for all {len(card_names)} cards.")

# Define the input file path (the path to your unique_magic_cards.txt)
input_file = "raw_txt_api/unique_magic_cards.txt"

# Download images for all the cards listed in the input file
download_images_for_all_cards(input_file)
