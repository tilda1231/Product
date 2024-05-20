from flask import Flask, request, jsonify, send_from_directory, abort, Response
from flask_cors import CORS
from recommendation_generator import generate_accessory_recommendations
import os

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "*"}})

IMAGE_FOLDER = os.path.abspath("../Img/img")
if not os.path.exists(IMAGE_FOLDER):
    print(f"Error: Image directory {IMAGE_FOLDER} does not exist.")
app.config['IMAGE_FOLDER'] = IMAGE_FOLDER

@app.route('/upload', methods=['POST'])
def upload_file():
    print("Received request to upload file")
    if 'file' not in request.files:
        print("No file part")
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        print("No selected file")
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file_path = os.path.join(app.config['IMAGE_FOLDER'], file.filename)
        file.save(file_path)
        print(f"File saved to {file_path}")

        occasion = request.form['occasion']
        season = request.form['season']
        style_theme = request.form['style_theme']
        skin_tone = request.form['skin_tone']
        gender = request.form['gender']
        clothing_type = request.form['clothing_type']

        print(f"Occasion: {occasion}, Season: {season}, Style Theme: {style_theme}, Skin Tone: {skin_tone}, Gender: {gender}, Clothing Type: {clothing_type}")
        print("Generating recommendations...")
        result = generate_accessory_recommendations(file_path, occasion, season, style_theme, skin_tone, gender, clothing_type, max_recommendations=10)

        recommendations = result['recommendations']
        for recommendation in recommendations:
            relative_path = os.path.relpath(recommendation['img'], app.config['IMAGE_FOLDER'])
            recommendation['img'] = f"http://127.0.0.1:5000/images/{relative_path}"
            print(f"Recommendation image path: {recommendation['img']}")

        print("Recommendations generated")
        return jsonify(result)

@app.route('/images/<path:filename>')
def serve_image(filename):
    print(f"Serving image: {filename}")
    file_path = os.path.join(app.config['IMAGE_FOLDER'], filename)
    if not os.path.exists(file_path):
        print(f"Error: Image {filename} not found at {file_path}")
        abort(404)
    return send_from_directory(app.config['IMAGE_FOLDER'], filename)

@app.route('/test-cors', methods=['GET'])
def test_cors():
    return jsonify({"message": "CORS is working!"})

@app.route('/')
def index():
    return Response({"Server is Running!"})

if __name__ == '__main__':
    app.run(debug=True)
