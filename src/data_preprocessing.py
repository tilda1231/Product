import json
import spacy
import string
from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer
import numpy as np
import re
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import os
import cv2
from sklearn.preprocessing import StandardScaler
from tensorflow.keras.applications import ResNet50 # type: ignore
from tensorflow.keras.applications.resnet50 import preprocess_input # type: ignore

### Step 1: Extracting the relvent Infomation: 

# Load JSON file
with open('../Anno/list_description_inshop.json', 'r') as f:
    data = json.load(f)

# Check if data is a list
if isinstance(data, list):
    # Iterate over items in the list
    for item in data:
        # Extract item ID and description
        item_id = item['item']
        description = item['description']
        # Process each item
        print(f"Item ID: {item_id}, Description: {description}")
else:
    print("Error: JSON data is not in the expected format (list).")

# Extract item descriptions
item_descriptions = {}
if isinstance(data, list):
    for item in data:
        item_id = item['item']
        description = item['description']
        item_descriptions[item_id] = description

# Print the first few item descriptions as a sample
for item_id, description in list(item_descriptions.items())[:5]:
    print(f"Item ID: {item_id}, Description: {description}")

### Step 2: Tokenizing and Text Cleaning ###

# Load the English language model
nlp = spacy.load('en_core_web_sm')

# Define a function for tokenization and text cleaning
def tokenize_and_clean(text):
    # If the input is already a string, proceed with tokenization and cleaning
    if isinstance(text, str):
        # Process the text using SpaCy
        doc = nlp(text)
        
        # Tokenize the text into words, remove punctuation, and convert to lowercase
        tokens = [token.text.lower() for token in doc if token.text not in string.punctuation]
        
        # Remove stopwords
        tokens = [token for token in tokens if not nlp.vocab[token].is_stop]
        
        return tokens
    else:
        # If the input is not a string, return an empty list
        return []

# Create a dictionary to store cleaned descriptions
cleaned_item_descriptions = {}

# Process each item description
for item_id, description in item_descriptions.items():
    # Tokenize and clean the description
    cleaned_description = tokenize_and_clean(description)
    
    # Store the cleaned description in the dictionary
    cleaned_item_descriptions[item_id] = cleaned_description

# Define the output file path for the cleaned descriptions
cleaned_output_file_path = 'cleaned_item_descriptions.json'

# Save cleaned_item_descriptions to a JSON file
with open(cleaned_output_file_path, 'w') as f:
    json.dump(cleaned_item_descriptions, f)

print(f"Cleaned descriptions saved to {cleaned_output_file_path}")

### Step 3: Feature Extraction ###
# Load JSON file
with open('../Anno/list_description_inshop.json', 'r') as f:
    data = json.load(f)

# Extract item descriptions
item_descriptions = {}
for item in data:
    item_id = item['item']
    description = item['description']
    item_descriptions[item_id] = description

# Create a list of item descriptions
descriptions = list(item_descriptions.values())

# Flatten the list of lists into a single list of strings
flattened_descriptions = [' '.join(desc) for desc in descriptions]

# Bag-of-Words (BoW)
vectorizer_bow = CountVectorizer()
bow_matrix = vectorizer_bow.fit_transform(flattened_descriptions)

# TF-IDF
vectorizer_tfidf = TfidfVectorizer()
tfidf_matrix = vectorizer_tfidf.fit_transform(flattened_descriptions)

# Save BoW and TF-IDF matrices to files
np.save('bow_matrix.npy', bow_matrix.toarray())
np.save('tfidf_matrix.npy', tfidf_matrix.toarray())

print("BoW and TF-IDF matrices saved.")

# Save item descriptions to a JSON file
output_file_path = 'item_descriptions.json'
with open(output_file_path, 'w') as f:
    json.dump(item_descriptions, f)

print(f"Item descriptions saved to {output_file_path}")


### Step 4: Attribute Extraction ###

# Load JSON file containing item descriptions
with open('../Anno/list_description_inshop.json', 'r') as f:
    data = json.load(f)

unique_colors = [
    'Cream', 'Black-blush', 'Heather grey', 'Black-cream', 'Natural-black', 'Burgundy', 'Heather grey-black', 
    'Black-white', 'Black', 'Cream-multi', 'White', 'Black-red', 'Navy', 'Camel', 'Oatmeal-black', 'Yellow', 
    'Navy-red', 'Light heather grey', 'Charcoal', 'Cream-black', 'Navy-cream', 'Cream-red', 'Champagne', 
    'Rust', 'Blue', 'Grey-white', 'Peach', 'Red-navy', 'Green', 'Coral', 'Lavender', 'Charcoal healther', 
    'Heather navy', 'Oatmeal', 'Ivory-grey', 'Periwinkle', 'Red', 'Mauve-pink', 'Wine', 'Cream-black', 
    'Cream-taupe', 'Teal-navy', 'Burgundy-cream', 'Black-blush', 'Cream-periwinkle', 'Cream-magenta', 
    'Black-fuchsia', 'Lime', 'Pink', 'Mint-peach', 'White-blue', 'Yellow-black', 'Bright cobalt', 'Navy-mustard', 
    'Black-coral', 'Cocoa', 'Black-tomato', 'Orange-purple', 'Light blue', 'Indigo', 'Ivory', 'Sage', 'Aqua', 
    'Khaki', 'Mustard', 'Brick', 'Light Green', 'Cream-aqua', 'Black-gold', 'Rose', 'Cocoa-beige', 'Tomato', 
    'Jade', 'Blush-black', 'Black-taupe', 'Pink-teal', 'Royal', 'Chestnut', 'Emerald', 'Rust', 'Olive', 'Amber', 
    'Dark denim', 'Dusty blue', 'Light denim', 'Neon pink', 'Neon orange', 'Neon yellow', 'Apricot', 'Blue-cream', 
    'Black-silver', 'Mustard-black', 'Dark navy-cream', 'Burgundy-pink', 'Navy-blue', 'Ivory-black', 'Gold-blue', 
    'Eggplant', 'Light blue-navy', 'Olive-khaki', 'Mustard-navy', 'Charcoal-taupe', 'Black-multi', 'Denim washed-white', 
    'Black-cream', 'Navy-cream', 'Dark olive', 'Peach-multi', 'Beige-orange', 'Nude-black', 'Burgundy', 'Teal-black', 
    'Salmon', 'Navy-white', 'Ivory-black', 'Cream-rust', 'Baby pink', 'Cream-dark navy', 'Olive-white', 'Denim-cream', 
    'Mint', 'Fuchsia', 'Medium denim', 'Mint-white', 'Wine', 'Grey', 'Rose', 'Plum', 'Silver', 'Sage-coral', 
    'Hunter green', 'Dawn pink', 'Berry', 'Gold', 'Ravishing red', 'Peach', 'Lavender-cream', 'Medium denim', 
    'Burgundy-navy', 'Brick', 'Blue-aqua', 'Brown', 'Ivory-black', 'Cream-green', 'Pink-neon yellow', 'Ivory-burgundy', 
    'Black-pink', 'Pink-aqua', 'Vanilla', 'Coral-cream', 'Silver-multi', 'Peacock', 'Mint-cream', 'Cherry-cream', 
    'Rust-multi', 'Bubble gum', 'Blush', 'Black-natural', 'Black-mint', 'Olive-mustard', 'Grey-ivory', 'Dynasty green', 
    'Cream-pink', 'White-purple', 'Cocoa', 'Dusty blue', 'Sage-cream', 'Tan-cream', 'Bright cobalt-red', 'Ivory-black'
]

# Consolidate similar colors
consolidated_colors = {
    'Cream-multi': 'Cream',
    'Cream-periwinkle': 'Cream',
    'Light heather grey': 'Heather grey',
    'Cream-taupe': 'Cream',
    'Burgundy-cream': 'Burgundy',
    'Cream-magenta': 'Cream',
    'Cream-aqua': 'Cream',
    'Blue-cream': 'Blue',
    'Dark navy-cream': 'Navy',
    'Ivory-black': 'Ivory',
    'Mustard-navy': 'Mustard',
    'Cream-dark navy': 'Cream',
    'Blue-aqua': 'Blue',
    'Pink-neon yellow': 'Pink',
    'Ivory-burgundy': 'Ivory',
    'Coral-cream': 'Coral',
    'Black-natural': 'Black',
    'Black-mint': 'Black',
    'Cream-pink': 'Cream',
    'Bright cobalt-red': 'Blue',
}

# Remove duplicates
unique_colors = list(set(unique_colors))

# Standardize color names
standardized_colors = [consolidated_colors.get(color, color) for color in unique_colors]

# Create a regular expression pattern for colors
pattern_colors = re.compile(r'\b(' + '|'.join(re.escape(color) for color in standardized_colors) + r')\b', re.IGNORECASE)
pattern_materials = re.compile(r'\b(cotton|polyester|wool|silk|denim|leather|linen|velvet|satin|chiffon|lace|knit|spandex|rayon|acrylic|cashmere|nylon|viscose|lyocell|modal)\b', re.IGNORECASE)
pattern_styles = re.compile(r'\b(casual|formal|sporty|chic|vintage|bohemian|preppy|grunge|feminine|laid-back|modern|classic|sleek|trendy|elegant|edgy|streetwear|minimalistic|sophisticated|retro|hipster|urban)\b', re.IGNORECASE)
pattern_patterns = re.compile(r'\b(stripes|floral|polka dots|checks|abstract|geometric|plaid|tribal|paisley|colorblocked)\b', re.IGNORECASE)


# Create dictionaries to store extracted attributes
extracted_colors = {}
extracted_materials = {}
extracted_styles = {}
extracted_patterns = {}

# Process each item description
for item in data:
    item_id = item['item']
    description = item['description']

     # Ensure description is a string
    if isinstance(description, list):
        description = ' '.join(description)

    # Search for colors in the description
    colors = pattern_colors.findall(description)
    if colors:
        extracted_colors[item_id] = colors

    # Search for materials in the description
    materials = pattern_materials.findall(description)
    if materials:
        extracted_materials[item_id] = materials

    # Search for styles in the description
    styles = pattern_styles.findall(description)
    if styles:
        extracted_styles[item_id] = styles

    # Search for patterns in the description
    patterns = pattern_patterns.findall(description)
    if patterns:
        extracted_patterns[item_id] = patterns

# Save extracted attributes to JSON files
with open('extracted_colors.json', 'w') as f:
    json.dump(extracted_colors, f)

with open('extracted_materials.json', 'w') as f:
    json.dump(extracted_materials, f)

with open('extracted_styles.json', 'w') as f:
    json.dump(extracted_styles, f)

with open('extracted_patterns.json', 'w') as f:
    json.dump(extracted_patterns, f)

print("Extracted attributes saved.")


### Step 5: Data Analysis and Visualisation. ###

# Load extracted attributes from JSON files
with open('extracted_colors.json', 'r') as f:
    extracted_colors = json.load(f)

with open('extracted_materials.json', 'r') as f:
    extracted_materials = json.load(f)

with open('extracted_styles.json', 'r') as f:
    extracted_styles = json.load(f)

with open('extracted_patterns.json', 'r') as f:
    extracted_patterns = json.load(f)

# Load item descriptions from JSON file
with open('item_descriptions.json', 'r') as f:
    item_descriptions = json.load(f)

# Count occurrences of colors
color_counts = {color: len(items) for items in extracted_colors.values() for color in items}

# Count occurrences of materials
material_counts = {material: len(items) for items in extracted_materials.values() for material in items}

# Count occurrences of styles
style_counts = {style: len(items) for items in extracted_styles.values() for style in items}

# Count occurrences of patterns
pattern_counts = {pattern: len(items) for items in extracted_patterns.values() for pattern in items}

# Create DataFrames for attributes
color_df = pd.DataFrame.from_dict(color_counts, orient='index', columns=['Count'])
material_df = pd.DataFrame.from_dict(material_counts, orient='index', columns=['Count'])
style_df = pd.DataFrame.from_dict(style_counts, orient='index', columns=['Count'])
pattern_df = pd.DataFrame.from_dict(pattern_counts, orient='index', columns=['Count'])

# Plot distribution of colors
plt.figure(figsize=(10, 6))
sns.barplot(x=color_df.index, y=color_df['Count'], hue=color_df.index, palette='viridis', legend=False)
plt.title('Distribution of Colors')
plt.xlabel('Color')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Plot distribution of materials
plt.figure(figsize=(10, 6))
sns.barplot(x=material_df.index, y=material_df['Count'], hue=material_df.index, palette='magma', legend=False)
plt.title('Distribution of Materials')
plt.xlabel('Material')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Plot distribution of styles
plt.figure(figsize=(10, 6))
sns.barplot(x=style_df.index, y=style_df['Count'], hue=style_df.index, palette='rocket', legend=False)
plt.title('Distribution of Styles')
plt.xlabel('Style')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()

# Plot distribution of patterns
plt.figure(figsize=(10, 6))
sns.barplot(x=pattern_df.index, y=pattern_df['Count'], hue=pattern_df.index, palette='cubehelix', legend=False)
plt.title('Distribution of Patterns')
plt.xlabel('Pattern')
plt.ylabel('Count')
plt.xticks(rotation=45)
plt.show()



### Step 6: Intergrating with Image Data ###
# Function to load and preprocess images
def load_and_preprocess_images(image_directory, target_size=(224, 224)):
    images = []
    for root, dirs, files in os.walk(image_directory):
        for filename in files:
            if filename.endswith(".jpg") or filename.endswith(".png"): 
                img_path = os.path.join(root, filename)
                img = cv2.imread(img_path)
                if img is not None:
                    # Resize image
                    resized_img = cv2.resize(img, target_size)
                    # Normalize pixel values
                    normalized_img = resized_img.astype(np.float32) / 255.0
                    images.append(normalized_img)
    return np.array(images)

# Define the parent directory containing all category directories
parent_directory = "../Img/img"

# List all category directories
category_directories = [os.path.join(parent_directory, category) for category in os.listdir(parent_directory) if os.path.isdir(os.path.join(parent_directory, category))]

# Load and preprocess images for each category
all_images = []
for category_directory in category_directories:
    category_images = load_and_preprocess_images(category_directory)
    all_images.extend(category_images)

# Convert the list of images to a NumPy array
all_images_array = np.array(all_images)

# Save preprocessed images to a file
np.save('preprocessed_images.npy', all_images_array)

# Use a pre-trained CNN model to extract features from images
# Here, we use ResNet50 as an example
base_model = ResNet50(weights='imagenet', include_top=False, pooling='avg')

# Preprocess input images according to the requirements of ResNet50
preprocessed_images = preprocess_input(all_images_array)

# Extract features from images using the pre-trained model
extracted_features = base_model.predict(preprocessed_images)


# Save extracted features to a file for future use
np.save('extracted_features.npy', extracted_features)