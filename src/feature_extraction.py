import cv2
import numpy as np
from sklearn.cluster import KMeans
import spacy
import string
from transformers import BlipProcessor, BlipForConditionalGeneration
import torch
from PIL import Image
import webcolors

nlp = spacy.load('en_core_web_sm')

def get_dominant_colors(image, k=3):
    resized_image = cv2.resize(image, (25, 25))  # Smaller size for faster processing
    rgb_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2RGB)
    pixel_values = rgb_image.reshape((-1, 3))
    pixel_values = np.float32(pixel_values)
    kmeans = KMeans(n_clusters=k, random_state=0)
    kmeans.fit(pixel_values)
    centers = kmeans.cluster_centers_.astype(int)  # Convert centers to integer
    return centers.tolist()  # Convert to list for easier handling

def extract_image_features(img_path):
    image = cv2.imread(img_path)
    dominant_colors = get_dominant_colors(image)
    print(f"Image Processing: Dominant colours extracted from the uploaded image: {dominant_colors}")
    return dominant_colors

def tokenize_and_clean(text):
    if isinstance(text, str):
        doc = nlp(text)
        tokens = [token.text.lower() for token in doc if token.text not in string.punctuation]
        tokens = [token for token in tokens if not nlp.vocab[token].is_stop]
        return tokens
    else:
        return []

def extract_features_from_description(description):
    cleaned_tokens = tokenize_and_clean(description)
    features = cleaned_tokens  # Placeholder implementation
    return features

# Load the BLIP model and processor
processor = BlipProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def generate_caption(img_path):
    image = Image.open(img_path).convert("RGB")
    inputs = processor(image, return_tensors="pt")
    out = model.generate(**inputs)
    caption = processor.decode(out[0], skip_special_tokens=True)
    return caption

def refine_caption(caption, clothing_type):
    keywords = {
        "pants": ["pants", "trousers", "jeans", "leggings", "shorts"],
        "tops": ["shirt", "t-shirt", "blouse", "top", "sweater"]
    }
    clothing_keywords = keywords.get(clothing_type, [])
    words = caption.split()
    
    # Find the first occurrence of a clothing keyword
    for i, word in enumerate(words):
        if word in clothing_keywords:
            start_index = max(i - 2, 0)  # Include a few words before the keyword
            end_index = min(i + 5, len(words))  # Include a few words after the keyword
            return " ".join(words[start_index:end_index])
    
    return caption

def is_clothing_type_in_caption(caption, clothing_type_keywords):
    return any(keyword in caption.lower() for keyword in clothing_type_keywords)

def closest_color(requested_color):
    min_colors = {}
    for key, name in webcolors.CSS3_HEX_TO_NAMES.items():
        r_c, g_c, b_c = webcolors.hex_to_rgb(key)
        rd = (r_c - requested_color[0]) ** 2
        gd = (g_c - requested_color[1]) ** 2
        bd = (b_c - requested_color[2]) ** 2
        min_colors[(rd + gd + bd)] = name
    return min_colors[min(min_colors.keys())]

def get_color_name(rgb_color):
    try:
        color_name = webcolors.rgb_to_name(rgb_color)
    except ValueError:
        color_name = closest_color(rgb_color)
    return color_name
