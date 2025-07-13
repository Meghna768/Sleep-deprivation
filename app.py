import streamlit as st
import numpy as np
import pandas as pd
import joblib

# Load model and scaler
kmeans = joblib.load("kmeans_model.pkl")
scaler = joblib.load("scaler.pkl")

st.set_page_config(page_title="🧠 Sleep & Wellness Profiler")
st.title("🧠 Sleep & Wellness Profiler")
st.markdown("Fill out the form below to find out your wellness cluster:")

# Input values (only once!)
sleep_hours = st.slider("Sleep Hours (per night)", 0.0, 12.0, 6.0, key="sleep_hours")
sleep_quality = st.slider("Sleep Quality (1=Poor, 10=Excellent)", 1, 10, 5, key="sleep_quality")
daytime_sleepiness = st.slider("Daytime Sleepiness (1=None, 10=Very High)", 1, 10, 5, key="sleepiness")
stress_level = st.slider("Stress Level (1=None, 10=Very High)", 1, 10, 5, key="stress")
physical_activity = st.slider("Physical Activity (0=Sedentary, 10=Very Active)", 0, 10, 5, key="activity")
caffeine_intake = st.number_input("Caffeine Intake (cups/day)", 0.0, 15.0, 2.0, key="caffeine")
age = st.number_input("Age", 10, 100, 20, key="age")
bmi = st.number_input("BMI", 10.0, 40.0, 22.0, key="bmi")

# Button to predict
if st.button("🧠 Predict My Wellness Group"):
    # Use same column names & order as model was trained on
    user_input = pd.DataFrame([{
        'Sleep_Hours': sleep_hours,
        'Sleep_Quality_Score': sleep_quality,
        'Daytime_Sleepiness': daytime_sleepiness,
        'Age': age,
        'BMI': bmi,
        'Caffeine_Intake': caffeine_intake,
        'Physical_Activity_Level': physical_activity,
        'Stress_Level': stress_level
    }])

    # Scale and predict
    user_input_scaled = scaler.transform(user_input)
    cluster = kmeans.predict(user_input_scaled)[0]

    # Output
    st.markdown("### 🚦 Your Wellness Group:")
    if cluster == 0:
        st.success("✅ You belong to **Group 0**: Balanced Sleep & Lifestyle")
        st.markdown("Keep up your healthy habits! 🧘‍♀️😴🍎")
    else:
        st.error("⚠️ You belong to **Group 1**: At Risk / Sleep-Deprived")
        st.markdown("Try improving your sleep routine, reducing stress, and increasing physical activity.")
