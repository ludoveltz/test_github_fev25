# test_numpy.py
import numpy as np

def test_numpy():
    try:
        # Test simple avec un array
        arr = np.array([1, 2, 3, 4, 5])
        print("✅ NumPy est correctement installé!")
        print(f"Version de NumPy: {np.__version__}")
        print(f"Test array: {arr}")
        
        # Test de calcul matriciel (utile pour nos modèles GenAI)
        matrix = np.array([[1, 2], [3, 4]])
        print(f"\nTest de calcul matriciel:")
        print(f"Matrice originale:\n{matrix}")
        print(f"Transposée:\n{matrix.T}")
        
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    test_numpy()
