import streamlit as st
import pandas as pd
import numpy as np
import joblib # To save and load the model


def predict_resale_value(model, car_features):
    car_df = pd.DataFrame([car_features])
    car_df = pd.get_dummies(car_df, drop_first=True)

    # Ensure consistent column order and handle missing columns with zeros
    # x_train is available from the executed cells in the notebook
    aligned_car_df = pd.DataFrame(columns=x_train.columns)
    aligned_car_df = pd.concat([aligned_car_df, car_df], ignore_index=True)
    aligned_car_df = aligned_car_df.fillna(0)

    prediction = model.predict(aligned_car_df)
    return prediction[0]


st.title('Car Resale Value Prediction')
st.write('Enter the details of the car to predict its resale value.')

# Input widgets for car features
year = st.slider('Year of Manufacture', min_value=1990, max_value=2025, value=2015)
kms_driven = st.number_input('Kilometers Driven', min_value=0, max_value=500000, value=50000)
fuel_type = st.selectbox('Fuel Type', ['Petrol', 'Diesel', 'CNG'])
transmission = st.selectbox('Transmission Type', ['Manual', 'Automatic'])
owner = st.number_input('Number of Previous Owners', min_value=0, max_value=10, value=0)

car_details = {
    'Year': year,
    'Kms_Driven': kms_driven,
    'Fuel_Type': fuel_type,
    'Transmission': transmission,
    'Owner': owner
}

if st.button('Predict Resale Value'):
    try:
        predicted_value = predict_resale_value(best_model, car_details)
        st.success(f"Predicted Resale Value: {predicted_value:.2f} lakhs")
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
