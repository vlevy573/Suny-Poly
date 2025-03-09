import streamlit as st
import plotly.express as px
import pandas as pd

# Title of the app
st.title("University Student Enrollment Dasbhaord")

# Load Data
df_uni=pd.read_csv('university_student_dashboard_data(1).csv')

# Retention Rate line plot
fig1 = px.line(df_uni, x='Year', y='Retention Rate (%)', title ='Student Retention Rates over Time')

# Retention Rate line plot
fig2 = px.line(df_uni, x='Year', y='Student Satisfaction (%)', title ='Student Satisfaction Rates over Time')

# Display the Plotly chart in Streamlit
st.plotly_chart(fig1)
st.plotly_chart(fig2)
