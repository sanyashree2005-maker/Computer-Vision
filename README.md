📷 Computer Vision & Image Processing Pipeline (OpenCV)

📌 Overview

This repository demonstrates a complete classical computer vision pipeline implemented using Python and OpenCV.
The project was created to understand how visual data flows through each stage of image processing, from raw image acquisition to basic object classification.

🎯 Objective

To learn and implement the end-to-end computer vision pipeline by applying individual image processing techniques such as image acquisition, preprocessing, segmentation, feature extraction, feature matching, post-processing, and simple object classification.

📝 Description

This project focuses on understanding the fundamental workflow of computer vision systems rather than building a single end application. Each Python file represents one stage of the vision pipeline and is designed to be executed sequentially.

The pipeline begins with image acquisition from a webcam or image file. The acquired image is then preprocessed using grayscale conversion, noise reduction, and contrast enhancement. Segmentation techniques are applied to separate objects from the background. Feature extraction and matching are performed using ORB descriptors, followed by post-processing techniques such as Non-Maximum Suppression to refine detections. Finally, a basic contour-based classification is used to label objects based on area.

This project serves as a strong foundation for understanding classical image processing concepts and prepares the ground for advanced deep learning-based vision systems.

📂 Files Overview (Pipeline Order)

01_image_acquisition.py      → Capture image from webcam or file

02_preprocessing.py          → Grayscale conversion, denoising, enhancement

03_segmentation.py           → Thresholding and contour detection

04_feature_extraction.py     → ORB keypoint and descriptor extraction

05_feature_matching.py       → Feature matching using BFMatcher

06_post_processing.py        → Non-maximum suppression

07_object_classification.py  → Area-based contour classification

🛠️ Technologies Used

* Python
* OpenCV
* NumPy

📌 Learning Outcomes

* Understanding of classical computer vision pipelines
* Hands-on experience with OpenCV image processing
* Practical knowledge of feature extraction and segmentation techniques

🚀 Future Enhancements

* Replace classical methods with CNN-based detectors
* Add face recognition or object detection models
* Improve robustness under varying lighting conditions
 ⭐ Note

This repository is intended for educational purposes to demonstrate the conceptual flow of computer vision systems.




