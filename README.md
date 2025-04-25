

## 📘 Project Documentation: Car Price Predictor

### 📄 Overview
This is a comprehensive machine learning project focused on predicting the price of used cars using a dataset from Quikr. It covers the full ML workflow: data cleaning, preprocessing, exploratory analysis, and training predictive models.

---

### 📚 Table of Contents

1. [Introduction](#introduction)
2. [Library Imports](#library-imports)
3. [Data Loading](#data-loading)
4. [Data Cleaning](#data-cleaning)
5. [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
6. [Feature Engineering](#feature-engineering)
7. [Model Building](#model-building)
8. [Evaluation](#evaluation)
9. [Conclusion](#conclusion)

---

### 🧑‍🏫 Introduction

The goal is to build a model that predicts car prices based on features such as the car's year, brand, fuel type, and kilometers driven.

---

### 📦 Library Imports

Standard data science libraries are used in this project:
```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
```

## 🖼️ Project Screenshot

![AI Chatbot Screenshot](https://github.com/zunairanureen/Car-Price-Predictor1/blob/main/Capture.JPG?raw=true)



### 📂 Data Loading

The dataset is loaded from a CSV file:
```python
car = pd.read_csv('/content/quikr_car.csv')
```

---

### 🧹 Data Cleaning

This section handles messy and inconsistent data. Steps include:

- Converting the `year` column to integers and removing non-year values.
- Replacing `'Ask For Price'` with NaNs and converting the `price` column to integers.
- Cleaning the `kms_driven` column by removing "kms" and commas, and converting to integer.
- Filling or removing NaNs in `fuel_type`.
- Keeping only the first three words in the `name` column to generalize car models.

These transformations ensure numerical features are machine-learning-ready.

---

### 📊 Exploratory Data Analysis (EDA)

Basic visualizations include:
- Distribution of car prices.
- Relationship between price and year.
- Box plots to explore categorical features like `fuel_type`.

Correlation analysis helps identify useful predictors.

---

### 🛠️ Feature Engineering

- Categorical encoding is applied (e.g., one-hot encoding for `fuel_type`).
- Irrelevant or highly missing columns are dropped.
- Data is split into training and test sets using `train_test_split`.

---

### 🤖 Model Building

A **Linear Regression** model is trained to predict car prices:
```python
from sklearn.linear_model import LinearRegression
model = LinearRegression()
model.fit(X_train, y_train)
```

Other models (Random Forest, Decision Tree) may also be included for performance comparison.

---

### 📈 Evaluation

Performance metrics include:
- R² Score
- Mean Squared Error (MSE)
- Visualization of predicted vs. actual prices

### Save Model
Use `joblib` or `pickle` to save the trained model:
```python
import joblib
joblib.dump(model, 'car_price_model.pkl')

---
### Create a flask App
- Build a UI to take car inputs and return price prediction.

---

### 🚀Deployment Steps
FOLLOW these Steps:

 Docker Setup In EC2 commands to be Executed


sudo apt-get update -y

sudo apt-get upgrade

#required

curl -fsSL https://get.docker.com -o get-docker.sh

sudo sh get-docker.sh

sudo usermod -aG docker ubuntu

newgrp docker

---

### Configure EC2 as self-hosted runner:
Setup github secrets:
AWS_ACCESS_KEY_ID=

AWS_SECRET_ACCESS_KEY=

AWS_REGION = us-east-1

AWS_ECR_LOGIN_URI = demo>> 566373416292.dkr.ecr.ap-south-1.amazonaws.com

---
ECR_REPOSITORY_NAME = simple-app

Go to Amazon ECR console.

Open your repository (simple-app).

You’ll see the latest image pushed.

### Run Container on EC2
docker pull 566373416292.dkr.ecr.ap-south-1.amazonaws.com/simple-app:latest
docker run -d -p 80:80 simple-app


---




