import streamlit as st
import pandas as pd

st.title('Analyses et corrélations')

st.write("Dataset cars")

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# Here we use "magic commands":
df_cars

# st.line_chart(df_cars['MAX_TEMPERATURE_C'])