import sys
from image_classification import extract_features
from feature_extraction import extract_image_features, extract_features_from_description, get_dominant_colors, generate_caption, refine_caption, is_clothing_type_in_caption, get_color_name
from rule_engine import apply_fashion_rules, colors_compatible 
import numpy as np
from PIL import Image
import os
import cv2
from concurrent.futures import ThreadPoolExecutor, as_completed
import random

dataset_path = os.path.abspath("../Img/img")

def list_image_files(root_dir):
    image_files = []
    for root, dirs, files in os.walk(root_dir):
        for file in files:
            if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                image_files.append(os.path.join(root, file))
    return image_files

# Usage example:
image_files = list_image_files(dataset_path)
print("Image files found:")
for file in image_files:
    print(file)

def process_image(image_path, fashion_rules, features):
    try:
        image = cv2.imread(image_path)
        if image is None:
            raise ValueError(f"Error loading image (None returned) {image_path}")

        dominant_colors = get_dominant_colors(image)

        image_features = {
            "primary_color": dominant_colors[0],
            "dominant_colors": dominant_colors
        }

        if apply_fashion_rules_to_image(fashion_rules, image_features, features):
            return image_path, dominant_colors
        else:
            return None, None

    except Exception as e:
        print(f"Error processing image {image_path}: {e}")
        return None, None

def apply_fashion_rules_to_image(fashion_rules, image_features, features):
    for rule in fashion_rules:
        if not satisfies_rule(image_features, rule, features):
            return False
    return True

def satisfies_rule(image_features, rule, features):
    if rule.startswith("Match accessories with the primary color"):
        return matches_primary_color(image_features, rule)
    elif rule.startswith("Avoid using more than three colours"):
        return avoids_clashing_colors(image_features, rule)
    else:
        return True

def matches_primary_color(image_features, rule):
    rule_primary_color = tuple(map(float, rule.split('(')[1].strip(')').split(',')))
    image_primary_color = image_features.get("primary_color")
    return colors_are_close(image_primary_color, rule_primary_color)

def avoids_clashing_colors(image_features, rule):
    num_colors = len(image_features.get("dominant_colors"))
    return num_colors <= 3

def colors_are_close(color1, color2, tolerance=30):
    return all(abs(c1 - c2) <= tolerance for c1, c2 in zip(color1, color2))

def filter_dataset(fashion_rules, features, dataset_path, gender, clothing_type, max_images=100):
    filtered_images = []
    image_paths = []

    print("Entering filter_dataset function")

    # Determine the path based on gender and clothing type
    if gender == "unisex":
        gender_paths = ["MEN", "WOMEN"]
    else:
        gender_paths = [gender.upper()]

    for gender_path in gender_paths:
        if clothing_type:
            clothing_path = os.path.join(dataset_path, gender_path, clothing_type)
        else:
            clothing_path = os.path.join(dataset_path, gender_path)

        for root, dirs, files in os.walk(clothing_path):
            for file in files:
                if file.lower().endswith(('.jpg', '.jpeg', '.png')):
                    image_path = os.path.join(root, file)
                    image_paths.append(image_path)

    # Sample a subset of image paths
    if len(image_paths) > max_images:
        image_paths = random.sample(image_paths, max_images)

    with ThreadPoolExecutor(max_workers=8) as executor:
        future_to_path = {executor.submit(process_image, path, fashion_rules, features): path for path in image_paths}
        for future in as_completed(future_to_path):
            result, dominant_colors = future.result()
            if result:
                filtered_images.append((result, dominant_colors))

    print("Exiting filter_dataset function")
    print(f"Number of images that passed the rule check: {len(filtered_images)}")
    return filtered_images

def generate_accessory_recommendations(user_input, occasion, season, style_theme, skin_tone, gender, clothing_type, max_recommendations=10):
    print("Generating clothing recommendations...")
    print(f"User input: {user_input}")
    print(f"Occasion: {occasion}, Season: {season}, Style Theme: {style_theme}, Skin Tone: {skin_tone}, Gender: {gender}, Clothing Type: {clothing_type}")

    # Step 1: Process user input
    if user_input.endswith(('.jpg', '.jpeg', '.png')):
        print("User input is an image.")
        features = extract_features(user_input)
    else:
        print("User input is a description.")
        features = extract_features_from_description(user_input)

    print(f"Extracted features: {features}")

    # Ensure features is a dictionary
    if isinstance(features, np.ndarray):
        features = {"feature": features}

    # Step 2: Generate fashion rules
    dominant_colors = extract_image_features(user_input)
    print(f"Dominant colors: {dominant_colors}")

    fashion_rules, advice = apply_fashion_rules(features, dominant_colors, occasion, season, style_theme, skin_tone, clothing_type)
    print(f"Fashion rules: {fashion_rules}")

    # Step 3: Filter dataset based on fashion rules
    clothing_images = filter_dataset(fashion_rules, features, dataset_path, gender, clothing_type)
    print(f"Filtered clothing images: {clothing_images}")

    # Step 4: Limit the number of recommendations
    recommendations = []
    clothing_type_keywords = {
        "pants": ["pants", "trousers", "jeans", "leggings", "shorts"],
        "tops": ["shirt", "t-shirt", "blouse", "top", "sweater"]
    }.get(clothing_type, [])

    for img, dominant_colors in clothing_images:
        caption = generate_caption(img)
        refined_caption = refine_caption(caption, clothing_type)
        if is_clothing_type_in_caption(refined_caption, clothing_type_keywords):
            recommendations.append({"img": img, "title": "Clothing Item", "description": refined_caption})
            if len(recommendations) == max_recommendations:
                break

    for recommendation in recommendations:
        print(f"Recommendation image path: {recommendation['img']}")  # Debug print

    return {"recommendations": recommendations, "advice": advice}


if __name__ == "__main__":
    if len(sys.argv) != 6:
        print("Usage: python main.py <user_input> <occasion> <season> <style_theme> <skin_tone>")
        sys.exit(1)

    user_input = sys.argv[1]
    occasion = sys.argv[2]
    season = sys.argv[3]
    style_theme = sys.argv[4]
    skin_tone = sys.argv[5]

    generate_accessory_recommendations(user_input, occasion, season, style_theme, skin_tone)
