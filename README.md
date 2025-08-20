# Fraud Shield - Online Fraud Detection System:
**Live App Link - [Fraud Shield](https://fraudshield.fly.dev)**

## Problem Statment

Online payment fraud is increasing rapidly in e-commerce/banking etc, causing financial losses and security risks for users and businesses. Traditional rule-based detection methods fail to adapt to evolving fraud patterns, creating the need for a smarter, real-time detection system.

## 🚀 Project Overview

The **Online Fraud Detection App** is a real time machine learning-powered solution designed to identify fraudulent transactions. Built with **Streamlit**, it provides an interactive user interface where users can input live transaction details and receive instant fraud predictions. The model analyzes transaction patterns and classifies them as **fraudulent** or **legitimate** based on trained data. This project aims to enhance online security and prevent financial fraud effectively.

## Demo
https://github.com/user-attachments/assets/4a95d80f-96d1-49ca-a806-3364ac437dc3

## ⚙️Technical Details

1. Programming Language: Python
2. Libraries Used: pandas, numpy, matplotlib, seaborn, scikit-learn, XGBoost, imbalanced-learn
3. Techniques Applied:
    Exploratory Data Analysis (EDA) with visualization
    Handling class imbalance using SMOTE & RandomUnderSampler
    Feature engineering and label encoding
    Model training with Logistic Regression, Decision Tree, Random Forest, XGBoost
    Final model: Random Forest Classifier (Recall: 99%, Precision: 94%)
    Model evaluation using Confusion Matrix, ROC-AUC, Classification Report
    Model Export: Saved with Joblib for deployment
4. Deployment: Deployed the app using **DOCKER**

## 📊 How It Works

1. The user inputs transaction details into the **Streamlit** UI.
2. The trained **machine learning model** processes the input.
3. The model predicts whether the transaction is **fraudulent** or **legitimate**.
4. The result is displayed instantly on the web interface.

## 📂 Repository Contents

- **`streamlit app.py`** - The main file to run the Streamlit web application.
- **`model.pkl`** - Pickle file containing the trained machine learning model.
- **`fraud_detection.ipynb`** - Jupyter Notebook showcasing the model training process.
- **`requirements.txt`** - List of required Python dependencies.

