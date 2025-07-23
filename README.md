# Sleep-deprivation
An supervised ML mini project that profiles users into wellness clusters based on their sleep and lifestyle with a working Streamlit app that maps user input to meaningful clusters 


# 🧠 Sleep & Wellness Profiler

An interactive Streamlit app that clusters individuals based on their sleep, stress, lifestyle, and health indicators using unsupervised machine learning.

## 🚀 Overview

This project uses KMeans Clustering to identify wellness groups among participants based on:
- Sleep patterns (duration, quality, sleepiness)
- Lifestyle factors (caffeine intake, physical activity)
- Physical health (BMI, age)
- Stress levels

It was built entirely from scratch using Python, visualized and analyzed in Jupyter/Colab, and deployed as an interactive Streamlit app.

## 💻 Demo


## 📂 Files in This Repository

| File                | Description                                      |
|---------------------|--------------------------------------------------|
| `app.py`            | Streamlit frontend for the wellness profiler     |
| `scaler.pkl`        | Trained StandardScaler used to normalize input   |
| `kmeans_model.pkl`  | Trained KMeans clustering model (k=2)            |
| `SleepWellness.ipynb` | Full notebook with EDA, feature engineering, modeling |
| `requirements.txt`  | Python dependencies for the project              |
| `README.md`         | You’re reading it!                               |

## 📊 Tech Stack

- Python
- Pandas, NumPy
- Scikit-learn
- Streamlit
- Joblib

## 📈 Clustering Insights

- Optimal number of clusters (k=2) determined using Elbow Method and Silhouette Score
- Group 0: Balanced Sleep & Lifestyle 😴💪
- Group 1: At Risk / Sleep-Deprived ⚠️

## 🧠 Future Enhancements

- Add cognitive performance features back in
- Improve clustering accuracy with more robust features
- Add SHAP-based insights to explain cluster separation

---

## 🔧 How to Run Locally

```bash
pip install -r requirements.txt
streamlit run app.py
