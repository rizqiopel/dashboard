import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

day_df = pd.read_csv("https://raw.githubusercontent.com/rizqiopel/dataanalis/main/day.csv")

st.title("Bike Sharing Data Analysis Dashboard")

st.set_option('deprecation.showPyplotGlobalUse', False)
st.subheader("Weather Situation vs. Number of Users")
weather_chart = sns.barplot(
    y="cnt", 
    x="weathersit",
    data=day_df.sort_values(by="weathersit", ascending=False)
)
st.pyplot()

st.subheader("Season vs. Number of Users")
weather_chart = sns.barplot(
    y="cnt", 
    x="season",
    data=day_df.sort_values(by="season", ascending=False)
)
st.pyplot()