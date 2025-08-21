# Fraud Shield - Online Payment Fraud Detection System:
**Live App Link - [Fraud Shield](https://fraudshield.fly.dev)**

## Problem Statment

Online payment fraud's are increasing rapidly, causing financial losses and security risks for users and businesses. Traditional rule-based detection methods fail to adapt to evolving fraud patterns, creating the need for a smarter, real-time detection system.

## 🚀 Project Overview

Our app **FraudShield** is a real time machine learning-powered solution designed to identify fraudulent transactions. This app can help banks, digital wallets or payment platforms to automatically flag suspicious transactions, helping to prevent financial loss. It takes the user inputs passes them to the trained model and returns the probability of fraud and fraud status to the user.

## Demo video
https://github.com/user-attachments/assets/4a95d80f-96d1-49ca-a806-3364ac437dc3

## ⚙️Technical Details

1. Programming Language: Python
2. Libraries Used: pandas, numpy, matplotlib, seaborn, scikit-learn, XGBoost, RandomUnderSampler, SMOTE
3. Techniques Applied:
    - Exploratory Data Analysis (EDA) for identifying fraud patterns
    - Feature engineering and manual label encoding
    - Model training with Logistic Regression, Decision Tree, Random Forest, XGBoost
    - Final model: Random Forest Classifier — achieved 99% recall and 94% precision, with a reduced decision threshold to   capture more fraudulent transactions
    - Model evaluation using, ROC-AUC(0.99), Classification Report
    - Model Export: Saved with the model and its artifacts using Joblib library
4. Deployment: Deployed the app using **DOCKER**

## 📊 How It Works

1. The user inputs transaction details into the **Streamlit** UI.
2. The trained **machine learning model** processes the input.
3. The app uses the trained model in the backend and returns the probability and fraud status based on the inputs.
4. The result is displayed instantly on the web interface.

## 📂 Repository Contents

- **`main.py`** - The main file to run the Streamlit web application.
- **`fraud_detection_model.pkl`** - Pickle file containing the trained machine learning model.
- **`model.ipynb`** - Jupyter Notebook showcasing the model training process.
- **`requirements.txt`** - List of required Python dependencies.
- **`Dockerfile`** - Docker file used fly.io for deployment

