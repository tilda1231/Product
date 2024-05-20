import sys
from recommendation_generator import generate_accessory_recommendations

def main():
    if len(sys.argv) != 6:  # Adjusted for the addition of dataset argument
        print("Usage: python main.py <user_input> <occasion> <season> <style_theme> <skin_tone>")
        sys.exit(1)

    user_input = sys.argv[1]
    occasion = sys.argv[2]
    season = sys.argv[3]
    style_theme = sys.argv[4]
    skin_tone = sys.argv[5]


    print(f"Number of arguments: {len(sys.argv)}")
    print(f"Argument List: {str(sys.argv)}")

    generate_accessory_recommendations(user_input, occasion, season, style_theme, skin_tone)  # Passed dataset

if __name__ == "__main__":
    main()