# Face Mask Detection using YOLOv8

This project implements a YOLOv8-based object detection system to identify whether individuals are wearing face masks. The model is trained on a custom dataset sourced from Roboflow.

---

## Project Structure

face-mask-detection/<br>
├── Face Mask Detection Dataset # Zipped Roboflow dataset<br>
├── Mask_Detection_YOLOv8.ipynb # Jupyter Notebook for training<br>
├── mask_detection.py # Script to run webcam<br>
├── Results/ # Sample input/output images<br>
├── best.pt # Trained weights<br>
├── requirements.txt # Required Python packages<br>
└── README.md # Project documentation<br>

## Dataset

The dataset is provided by Roboflow. You can download it directly using the link below:

https://universe.roboflow.com/uk-zychs/face-mask-detection-oryic/dataset/1#

## Results

| **Metric**     | **Value** |
|----------------|-----------|
| Precision      | 0.904     |
| Recall         | 0.893     |
| mAP@0.5        | 0.935     |
| mAP@0.5:0.95   | 0.675     |


