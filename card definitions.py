from PIL import Image
import pytesseract
import matplotlib.pyplot as plt

# Load the card image
card_image_path = "path_to_your_card_image.jpg"
card_image = Image.open(card_image_path)
width, height = card_image.size

# Define regions based on typical Magic card layout ratios
regions = {
    "Title Area": (0, 0, width, int(height * 0.1)),  # Top ~10% for title
    "Mana Cost": (int(width * 0.8), 0, width, int(height * 0.1)),  # Right of Title, top 10%
    "Image Box": (0, int(height * 0.1), width, int(height * 0.5)),  # Top 40-50% for image
    "Text Box": (0, int(height * 0.65), width, int(height * 0.95)),  # Bottom 30% for main text
    "Power/Toughness": (int(width * 0.8), int(height * 0.9), width, height)  # Bottom-right for creatures
}

# Extract and perform OCR on the Title Area to get the card name
title_area_coords = regions["Title Area"]
title_image = card_image.crop(title_area_coords)
card_name = pytesseract.image_to_string(title_image, config="--psm 7")  # PSM 7 is optimized for single-line text

# Display the Title Area for reference
plt.imshow(title_image)
plt.axis('off')
plt.title("Title Area - Detected Card Name")
plt.show()

# Print the detected card name
print("Detected Card Name:", card_name.strip())
