# ML-Based Car Price Prediction Web App

---

## 🚗 Project Overview

This project implements a machine learning model to predict the resale price of used cars based on various features such as present price, kilometers driven, fuel type, seller type, transmission, owner count, and car age. It includes both:

- A **training pipeline** to preprocess data, train, evaluate, and save the model
- A **Streamlit web application** that allows users to input car details and get real-time resale price predictions

The model is trained on a publicly available car resale dataset and leverages a Random Forest Regressor for accurate price estimation.

---

## 🔍 Features

- Comprehensive data preprocessing including feature engineering and label encoding  
- Model training with Random Forest Regressor and performance evaluation  
- User-friendly Streamlit interface with custom styling  
- Real-time car price prediction based on multiple inputs  
- Easily extendable and modifiable for additional features or datasets  

---

## 🛠️ Technologies Used

- Python  
- Pandas, NumPy for data manipulation  
- scikit-learn for machine learning model development  
- Streamlit for the web application  
- joblib and pickle for model serialization  

---

## 📁 Repository Structure

```
├── app.py                  # Streamlit web app to predict car prices
├── car_price_model.pkl     # Trained Random Forest model
├── car data.csv            # Dataset used for training
├── train_model.py          # Script for training and saving the model
├── requirements.txt        # Project dependencies
└── README.md               # This documentation
```

---

## 🔧 Installation & Setup

1. Clone the repository:  
   ```bash
   git clone https://github.com/Pranaykumar4344/codeX-techno-Project-3
   cd codeX-techno-Project-3
   ```

2. (Optional) Create and activate a virtual environment:  
   ```bash
   python -m venv venv
   source venv/bin/activate    # Linux/Mac
   venv\Scripts\activate     # Windows
   ```

3. Install required packages:  
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 How to Train the Model

If you want to retrain the model with the dataset:

```bash
python model_training.py
```

This will preprocess the data, train a Random Forest model, evaluate its performance, and save the trained model as `car_price_model.pkl`.

---

## 🖥️ How to Run the Web App

After training or if you already have `car_price_model.pkl`, launch the interactive web app:

```bash
streamlit run app.py
```
Alternatively, you can try the live app here:
https://car-price-prediction-ml.streamlit.app/

Enter the car details in the UI and click **Predict Selling Price** to get an estimated resale price in Lakhs ₹.

---

## 📈 Model Details

- Model Type: Random Forest Regressor  
- Features Used:  
  - Present Price (in Lakhs ₹)  
  - Kilometers Driven  
  - Fuel Type (Petrol, Diesel, CNG)  
  - Seller Type (Dealer, Individual)  
  - Transmission (Manual, Automatic)  
  - Owner Count  
  - Car Age (calculated from year of purchase)

- Performance: Mean Squared Error (MSE) reported during training (see console output)

---

## 🤝 Contributions

Contributions, feature requests, and bug reports are welcome! Please open an issue or submit a pull request.

---

## 📫 Contact

Feel free to connect with me on LinkedIn:  
[https://www.linkedin.com/in/pranaykumar-ai-ml](https://www.linkedin.com/in/janapareddi-pranay-kumar-5897a828a/)

---
