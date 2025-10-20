import streamlit as st
import pandas as pd
import pickle
import requests
from io import BytesIO

st.title("📊 Sales Prediction App")
st.write("Predict sales based on advertising spend on YouTube, TikTok, and Instagram.")

# URL ของไฟล์ .pkl บน GitHub (ใช้ raw link)
model_url = "https://raw.githubusercontent.com/Plaikanya/regression_class11/blob/main/model-reg-67130701707.pkl"

# โหลดโมเดลจาก GitHub
response = requests.get(model_url)
model = pickle.load(BytesIO(response.content))

# Input fields
youtube = st.number_input("YouTube Advertising Budget", min_value=0.0, value=50.0)
tiktok = st.number_input("TikTok Advertising Budget", min_value=0.0, value=50.0)
instagram = st.number_input("Instagram Advertising Budget", min_value=0.0, value=50.0)

new_data = pd.DataFrame({
    "youtube": [youtube],
    "tiktok": [tiktok],
    "instagram": [instagram]
})

# Predict
if st.button("Predict Sales"):
    predicted_sales = model.predict(new_data)
    st.success(f"💰 Estimated Sales: {predicted_sales[0]:.2f}")
