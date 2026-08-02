# 🐶🐱 Cats vs Dogs Classification using Transfer Learning (MobileNetV2)

## 📌 Project Overview

This project classifies images of Cats and Dogs using Transfer Learning.

Instead of training a CNN from scratch, we use Google's pretrained MobileNetV2 model trained on ImageNet.

The pretrained model acts as a Feature Extractor while custom Dense layers perform binary classification.

---

# Dataset
Download from Kaggle => https://www.kaggle.com/datasets/shubhamchauhan90/
Cats vs Dogs Dataset

Classes

- Cat
- Dog

Image Size

150 × 150 × 3

---

# Technologies Used

- Python
- TensorFlow
- Keras
- MobileNetV2
- NumPy
- Matplotlib
- Pandas

---

# Project Structure

03_Cats_vs_Dogs_Transfer_Learning

│

├── dataset

│   ├── training_set

│   └── test_set

│

├── notebook

│   └── Transfer_Learning_MobileNetV2.ipynb

│

├── outputs

│   ├── predictions.png

│   └── predictions.csv

│

├── saved_model

│   └── mobilenetv2_cats_dogs.keras

│

├── README.md

└── requirements.txt

---

# Transfer Learning Architecture

Input Image

↓

MobileNetV2 (Frozen)

↓

GlobalAveragePooling2D

↓

Dense (128, ReLU)

↓

Dropout (0.3)

↓

Dense (1, Sigmoid)

↓

Prediction

---

# Features

✔ Transfer Learning

✔ ImageNet Pretrained Weights

✔ Frozen Base Model

✔ EarlyStopping

✔ Accuracy Graph

✔ Loss Graph

✔ Random Predictions

✔ Prediction Confidence

✔ Saved Model

---

# Future Improvements

- Fine-Tuning
- Data Augmentation
- Streamlit Deployment
- FastAPI Deployment
- Docker Deployment

---

# Author

Shubham Chauhan