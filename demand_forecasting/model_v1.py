import streamlit as st
import pandas as pd
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt

st.title("📦 Demand Forecasting Dashboard")

uploaded_file = st.file_uploader("Upload demand CSV (columns: week, demand)", type="csv")

if uploaded_file:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())

    X = df[['week']]
    y = df['demand']

    model = LinearRegression()
    model.fit(X, y)

    future_week = st.number_input("Forecast for week:", min_value=int(df['week'].max()) + 1)
    if st.button("Predict"):
        prediction = model.predict([[future_week]])[0]
        st.success(f"Predicted demand for week {future_week}: {prediction:.2f}")

        # Plot
        fig, ax = plt.subplots()
        ax.plot(df['week'], df['demand'], label='Actual')
        ax.scatter([future_week], [prediction], color='red', label='Prediction')
        ax.set_xlabel("Week")
        ax.set_ylabel("Demand")
        ax.legend()
        st.pyplot(fig)

