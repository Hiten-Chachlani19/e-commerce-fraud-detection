# 🛡️ E-Commerce Credit Card Fraud Detection System

An end-to-end Machine Learning web application designed to detect fraudulent credit card transactions in real-time. Built using **Data Mining techniques**, **Random Forest Classifier**, **Flask REST API**, and a modern **Responsive Frontend Dashboard**.

---

## 📌 Features

* **Real-time Fraud Prediction:** Instant risk scoring and classification (Safe vs. Fraudulent).
* **Synthetic Dataset Generation:** Automated pipeline simulating real-world e-commerce transaction patterns with class imbalance handling.
* **Balanced ML Model:** Powered by Random Forest algorithm fine-tuned for high precision and recall on fraud cases.
* **RESTful Backend API:** Lightweight Flask API with CORS support for seamless client-server interaction.
* **Modern Web Interface:** Dark-themed responsive dashboard for easy transaction parameters testing.

---

## 📂 Project Architecture

```text
ecommerce-fraud-detection/
│
├── dataset/
│   ├── generate_dataset.py     # Synthetic data generation script
│   └── fraud_dataset.csv       # Dataset generated
│
├── model/
│   ├── train_model.py          # Training and model evaluation script
│   └── fraud_model.pkl        # Serialized trained model
│
├── backend/
│   ├── app.py                  # Flask API server
│   └── requirements.txt        # Python dependencies
│
└── frontend/
    ├── index.html              # Dashboard UI
    ├── style.css               # Styling rules
    └── script.js               # API integration logic