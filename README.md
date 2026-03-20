# Credit Risk Modelling

## Overview
This project implements a machine learning-based Credit Risk Modelling system to classify loan applicants into different risk categories based on their financial and behavioral data. The goal is to assist financial institutions in making better lending decisions by predicting the creditworthiness of applicants.

The model categorizes customers into multiple risk levels (e.g., P1, P2, P3, P4), where lower categories represent higher creditworthiness and lower default risk.

---

## Problem Statement
Financial institutions face challenges in identifying high-risk borrowers due to large volumes of data and complex relationships between financial attributes. This project aims to build a predictive model that classifies customers based on their likelihood of default using historical credit data.

---

## Dataset Description
The dataset consists of customer financial and behavioral attributes, including:

- Demographics (Age, Gender, Marital Status)
- Financial attributes (Income, loan-related features)
- Credit behavior (delinquencies, payment history)
- Loan enquiry details
- Target variable: `Approved_Flag`

Key observations:
- Multiple categorical and numerical features
- Missing values represented using placeholders
- Class imbalance in risk categories

---

## Project Workflow

### Data Preprocessing
- Handling missing values
- Removing irrelevant features
- Encoding categorical variables
- Normalizing numerical features

### Exploratory Data Analysis (EDA)
- Distribution analysis
- Feature correlation analysis
- Relationship between features and target variable

### Feature Selection
- Statistical tests (Chi-Square, ANOVA)
- Removal of redundant features
- Selection of significant predictors

### Model Building
Machine learning models used:
- Random Forest Classifier
- XGBoost Classifier

### Model Evaluation
Evaluation metrics used:
- Accuracy
- Precision
- Recall
- F1 Score

---

## Results

- XGBoost achieved higher accuracy compared to Random Forest
- Model accuracy significantly improved when credit-related features were included
- Multi-class classification successfully separates customers into risk categories
- Performance drops when key financial indicators are removed, showing their importance

---

## Key Insights

- Credit score and repayment history are strong predictors of loan approval
- Certain categories (e.g., mid-risk customers) are harder to classify accurately
- Feature selection significantly improves model performance
- Ensemble methods outperform basic models

---

## Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- Matplotlib
- Seaborn

---
