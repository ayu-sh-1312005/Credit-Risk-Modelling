# 🚀 ML-Based Credit Risk Modelling

🔗 **Live App:** https://ml-based-credit-risk-modelling.streamlit.app/

---

## 📌 Overview

This project is a **Machine Learning-based Credit Risk Prediction System** that helps financial institutions assess whether a loan applicant is likely to **default or not**.

Using historical loan data and advanced ML techniques, the model predicts **creditworthiness**, enabling better decision-making and risk mitigation.

---

## 🎯 Key Features

✨ User-friendly interactive web app
📊 Real-time prediction of loan default risk
🤖 Machine Learning model with preprocessing pipeline
📈 Feature scaling and transformation included
⚡ Fast and lightweight deployment using Streamlit

---

## 🧠 Tech Stack

* **Python**
* **NumPy & Pandas** (Data Processing)
* **Scikit-learn** (ML Models & Preprocessing)
* **XGBoost** (Advanced Boosting Model)
* **Streamlit** (Web App Deployment)
* **Joblib** (Model Serialization)

---

## 🏗️ Project Structure

```
Credit Risk Modelling/
│
├── main.py                      # Streamlit app
├── prediction_helper.py         # Prediction pipeline
├── artifacts/
│   └── model_data.joblib        # Trained model & scaler
├── requirements.txt
└── README.md
```

---

## ⚙️ How It Works

1. User inputs applicant details
2. Data is preprocessed using trained scaler
3. Model predicts probability of default
4. Result is displayed instantly

---

## 🖥️ Run Locally

```bash
# Clone the repository
git clone https://github.com/ayu-sh-1312005/Credit-Risk-Modelling.git

# Navigate to project folder
cd Credit-Risk-Modelling

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run "Credit Risk Modelling/main.py"
```

---

## 📊 Model Details

* Algorithm: **XGBoost Classifier**
* Features: Financial & behavioral attributes
* Output: **Binary Classification (Default / No Default)**

---

## 🌐 Deployment

The app is deployed using **Streamlit Cloud**:

👉 https://ml-based-credit-risk-modelling.streamlit.app/

---

## 📸 Screenshots

*(Add screenshots here for better presentation)*

---

## 🚀 Future Improvements

* 📉 Add model explainability (SHAP)
* 📊 Dashboard with analytics
* 🔐 User authentication system
* ☁️ API deployment (FastAPI)

---

## 🤝 Contributing

Contributions are welcome! Feel free to fork the repo and submit a pull request.

---

## 📜 License

This project is open-source and available under the MIT License.

---

## 👨‍💻 Author

**Ayush Gupta**
📍 Computer Science Engineer | Data Science Enthusiast

---

⭐ If you like this project, don’t forget to **star the repo!**
