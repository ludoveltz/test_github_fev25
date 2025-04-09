import trimesh
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import open3d as o3d
import os

class CADToGraph:
    def __init__(self, file_path):
        """
        Initialise le convertisseur avec le chemin du fichier 3D
        """
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Le fichier {file_path} n'existe pas")
            
        self.file_path = file_path
        self.mesh = None
        self.graph = nx.Graph()
        
    def load_mesh(self):
        """
        Charge le maillage 3D à partir du fichier
        """
        try:
            # Vérification de l'extension du fichier
            file_ext = os.path.splitext(self.file_path)[1].lower()
            if file_ext not in ['.stl', '.obj']:
                raise ValueError(f"Format de fichier non supporté: {file_ext}. Formats supportés: .stl, .obj")
                
            self.mesh = trimesh.load(self.file_path)
            
            # Vérification que le maillage est valide
            if not self.mesh.is_watertight:
                print("Attention: Le maillage n'est pas étanche (watertight)")
                
            if len(self.mesh.vertices) == 0 or len(self.mesh.faces) == 0:
                raise ValueError("Le maillage est vide")
                
            print(f"Maillage chargé avec succès: {len(self.mesh.vertices)} sommets, {len(self.mesh.faces)} faces")
            return True
            
        except Exception as e:
            print(f"Erreur lors du chargement du maillage: {str(e)}")
            return False
            
    def create_graph(self):
        """
        Crée un graphe à partir du maillage
        """
        if self.mesh is None:
            print("Veuillez d'abord charger un maillage")
            return False
            
        try:
            # Réinitialisation du graphe
            self.graph = nx.Graph()
            
            # Ajout des sommets au graphe
            for i, vertex in enumerate(self.mesh.vertices):
                self.graph.add_node(i, pos=vertex)
                
            # Ajout des arêtes entre les sommets connectés
            for face in self.mesh.faces:
                for i in range(3):
                    self.graph.add_edge(face[i], face[(i+1)%3])
                    
            print(f"Graphe créé avec {self.graph.number_of_nodes()} nœuds et {self.graph.number_of_edges()} arêtes")
            return True
            
        except Exception as e:
            print(f"Erreur lors de la création du graphe: {str(e)}")
            return False
        
    def visualize(self, save_path=None):
        """
        Visualise le graphe 3D
        Args:
            save_path (str, optional): Chemin pour sauvegarder l'image
        """
        if self.graph.number_of_nodes() == 0:
            print("Le graphe est vide")
            return
            
        try:
            # Création de la figure 3D
            fig = plt.figure(figsize=(10, 10))
            ax = fig.add_subplot(111, projection='3d')
            
            # Récupération des positions des nœuds
            pos = nx.get_node_attributes(self.graph, 'pos')
            node_xyz = np.array([pos[node] for node in self.graph.nodes()])
            
            # Affichage des nœuds
            scatter = ax.scatter(node_xyz[:, 0], node_xyz[:, 1], node_xyz[:, 2], 
                               c='b', marker='o', s=50)
            
            # Affichage des arêtes
            for edge in self.graph.edges():
                x = [pos[edge[0]][0], pos[edge[1]][0]]
                y = [pos[edge[0]][1], pos[edge[1]][1]]
                z = [pos[edge[0]][2], pos[edge[1]][2]]
                ax.plot(x, y, z, 'r-', alpha=0.5, linewidth=1)
                
            # Configuration de la visualisation
            ax.set_xlabel('X')
            ax.set_ylabel('Y')
            ax.set_zlabel('Z')
            plt.title("Visualisation du graphe 3D")
            
            # Sauvegarde de l'image si demandé
            if save_path:
                plt.savefig(save_path, dpi=300, bbox_inches='tight')
                print(f"Image sauvegardée: {save_path}")
                
            plt.show()
            
        except Exception as e:
            print(f"Erreur lors de la visualisation: {str(e)}")

def main():
    # Exemple d'utilisation
    try:
        # Vérification des arguments en ligne de commande
        import sys
        if len(sys.argv) > 1:
            file_path = sys.argv[1]
        else:
            file_path = "example.stl"  # Fichier par défaut
            
        converter = CADToGraph(file_path)
        if converter.load_mesh():
            if converter.create_graph():
                converter.visualize()
                
    except Exception as e:
        print(f"Erreur: {str(e)}")

if __name__ == "__main__":
    main() 