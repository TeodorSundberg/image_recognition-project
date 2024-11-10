from PIL import Image
import pytesseract

# Load the card image
card_image_path = "path_to_your_card_image.jpg"
card_image = Image.open(card_image_path)
width, height = card_image.size

# Define the "Title Area" (top 10% of the card)
title_area = (0, 0, width, int(height * 0.1))
title_image = card_image.crop(title_area)

# Perform OCR on the Title Area to get the card name
card_name = pytesseract.image_to_string(title_image, config="--psm 7")  # PSM 7 is optimized for a single line of text
print("Card Name:", card_name.strip())
