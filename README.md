# End-to-End Data Science Project for Churn Prediction

## Overview

This project demonstrates a complete machine learning pipeline for predicting customer churn in the banking sector, focusing on European customers from France, Germany, and Spain. The solution integrates model development, version control, performance tracking, and deployment into a cohesive workflow.

---

## 🔧 Technologies & Tools

- **Backend:** FastAPI
- **Frontend:** HTML, CSS, JavaScript
- **Model:** Random Forest Classifier (RFC)
- **Metrics Tracking:** Weights & Biases (W&B)
- **Data & Model Versioning:** DVC (Data Version Control)
- **Testing:** pytest
- **Deployment:** Render.com

---

## 📈 Model Performance

- **Model:** Random Forest Classifier (RFC)
- **Accuracy:** ~89% on validation data
- **Features:** One-hot encoded `Country` (France, Germany, Spain) and `Gender` (Female, Male)

---


---

## 🚀 Setup & Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/ajheshbasnet/End-to-End-Data-Science-Project-for-Churn-Prediction.git
   cd End-to-End-Data-Science-Project-for-Churn-Prediction

pip install -r requirements.txt
uvicorn src.inference:app --host 0.0.0.0 --port 8000
Open http://127.0.0.1:8000/ in your browser.

