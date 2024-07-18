import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Fonction pour filtrer par région
def filter_by_region(data, region):
    data['continent'] = data['continent'].str.strip()
    return data[data['continent'].str.contains(region, case=False, na=False)]

# Fonction pour tracer la matrice de corrélation
def plot_correlation(data):
    if data.empty:
        st.write("Aucune donnée disponible pour cette région.")
    else:
        # Sélectionner uniquement les colonnes numériques
        numeric_data = data.select_dtypes(include='number')
        if numeric_data.shape[1] < 2:
            st.write("Pas assez de colonnes numériques pour afficher la corrélation.")
        else:
            corr = numeric_data.corr()
            fig, ax = plt.subplots(figsize=(10, 8))
            sns.heatmap(corr, annot=True, cmap='coolwarm', vmin=-1, vmax=1, ax=ax)
            st.pyplot(fig)

# Fonction pour tracer la distribution
def plot_distribution(data, column):
    if data.empty:
        st.write("Aucune donnée disponible pour cette région.")
    else:
        fig, ax = plt.subplots(figsize=(10, 6))
        sns.histplot(data[column], kde=True, ax=ax)
        st.pyplot(fig)

# Titre de l'application
st.title("Analyse des voitures par région")

# Chargement des données
uploaded_file = st.file_uploader("Choisissez un fichier CSV", type="csv")
if uploaded_file is not None:
    data = pd.read_csv(uploaded_file)
    st.write("Fichier chargé avec succès.")
    st.write(data.head())  # Afficher les premières lignes pour vérifier le contenu

    # Vérifier les valeurs uniques de la colonne 'continent'
    st.write("Valeurs uniques dans la colonne 'continent':")
    st.write(data['continent'].unique())

    # Sélection de la région
    region = st.selectbox("Sélectionnez la région", options=["US", "Europe", "Japan"])

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
else:
    st.write("Veuillez télécharger un fichier CSV.")
