import streamlit as st
import pickle
import numpy as np
from datetime import datetime

# Load trained model
with open('car_price_model.pkl', 'rb') as f:
    model = pickle.load(f)

# Page configuration
st.set_page_config(page_title="Car Price Predictor", page_icon="🚗", layout="centered")

# Custom CSS styling
st.markdown("""
    <style>
        .stButton>button {
            background-color: #FF4B4B;
            color: white;
            font-weight: bold;
            padding: 10px 24px;
            border-radius: 8px;
        }
        .stRadio > div {
            flex-direction: row;
        }
        .result-box {
            padding: 1rem;
            background-color: #2E7D32;
            border-radius: 10px;
            color: white;
            text-align: center;
            font-size: 1.5rem;
            margin-top: 20px;
        }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown("<h1 style='text-align: center; color: #FF4B4B;'>🚗 Car Resale Price Predictor</h1>", unsafe_allow_html=True)
st.markdown("<hr style='border: 1px solid #FF4B4B;'>", unsafe_allow_html=True)

# Sidebar Info
st.sidebar.title("ℹ️ About")
st.sidebar.info("""
This app predicts the **resale price** of a used car based on:
- Present Price
- Kilometers Driven
- Fuel Type
- Seller Type
- Transmission
- Owner Count
- Car Age
""")

# User Input
st.markdown("### 🔧 Enter Car Details Below")

col1, col2 = st.columns(2)

with col1:
    present_price = st.number_input("Present Price (in Lakhs ₹)", min_value=0.0, format="%.2f")
    kms_driven = st.number_input("Kilometers Driven", min_value=0)

with col2:
    year = st.number_input("Year of Purchase", min_value=1990, max_value=datetime.now().year)
    owner = st.selectbox("Owner Count", [0, 1, 3])

fuel_type = st.radio("Fuel Type", ["Petrol", "Diesel", "CNG"])
seller_type = st.radio("Seller Type", ["Dealer", "Individual"])
transmission = st.radio("Transmission Type", ["Manual", "Automatic"])

# Prediction logic
if st.button("🚀 Predict Selling Price"):
    car_age = datetime.now().year - year

    # Mappings must match training.py
    fuel_map = {"CNG": 0, "Diesel": 1, "Petrol": 2}
    seller_map = {"Dealer": 0, "Individual": 1}
    trans_map = {"Automatic": 0, "Manual": 1}

    input_features = np.array([[present_price,
                                kms_driven,
                                fuel_map[fuel_type],
                                seller_map[seller_type],
                                trans_map[transmission],
                                owner,
                                car_age]])

    # Make prediction
    predicted_price = model.predict(input_features)[0]

    # Display result
    st.markdown(f"<div class='result-box'>💰 Estimated Selling Price: ₹{round(predicted_price, 2)} Lakhs</div>", unsafe_allow_html=True)

# Footer
st.markdown("---")
st.markdown("<div style='text-align: center; color: gray;'>Made with ❤️ by Pranay</div>", unsafe_allow_html=True)
