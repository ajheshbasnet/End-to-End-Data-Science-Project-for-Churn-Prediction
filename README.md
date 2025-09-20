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

## 📂Project Structure

```plaintext
├── .dvc                   # Data Version Control files
├── .github/workflows       # GitHub Actions CI workflows
├── data                    # Contains datasets
├── data_dump/files/md5     # Metadata related to the datasets
├── models                  # Trained machine learning models
├── src                     # Source code for data processing and models
│   ├── inference.py        # Model inference logic
│   ├── main.ipynb          # Jupyter notebook for data analysis
│   └── index.html          # HTML template for UI
├── testing                 # Unit and integration tests
├── .dvcignore              # DVC tracking exclusions
├── .gitignore              # Git ignore file
├── README.md               # Project overview and documentation
├── data.dvc                # Data version control tracking
├── dvc_workflow.txt        # DVC workflow configuration
├── requirements.txt        # Python dependencies
└── setup.py                # Setup script



---

## 🚀 Setup & Run Locally

1. Clone the repository:

   ```bash
   git clone https://github.com/ajheshbasnet/End-to-End-Data-Science-Project-for-Churn-Prediction.git
   cd End-to-End-Data-Science-Project-for-Churn-Prediction

- pip install -r requirements.txt
- uvicorn src.inference:app --host 0.0.0.0 --port 8000
- Open http://127.0.0.1:8000/ in your browser.

