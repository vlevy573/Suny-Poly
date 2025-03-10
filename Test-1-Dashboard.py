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

# Arrange the plots in a grid layout
col1, col2 = st.columns(2)  # Create 2 columns

with col1:
    st.plotly_chart(fig1, use_container_width=True)  # First plot in first column

with col2:
    st.plotly_chart(fig2, use_container_width=True)  # Second plot in second column
