import random
from typing import List
import time

class Gene:
    def __init__(self):
        self.value = random.randint(0, 1)
    
    def mutate(self):
        self.value = 1 - self.value
    
    def __str__(self):
        return str(self.value)

class Chromosome:
    def __init__(self):
        self.genes = [Gene() for _ in range(10)]
    
    def mutate(self):
        for gene in self.genes:
            if random.random() < 0.3:  # Réduit la probabilité de mutation
                gene.mutate()
    
    def is_perfect(self):
        return all(gene.value == 1 for gene in self.genes)
    
    def __str__(self):
        return ''.join(str(gene) for gene in self.genes)

class DNA:
    def __init__(self):
        self.chromosomes = [Chromosome() for _ in range(10)]
    
    def mutate(self):
        for chromosome in self.chromosomes:
            if random.random() < 0.3:  # Réduit la probabilité de mutation
                chromosome.mutate()
    
    def is_perfect(self):
        return all(chromosome.is_perfect() for chromosome in self.chromosomes)
    
    def __str__(self):
        return '\n'.join(str(chromosome) for chromosome in self.chromosomes)

class Organism:
    def __init__(self, mutation_probability):
        self.dna = DNA()
        self.mutation_probability = mutation_probability
        self.generation = 0
    
    def mutate(self):
        if random.random() < self.mutation_probability:
            self.dna.mutate()
        self.generation += 1
        return self.dna.is_perfect()

def experience_biologique(nb_organismes: int, mutation_probability: float, max_generations: int = 1000):
    print(f"🧬 Début de l'expérience avec {nb_organismes} organismes")
    print(f"Probabilité de mutation : {mutation_probability}")
    print(f"Nombre maximum de générations : {max_generations}\n")
    
    organismes = [Organism(mutation_probability) for _ in range(nb_organismes)]
    start_time = time.time()
    
    # Ajout d'un compteur de progression
    for generation in range(max_generations):
        if generation % 100 == 0:
            print(f"Generation {generation}...")
            
        for i, organisme in enumerate(organismes):
            if organisme.mutate():
                end_time = time.time()
                duree = end_time - start_time
                
                print(f"\n🎉 Succès ! Organisme parfait trouvé !")
                print(f"Numéro d'organisme : {i + 1}")
                print(f"Nombre de générations : {organisme.generation}")
                print(f"Temps écoulé : {duree:.2f} secondes")
                return
    
    print("\n⚠️ Aucun organisme parfait trouvé après", max_generations, "générations")

if __name__ == "__main__":
    # Paramètres optimisés
    NB_ORGANISMES = 5
    MUTATION_PROBABILITY = 0.3
    MAX_GENERATIONS = 1000  # Limite le nombre de générations
    
    experience_biologique(NB_ORGANISMES, MUTATION_PROBABILITY, MAX_GENERATIONS)
