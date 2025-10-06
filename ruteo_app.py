import streamlit as st
import pandas as pd
import networkx as nx
import folium
from streamlit_folium import st_folium

st.title("🧭 Ruteo de Mantenimiento")
st.write("Visualiza y optimiza rutas de mantenimiento entre equipos o plantas.")

# Cargar datos
uploaded_file = st.file_uploader("Sube un archivo Excel con las ubicaciones", type=["xlsx"])

if uploaded_file:
    df = pd.read_excel(uploaded_file)
    st.dataframe(df)

    # Crear grafo de conexiones
    G = nx.Graph()

    for i, row in df.iterrows():
        G.add_node(row["Punto"], pos=(row["Latitud"], row["Longitud"]))

    # Crear mapa base
    first_point = df.iloc[0]
    m = folium.Map(location=[first_point["Latitud"], first_point["Longitud"]], zoom_start=13)

    for i, row in df.iterrows():
        folium.Marker(
            [row["Latitud"], row["Longitud"]],
            popup=row["Punto"],
            icon=folium.Icon(color="blue", icon="wrench", prefix="fa")
        ).add_to(m)

    st_data = st_folium(m, width=700, height=500)
else:
    st.info("Por favor, sube un archivo Excel con columnas: Punto, Latitud, Longitud.")
