import os
import pandas as pd
import re


def read_file(file_path):
    """Read a .txt file and extract its lines."""
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return [line.strip().lower() for line in file if line.strip()]
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []


def clean_card_names(card_list):
    """Clean and filter card names."""
    cleaned_cards = []
    sideboard_found = False  # Track if "Sideboard" has been encountered

    for card in card_list:
        # Stop processing once "Sideboard" is found
        if card.startswith("sideboard"):
            sideboard_found = True
            continue
        if sideboard_found:
            continue

        # Remove leading numbers if they exist
        cleaned_card = re.sub(r"^\d+\s*", "", card).strip()
        if cleaned_card:  # Add only non-empty card names
            cleaned_cards.append(cleaned_card)
    return cleaned_cards


def get_unique_cards(input_dir):
    """Combine and deduplicate card names from all files in the input directory."""
    unique_cards = set()
    for file_name in os.listdir(input_dir):
        file_path = os.path.join(input_dir, file_name)
        if os.path.isfile(file_path) and file_name.lower().endswith(".txt"):
            print(f"Processing file: {file_name}")
            card_names = read_file(file_path)
            cleaned_names = clean_card_names(card_names)
            unique_cards.update(cleaned_names)
    return sorted(unique_cards)


def save_to_txt(card_list, output_file):
    """Save the card list to a TXT file."""
    try:
        os.makedirs(os.path.dirname(output_file), exist_ok=True)  # Ensure output directory exists
        with open(output_file, "w", encoding="utf-8") as file:
            for card in card_list:
                file.write(card + "\n")
        print(f"Unique card list saved to {output_file}")
    except Exception as e:
        print(f"Error saving file {output_file}: {e}")


def main():
    input_dir = "decklists"  # Folder containing input files
    output_dir = "raw_txt_api"  # Folder to save the output file
    output_file = os.path.join(output_dir, "unique_magic_cards.txt")

    # Check if the input directory exists
    if not os.path.exists(input_dir):
        print(f"Input directory '{input_dir}' does not exist.")
        return

    # Extract unique cards
    print("Extracting unique Magic card names...")
    unique_cards = get_unique_cards(input_dir)

    # Check if any cards were found
    if not unique_cards:
        print("No unique cards found. Please check your input files.")
        return

    # Save the unique cards to the output file
    save_to_txt(unique_cards, output_file)
    print(f"Processed {len(unique_cards)} unique card names.")


if __name__ == "__main__":
    main()
