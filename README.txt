=====================================================================
WardrobeWhiz - Intelligent Clothing Recommendation System
=====================================================================

=====================================
In-shop Clothes Retrieval Benchmark
=====================================

--------------------------------------------------------
By Multimedia Lab, The Chinese University of Hong Kong
--------------------------------------------------------

For more information about the dataset, visit the project website:

  http://mmlab.ie.cuhk.edu.hk/projects/DeepFashion.html

If you use the dataset in a publication, please cite the paper below:

  @inproceedings{liu2016deepfashion,
 	author = {Ziwei Liu, Ping Luo, Shi Qiu, Xiaogang Wang, and Xiaoou Tang},
 	title = {DeepFashion: Powering Robust Clothes Recognition and Retrieval with Rich Annotations},
 	booktitle = {Proceedings of IEEE Conference on Computer Vision and Pattern Recognition (CVPR)},
 	month = June,
 	year = {2016} 
  }

Please note that we do not own the copyrights to these images. Their use is RESTRICTED to non-commercial research and educational purposes.

========================
Change Log
========================

Version 1.0, released on 18/07/2016
Version 1.1, released on 29/08/2016, add item description annotations
Version 1.2, released on 22/12/2016, add landmarks annotations
Version 1.3, released on 28/06/2017, add attribute annotations
Version 2.0, released on 11/03/2020, add segmentation mask and dense pose annotations

========================
File Information
========================

- Images (Img/)
    52,712 in-shop clothes images (~200,000 cross-pose/scale pairs). See IMAGE section below for more info.

- Bounding Box Annotations (Anno/list_bbox_inshop.txt)
    bounding box labels. See BBOX LABELS section below for more info.

- Fashion Landmark Annotations (Anno/list_landmarks_inshop.txt)
	fashion landmark labels. See LANDMARK LABELS section below for more info.

- Item Annotations (Anno/list_item_inshop.txt)
	item labels. See ITEM LABELS section below for more info.

- Description Annotations (Anno/list_description_inshop.json)
	item descriptions. See DESCRIPTION LABELS section below for more info.

- Attribute Annotations (Anno/attributes/list_attr_cloth.txt & Anno/attributes/list_attr_items.txt & Anno/attributes/list_color_cloth.txt)
	clothing attribute labels. See ATTRIBUTE LABELS section below for more info.

- Segmentation Mask Annotations (Anno/segmentation/DeepFashion_instances_train.json & Anno/segmentation/DeepFashion_instances_query.json & Anno/segmentation/DeepFashion_instances_gallery.json)
	clothing segmentation mask labels. See SEGMENTATION LABELS section below for more info.

- Dense Pose Annotations (Anno/densepose/img_iuv.zip)
	clothing dense pose labels. See DENSEPOSE LABELS section below for more info.

- Evaluation Partitions (Eval/list_eval_partition.txt)
	image names for training, validation and testing set respectively. See EVALUATION PARTITIONS section below for more info.

=========================
New Directories
=========================

- frontend/
  Contains the React frontend code for the WardrobeWhiz application.

- src/
  Contains the backend code, data processing scripts, and models for the WardrobeWhiz application.

- sampleInputImages/
  Contains sample images for testing the WardrobeWhiz application.


=========================
Installation
=========================

### Backend Installation

1. Navigate to the `src` directory:
- cd src

2. if your using a virtual enviroment, activate it with:
On Windows:
- venv\Scripts\activate
On macOS and Linux:
- source venv/bin/activate

4. Install the required Python packages:
- pip install Flask
- pip install flask-cors
- pip install numpy 
- pip install tensorflow
- pip install opencv-python
- pip install scikit-learn
- pip install spacy
- pip install transformers
- pip install torch
- pip install pillow
- pip install webcolors

5. Download en_core_web_sm model:
- python -m spacy download en_core_web_sm

6. Run app.py file:
- python app.py


### Frontend Installation
1. Navigate to the frontend directory:
- cd frontend

2. Install the required Node.js packages:
- npm install

=========================
Contact
=========================

Please contact Ziwei Liu (lz013@ie.cuhk.edu.hk) for questions about the dataset.

For questions about the WardrobeWhiz application, please contact Matilda Deakin at m.d@sky.com.
