# 🐱🐶 Cats vs Dogs Image Classifier (CNN)

## 📌 Project Overview

This project is a Binary Image Classification project built using a Convolutional Neural Network (CNN).

The model classifies an input image into one of the following classes:

- Cat
- Dog

The project is implemented using TensorFlow and Keras.

---

# Dataset

Training Images

- Cats
- Dogs

Testing Images

- Cats
- Dogs

Image Size

150 × 150 × 3

---

# Technologies Used

- Python
- TensorFlow
- Keras
- NumPy
- Matplotlib
- Pandas

---

# Project Structure

02_Cats_vs_Dogs_Classifier

│

├── dataset   ,( Download from Kaggle: https://www.kaggle.com/datasets/shubhamchauhan90/cat-and-dog 
                     and extract into dataset     )
│ ├── training_set

│ └── test_set

│

├── notebook

│ └── Cats_vs_Dogs_Classifier.ipynb

│

├── outputs

│ ├── prediction_results.png

│ └── prediction_results.csv

│

├── saved_model

│ └── cats_vs_dogs_cnn.keras

│

├── README.md

└── requirements.txt

---

# CNN Architecture

Input Image

↓

Conv2D (32 Filters)

↓

MaxPooling

↓

Conv2D (64 Filters)

↓

MaxPooling

↓

Flatten

↓

Dense (128)

↓

Dense (1, Sigmoid)

↓

Prediction

---

# Features

✔ Dataset Visualization

✔ Image Normalization

✔ CNN Architecture

✔ EarlyStopping

✔ Accuracy & Loss Graphs

✔ Random Image Prediction

✔ Prediction Confidence

✔ Prediction Report (CSV)

✔ Saved CNN Model

---

# Future Improvements

- Transfer Learning

- Data Augmentation

- Streamlit Web App

- Flask/FastAPI Deployment

- Docker Deployment

---

# Author

Shubham Chauhan