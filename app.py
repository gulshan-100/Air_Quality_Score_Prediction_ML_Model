import streamlit as st
import joblib
import numpy as np

# Load the trained model
model = joblib.load("AIR_QUALITY_PREDICTION_MODEL.pkl")


def main():
    st.header('AIR QUALITY SCORE PREDICTION MODEL')
    
    # User input fields
    AQI = st.text_input("AQI")
    PM10 = st.text_input("PM10")
    PM2_5  = st.text_input("PM2.5")
    NO2 = st.text_input("NO2")
    SO2 = st.text_input("SO2")
    O3 = st.text_input("O3")
    Temperature = st.text_input("Temperature")
    Humidity = st.text_input("Humidity")
    Windspeed = st.text_input('Windspeed')
    RespiratoryCases = st.text_input("RespiratoryCases")
    CardiovascularCases  = st.text_input("CardiovascularCases")
    HospitalAdmissions = st.text_input("HospitalAdmissions")
    
    # Convert inputs to float (assuming they are numerical inputs)
    try:
        AQI = float(AQI) if AQI else 0.0
        PM10 = float(PM10) if PM10 else 0.0
        PM2_5 = float(PM2_5) if PM2_5 else 0.0
        NO2 = float(NO2) if NO2 else 0.0
        SO2 = float(SO2) if SO2 else 0.0
        O3 = float(O3) if O3 else 0.0
        Temperature = float(Temperature) if Temperature else 0.0
        Humidity = float(Humidity) if Humidity else 0.0
        Windspeed = float(Windspeed) if Windspeed else 0.0
        RespiratoryCases = float(RespiratoryCases) if RespiratoryCases else 0.0
        CardiovascularCases = float(CardiovascularCases) if CardiovascularCases else 0.0
        HospitalAdmissions = float(HospitalAdmissions) if HospitalAdmissions else 0.0
    except ValueError:
        st.error("Please enter valid numerical inputs.")
        return
    
    # Create input array for prediction
    input_data = np.array([[AQI, PM10, PM2_5, NO2, SO2, O3, Temperature, Humidity, Windspeed, 
                            RespiratoryCases, CardiovascularCases, HospitalAdmissions]])
    
    # Make prediction
    prediction = model.predict(input_data)
    
    # Display prediction
    st.subheader("Prediction:")
    st.write(f"Predicted AQI: {prediction[0]}")

if __name__ == '__main__':
    main()
