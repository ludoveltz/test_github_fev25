# Convertisseur de fichiers CAO vers Graphes 3D

Ce projet permet de convertir des fichiers 3D (format STL ou OBJ) en graphes géométriques exploitables, où les nœuds représentent les points ou faces et les arêtes représentent les connexions.

## Prérequis

- Python 3.8 ou supérieur
- pip (gestionnaire de paquets Python)

## Installation

1. Clonez ce dépôt :
```bash
git clone https://github.com/votre-username/cad-to-graph-3d.git
cd cad-to-graph-3d
```

2. Installez les dépendances :
```bash
pip install -r requirements.txt
```

## Utilisation

1. Placez votre fichier 3D (STL ou OBJ) dans le répertoire du projet
2. Modifiez le chemin du fichier dans la fonction `main()` du fichier `cad_to_graph.py`
3. Exécutez le script :
```bash
python cad_to_graph.py
```

## Fonctionnalités

- Chargement de fichiers 3D (STL, OBJ)
- Conversion en graphe géométrique
- Visualisation 3D interactive du graphe
- Extraction des coordonnées des sommets et des arêtes

## Structure du projet

```
cad-to-graph-3d/
├── README.md
├── requirements.txt
└── cad_to_graph.py
```

## Exemple

```python
from cad_to_graph import CADToGraph

# Création d'une instance du convertisseur
converter = CADToGraph("mon_modele.stl")

# Chargement du maillage
converter.load_mesh()

# Création du graphe
converter.create_graph()

# Visualisation
converter.visualize()
``` 