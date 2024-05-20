import numpy as np
from sklearn.metrics.pairwise import cosine_similarity

def apply_fashion_rules(features, dominant_colors, occasion, season, style_theme, skin_tone, clothing_category):
    advice = []

    # Convert primary color to name
    primary_color = dominant_colors[0]
    primary_color_name = rgb_to_color_name(primary_color)
    
    # Primary color and style theme advice
    advice.append(f"We think in order to create the best outfit, choose {primary_color_name} {clothing_category}.")
    
    # General color advice
    if len(dominant_colors) > 3:
        advice.append("Avoid using more than three colors in an outfit to prevent clashing.")

    # Occasion appropriateness
    if occasion == "casual":
        advice.append("Choose casual clothing items.")
    elif occasion == "formal":
        advice.append("Opt for more elegant and refined clothing items.")
    elif occasion == "night out":
        advice.append("Choose stylish and eye-catching items for a night out.")
    elif occasion == "office":
        advice.append("Choose professional and polished clothing items for the office.")

    # Balancing proportions
    outfit_complexity = features.get('outfit_complexity', 'simple')
    if outfit_complexity == 'simple':
        advice.append("Match large statement pieces with simple outfits.")
    else:
        advice.append("Match delicate accessories with intricate outfits.")

    # Seasonal relevance
    if season == "summer":
        advice.append("Choose light and breathable fabrics for summer.")
    elif season == "winter":
        advice.append("Choose warm, rich-toned and layered clothing for winter.")
    elif season == "spring":
        advice.append("Opt for fresh and vibrant colors for spring.")
    elif season == "autumn":
        advice.append("Choose warm and earthy tones for fall.")

    # Style consistency
    advice.append(f"Maintain a consistent style theme: {style_theme} items for a {style_theme} outfit.")

    # Skin tone compatibility
    if skin_tone == "warm":
        advice.append("Warm colors such as gold and red will complement your skin tone.")
    elif skin_tone == "cool":
        advice.append("Cool colors such as silver and blue will complement your skin tone.")
    elif skin_tone == "neutral":
        advice.append("Neutral colors such as beige, gray, and navy will complement your skin tone.")
    elif skin_tone == "olive":
        advice.append("Olive skin tones look great with earthy colors like green and brown.")

    # Focal points
    advice.append(f"Use {clothing_category} to create focal points in the outfit.")

    # Functionality and comfort
    if occasion == "night out":
        advice.append("Choose practical and comfortable items for the occasion.")
    elif occasion == "office":
        advice.append("Choose comfortable yet professional items for the office.")

    # Trend awareness
    advice.append("Incorporate current fashion trends into your choices but balance them with timeless pieces to avoid looking dated.")

    # Color compatibility
    if colors_compatible(features, dominant_colors):
        advice.append("The clothing items match the colors of the outfit.")
    else:
        advice.append("Consider items that complement the colors of the outfit.")

    # Clothing category specific
    if clothing_category:
        advice.append(f"Consider different styles and fits of {clothing_category}.")

    return [], advice  # Only returning advice for now

def colors_compatible(features, dominant_colors, threshold=0.7):
    user_colors = features.get("dominant_colors")
    accessory_colors = dominant_colors
    
    if user_colors is None:
        return False
    
    # Calculate color similarity
    similarity_scores = []
    for user_color in user_colors:
        for accessory_color in accessory_colors:
            similarity_score = color_similarity(user_color, accessory_color)
            similarity_scores.append(similarity_score)
    
    # Calculate average similarity score
    avg_similarity = np.mean(similarity_scores)
    
    # Check if average similarity meets the threshold
    return avg_similarity >= threshold

def color_similarity(color1, color2):
    # Calculate cosine similarity between two colors
    color1 = np.array(color1).reshape(1, -1)
    color2 = np.array(color2).reshape(1, -1)
    similarity = cosine_similarity(color1, color2)[0][0]
    return similarity

def rgb_to_color_name(rgb):
    # Define a simple dictionary for color names
    color_names = {
        (216, 205, 197): "Beige",
        (63, 54, 49): "Dark Brown",
        (157, 143, 134): "Grey",
        (255, 255, 255): "White",
        (0, 0, 0): "Black",
        (255, 0, 0): "Red",
        (0, 255, 0): "Green",
        (0, 0, 255): "Blue",
        (255, 255, 0): "Yellow",
        (255, 165, 0): "Orange",
        (128, 0, 128): "Purple",
        (255, 192, 203): "Pink",
        (0, 128, 128): "Teal",
        # Add more colors as needed
    }

    # Find the closest color name
    closest_color_name = "RGB({}, {}, {})".format(*rgb)
    min_distance = float('inf')

    for color_rgb, name in color_names.items():
        distance = np.linalg.norm(np.array(rgb) - np.array(color_rgb))
        if distance < min_distance:
            min_distance = distance
            closest_color_name = name

    return closest_color_name
