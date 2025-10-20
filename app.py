import streamlit as st
import pandas as pd
import pickle

# Step 1: Load trained model
with open("/content/drive/MyDrive/model-reg-67130701707.pkl", "rb") as file:
    model = pickle.load(file)

# Title
st.title("📊 Sales Prediction App")
st.write("Predict sales based on advertising spend on YouTube, TikTok, and Instagram.")

# Step 2: Input fields
youtube = st.number_input("YouTube Advertising Budget", min_value=0.0, value=50.0)
tiktok = st.number_input("TikTok Advertising Budget", min_value=0.0, value=50.0)
instagram = st.number_input("Instagram Advertising Budget", min_value=0.0, value=50.0)

# Create DataFrame
new_data = pd.DataFrame({
    "youtube": [youtube],
    "tiktok": [tiktok],
    "instagram": [instagram]
})

# Step 3: Predict
if st.button("Predict Sales"):
    predicted_sales = model.predict(new_data)
    st.success(f"💰 Estimated Sales: {predicted_sales[0]:.2f}")
