import streamlit as st
import requests
import os

# ⚠️ When running locally
#API_URL = "http://localhost:8000/predict"

# Reads API_HOST env var, defaults to 'loksai-api-svc'
API_HOST = os.getenv("API_HOST", "loksai-api-svc")
API_URL = f"http://{API_HOST}:8000/predict"

st.title("Loksai MLOps Feedback Analyzer")

text = st.text_area("Enter feedback")

if st.button("Analyze"):

    if text.strip() == "":
        st.warning("Please enter some text!")

    else: 
        response = requests.post(API_URL, params={"text": text})

        if response.status_code == 200:
            result = response.json()

            sentiment = result["sentiment"]
        

            st.markdown(
                f"""
                ### 🧠 Prediction Result
                **Sentiment:** `{sentiment.capitalize()}`
                """
            )
        else:
            st.error("Failed to get prediction from API")
