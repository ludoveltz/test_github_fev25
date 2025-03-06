import tensorflow as tf
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import platform

# Configuration de l'environnement ML
print("Configuration de l'environnement ML:")
print(f"Python: {platform.python_version()}")
print(f"TensorFlow: {tf.__version__}")
print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")

# Données nutritionnelles pour le hackathon
aliments = {
    'Nom': ['Riz', 'Quinoa', 'Lentilles', 'Pois chiches'],
    'Calories': [130, 120, 116, 164],
    'Protéines': [2.7, 4.4, 9.0, 8.9],
    'Fibres': [0.6, 2.8, 7.9, 12.5]
}

# Création du DataFrame
df = pd.DataFrame(aliments)
print("\nDonnées nutritionnelles:")
print(df)

# Préparation des données pour ML
X = np.array(df[['Calories', 'Fibres']])
y = np.array(df['Protéines'])

# Création du modèle
model = tf.keras.Sequential([
    tf.keras.layers.Dense(8, activation='relu', input_shape=(2,)),
    tf.keras.layers.Dense(4, activation='relu'),
    tf.keras.layers.Dense(1)
])

# Compilation et entraînement
model.compile(optimizer='adam', loss='mse', metrics=['mae'])
print("\nEntraînement du modèle nutritionnel:")

history = model.fit(
    X, y,
    epochs=100,
    verbose=0,
    validation_split=0.2
)

# Visualisation des résultats
plt.figure(figsize=(12, 5))

# Graphique de la loss
plt.subplot(1, 2, 1)
plt.plot(history.history['loss'], label='Training Loss')
plt.plot(history.history['val_loss'], label='Validation Loss')
plt.title('Évolution de la Loss')
plt.xlabel('Epoch')
plt.ylabel('Mean Squared Error')
plt.legend()

# Graphique des prédictions vs réalité
plt.subplot(1, 2, 2)
plt.scatter(df['Calories'], df['Protéines'], label='Données réelles')
plt.xlabel('Calories')
plt.ylabel('Protéines (g)')
plt.title('Relation Calories-Protéines')
plt.legend()

plt.tight_layout()
plt.show()

# Test de prédiction
nouveau_aliment = np.array([[150, 5.0]])  # 150 calories, 5g fibres
prediction = model.predict(nouveau_aliment)[0][0]

print(f"\nPrédiction pour un nouvel aliment:")
print(f"Calories: {nouveau_aliment[0][0]}")
print(f"Fibres: {nouveau_aliment[0][1]}g")
print(f"Protéines prédites: {prediction:.1f}g")
