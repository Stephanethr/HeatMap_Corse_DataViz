# Projet de Visualisation de la Consommation Électrique et de la Population en Corse

## Description

Ce projet vise à visualiser les données de consommation électrique et de population des communes de Corse à l'aide de cartes interactives. Les cartes sont générées avec la bibliothèque Folium, tandis que les données géographiques sont traitées avec GeoPandas.

## Technologies Utilisées

- **Python** : Langage de programmation.
- **Pandas** : Bibliothèque pour la manipulation des données.
- **Folium** : Bibliothèque pour la création de cartes interactives.
- **GeoPandas** : Extension de Pandas pour travailler avec des données géographiques.
- **CSV/GeoJSON** : Formats de fichiers pour les données.

## Fichiers Nécessaires

- `consommation-corse.csv` : Fichier contenant les données de consommation électrique par commune.
- `popu-corse.csv` : Fichier contenant les données de population par commune.
- `coordonnees-communes-corse.csv` : Fichier contenant les coordonnées (latitude et longitude) des communes de Corse.
- `cantons-corse.geojson` : Fichier GeoJSON contenant les limites géographiques des communes de Corse.

## Installation

1. Clonez le dépôt :

   ```bash
   git clone git@github.com:Stephanethr/heatmap-population-consommation-corse.git
   cd heatmap-population-consommation-corse
   
2. Installez les dépendances nécessaires :

  ```bash
  pip install pandas folium geopandas
