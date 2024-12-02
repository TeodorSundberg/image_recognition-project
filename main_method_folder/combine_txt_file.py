import os
import pandas as pd
import re

def read_file(file_path):
    """Read a file and extract Magic card names."""
    _, ext = os.path.splitext(file_path.lower())
    try:
        if ext == ".csv":
            # Assume the first column contains the card names
            df = pd.read_csv(file_path)
            return df.iloc[:, 0].dropna().astype(str).str.lower().tolist()
        elif ext == ".txt":
            # Read all lines from the text file
            with open(file_path, "r", encoding="utf-8") as file:
                return [line.strip().lower() for line in file if line.strip()]
        elif ext in [".xls", ".xlsx"]:
            # Read the first column of Excel files
            df = pd.read_excel(file_path, sheet_name=0)
            return df.iloc[:, 0].dropna().astype(str).str.lower().tolist()
        else:
            print(f"Unsupported file format: {ext}")
            return []
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return []

def clean_card_names(card_list):
    """Clean and filter card names."""
    cleaned_cards = []
    for card in card_list:
        # Ignore lines starting with a number or "sideboard"
        if card.startswith("sideboard") or re.match(r"^\d+\s", card):
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
        if os.path.isfile(file_path):
            print(f"Processing file: {file_name}")
            card_names = read_file(file_path)
            # Clean and filter card names before adding
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
    input_dir = "decklists"  # Folder containing input files (relative path to the current directory)
    output_dir = "raw_txt_api"  # Folder to save the output file (relative path to the current directory)
    output_file = os.path.join(output_dir, "unique_magic
