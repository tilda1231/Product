# WardrobeWhiz Backend

This directory contains the backend code, data processing scripts, and models for the WardrobeWhiz intelligent clothing recommendation system.

## Directory Structure

- `app.py`: Main application script to run the Flask server.
- `main.py`: Entry point script for generating recommendations.
- `data_preprocessing.py`: Script for preprocessing data.
- `feature_extraction.py`: Script for extracting features from images and descriptions.
- `image_classification.py`: Script for classifying images.
- `recommendation_generator.py`: Script for generating clothing recommendations.
- `rule_engine.py`: Script for applying fashion rules.
- `uploads/`: Directory for storing uploaded images.
- `Img/`: Directory for storing image dataset.
- `__pycache__/`: Directory for storing compiled Python files.
- `bow_matrix.npy`: Bag-of-Words matrix.
- `cleaned_item_descriptions.json`: Cleaned item descriptions.
- `extracted_colors.json`: Extracted color attributes.
- `extracted_materials.json`: Extracted material attributes.
- `extracted_patterns.json`: Extracted pattern attributes.
- `extracted_styles.json`: Extracted style attributes.
- `item_descriptions.json`: Item descriptions.
- `preprocessed_images.npy`: Preprocessed images.

## Running the Server

To run the backend server, navigate to the `src` directory and run:

```sh
python app.py
```
