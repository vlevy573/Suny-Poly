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

st.metric("Average Hours Worked", f"{df['Hours Worked'].mean():.1f} hrs")
st.metric("Total Tasks Completed", df['Tasks Completed'].sum())

with col1:
    st.plotly_chart(fig1, use_container_width=True)  # First plot in first column
    st.metric("Retention Rate This Term", df_uni[(df_uni['Year']=='2024','Retention Rate (%)')].mean())

with col2:
    st.plotly_chart(fig2, use_container_width=True)  # Second plot in second column
    st.metric("Satisfaction Rate This Term", df_uni[(df_uni['Year']=='2024', 'Student Satisfaction (%)')].mean())
