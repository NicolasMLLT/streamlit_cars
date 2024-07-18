import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fonction pour filtrer par région
def filter_by_region(data, region):
    return data[data['continent'] == region]

# Fonction pour tracer la matrice de corrélation
def plot_correlation(data):
    corr = data.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
    st.pyplot(fig)

# Fonction pour tracer la distribution
def plot_distribution(data, column):
    fig, ax = plt.subplots(figsize=(10, 6))
    sns.histplot(data[column], kde=True, ax=ax)
    st.pyplot(fig)

# Chargement des données
link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
data = pd.read_csv(link)

# Titre de l'application
st.title("Analyse des voitures par région")

# Sélection de la région
region = st.selectbox("Sélectionnez la région", options=["US.", "Europe.", "Japan."])

# Filtrage des données par région
filtered_data = filter_by_region(data, region)

# Affichage des données filtrées
st.write(f"Nombre de voitures dans la région {region}: {len(filtered_data)}")
st.dataframe(filtered_data)

# Analyse de corrélation
st.header("Matrice de corrélation")
plot_correlation(filtered_data)

# Analyse de distribution
st.header("Analyse de distribution")
column = st.selectbox("Sélectionnez la colonne pour l'analyse de distribution", options=filtered_data.columns)
plot_distribution(filtered_data, column)

