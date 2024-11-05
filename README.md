Supervised Learning Project - Playing Card Reader


Specifikation

I will base my supervised learning on trying to read card text of pictures from a game with a huge number of different cards

Cards can be simple one sentence structures of all english words like above or more complex like below with 




However, each card generally has 4 generally main identifying features.

Card name - Top left of Card
Rules text - In the middle
Symbol (used to narrow down the search only) - on the right
Collector identifier number  - bottom left
There is also a 5th thing which is artwork, but I plan to leave it out of scope in the 1st iteration.


I want to be able to train a program to identify cards, by having the minimal amount of information and sometimes not fully pixelated for a clear view.
Training data could be semi automated with random black pixels not shown. 
It will then go to an API to get the full text and name of the card. https://github.com/MagicTheGathering/mtg-sdk-python

The training of the supervised tool will be done by downloading a bunch of pictures through the API where we will have access to the correct answer.

Open library datasets
I want to do the project in multiple steps.
Where I can see stopping at step 2 and refining that as the only part of the project.

Step 1: 
Text Classification and OCR: Focus on analyzing text to train a text classification model and then working more on Optical Character Recognition to extract text from pictures. 
CHAT GPT Suggestion: This could be done with models like BERT or fine-tuning on a library like Hugging Face.

Step 2:
Image Classification:
I want to use the public card reader API which should be able to create an automated and labeled dataset of card images and text.
CHAT GPT Suggestion: CNN or a model like ResNet
Step 3:
Multi-Object Detection:
Training on multiple cards: The first model should be training on 1 picture per card, but the next one could be about training the modell to use a picture with several object
Chat GPT Extra stuff for step 3	
	Common architectures include YOLO (You Only Look Once), Faster R-CNN, and SSD (Single Shot MultiBox Detector). These models are optimized for identifying multiple objects in images and drawing bounding boxes around them.make it straightforward to set up.
After detection, you might want to apply OCR to the bounding boxes if the goal is to analyze the card text.
By training a model with these techniques, I want to be able to locate and classify each card individually, even in a cluttered image with overlapping or partially hidden cards.
Features
Text Classification
Image Classification
Data Collection
Preprocessing
Feature Extraction
Model Training
User Interface
Confidence Intervals
Limitations


Requirements
Software Requirements
Libraries
pandas: For data manipulation and analysis.
scikit-learn: Machine learning algorithms and preprocessing.
numpy: Numerical operations.
requests: For API calls, or recommended API method for data sourcing.
Classes and Methods
CardData
Responsible for loading, cleaning, and preprocessing Magic card data.
Methods:
load_data(): Load card data, possibly from a CSV, database, or API.
clean_data(): Clean data by handling missing values, duplicates, and formatting inconsistencies.
preprocess_data(): Preprocess the card data, such as converting card texts to a standard format.
ImageData
Handles images of Magic cards and preprocesses them for model training.
Methods:
load_image_data(): Load card images from a directory or API.
annotate_data(): Annotate images with bounding boxes for multi-card detection.
preprocess_image_data(): Resize, normalize, and apply any necessary transformations to the images.
FeatureExtractor
Extracts and encodes features from both text and image data.
Methods:
encode_text_features(): Process card text data, perhaps through tokenization and vectorization.
extract_image_features(): Extract image features using pre-trained CNN layers or other relevant feature extraction methods.
create_feature_matrix(): Combine extracted features into a single matrix for model input.
CardRecognitionModel
Implements the chosen model for card recognition and classification (e.g., YOLO for image detection, combined with OCR for text extraction).
Methods:
train_model(): Train the model to recognize and classify Magic cards.
detect_cards(): Detect and classify multiple cards within a single image.
extract_text(): Use OCR to extract text from identified card regions for further classification.
UserInterface
Manages user interactions and displays results.
Methods:
get_user_input(): Allows the user to specify image inputs or model preferences.
display_classification_results(): Show detected cards, their names, and attributes to the user.
This structure will support training and deployment of a Magic card recognition and classification model that can handle multiple cards in one image and output relevant text and card details.


Extended END goal
EVALUATE - 
The end goal of what I want to do is to have video footage similar to this and be able to identify all of the cards in the picture

With varying levels of difficulty and ofc with the possibility of not having enough data to make a decision.

But I would be happy with just having being able to identify 1 card with faults like these



