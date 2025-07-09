
import streamlit as st
import pandas as pd
import plotly.express as px

st.title("Supply Chain Analytics Dashboard")

# Load predictions
df = pd.read_csv('predictions.csv')

# Section 1: Raw Predictions
st.header("Predicted vs Actual Sales")
st.dataframe(df.head())

# Section 2: Scatter Plot
st.header("True vs Predicted Sales")
fig = px.scatter(df, x='Actual', y='Predicted', trendline='ols')
st.plotly_chart(fig)

# Section 3: Residuals
st.header("Residuals Distribution")
df['Residuals'] = df['Actual'] - df['Predicted']
fig = px.histogram(df, x='Residuals', nbins=30)
st.plotly_chart(fig)
