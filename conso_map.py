import pandas as pd
import folium
from folium.plugins import HeatMap
import geopandas as gpd

# Charger les données de consommation électrique
consommation_df = pd.read_csv('consommation-corse.csv', delimiter=';')

# Charger les coordonnées des communes et filtrer les valeurs manquantes
coordonnees_df = (
    pd.read_csv('coordonnees-communes-corse.csv', delimiter=';')
    .dropna(subset=['Commune', 'Coordonnées'])
)

# Séparer la colonne 'Coordonnées' en 'Longitude' et 'Latitude' et convertir en float
coordonnees_df[['Longitude', 'Latitude']] = (
    coordonnees_df['Coordonnées'].str.split(',', expand=True).astype(float)
)

# Garder uniquement les colonnes 'Commune', 'Longitude' et 'Latitude'
coordonnees_df = coordonnees_df[['Commune', 'Longitude', 'Latitude']]

# Vérifier les coordonnées
print(coordonnees_df.head())

# Fusionner les données de consommation avec les coordonnées
merged_df = pd.merge(consommation_df, coordonnees_df, on='Commune')

# Vérifier le DataFrame fusionné
print(merged_df.head())

# Charger les données géographiques des communes de Corse
communes = gpd.read_file('cantons-corse.geojson')

# Initialiser la carte centrée sur la Corse (choisir des coordonnées centrales approximatives)
m = folium.Map(location=[42.039604, 9.012893], zoom_start=8)

# Préparer les données pour la carte de chaleur
heat_data = [[row['Longitude'], row['Latitude'], row['consommation_mwh']] for _, row in merged_df.iterrows()]

# Ajouter la carte de chaleur
HeatMap(heat_data).add_to(m)

# Ajouter les zones des communes à la carte
for _, commune in communes.iterrows():
    # Convertir les coordonnées de la géométrie en un format compatible avec Folium
    geo_json = folium.GeoJson(commune['geometry'], style_function=lambda x: {
        'fillColor': 'transparent', 'color': 'blue', 'weight': 1, 'fillOpacity': 0.2
    })
    geo_json.add_to(m)

# Sauvegarder la carte dans un fichier HTML
m.save("carte_conso_corse.html")

# Afficher les premières lignes du DataFrame fusionné pour vérification
print(merged_df[['Commune', 'Latitude', 'Longitude', 'consommation_mwh']].head())
