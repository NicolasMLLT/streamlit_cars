import streamlit as st
import pandas as pd

link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)

# Here we use "magic commands":
df_cars

def filter_by_region(data, region):
    return data[data['continent'] == region]

import seaborn as sns
import matplotlib.pyplot as plt

def plot_correlation(data):
    corr = data.corr()
    plt.figure(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
    plt.show()

def plot_distribution(data, column):
    plt.figure(figsize=(10, 6))
    sns.histplot(data[column], kde=True)
    plt.show()

# Titre de l'application
st.title("Analyse des voitures par région")

# Sélection de la région
region = st.selectbox("Sélectionnez la région", options=["US.", "Europe.", "Japan."])

# Filtrage des données par région
filtered_data = data[data['continent'] == region]

# Affichage des données filtrées
st.write(f"Nombre de voitures dans la région {region}: {len(filtered_data)}")
st.dataframe(filtered_data)

# Analyse de corrélation
st.header("Matrice de corrélation")
corr = filtered_data.corr()
plt.figure(figsize=(10, 8))
sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
st.pyplot(plt)

# Analyse de distribution
st.header("Analyse de distribution")
column = st.selectbox("Sélectionnez la colonne pour l'analyse de distribution", options=filtered_data.columns)
plt.figure(figsize=(10, 6))
sns.histplot(filtered_data[column], kde=True)
st.pyplot(plt)
