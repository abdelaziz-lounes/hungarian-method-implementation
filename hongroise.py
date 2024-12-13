import numpy as np

# Matrices données
# F représente les flux entre les commerces, où F[i][j] est le flux entre commerce i et commerce j.
# D représente les distances entre les emplacements, où D[i][j] est la distance entre emplacement i et emplacement j.
F = np.array([
    [0, 1, 0, 1],
    [1, 0, 0, 2],
    [0, 0, 0, 2],
    [1, 2, 3, 0]
])

D = np.array([
    [0, 4, 3, 5],
    [4, 0, 5, 4],
    [3, 5, 0, 4],
    [5, 4, 4, 0]
])

# Calcul de la matrice de coût C
# Chaque élément de C est le produit de F et D pour déterminer le coût de chaque paire (commerce, emplacement).
C = F * D

# Étape 1 : réduction de lignes
# Pour chaque ligne de C, on soustrait le minimum de cette ligne à tous les éléments de la ligne.
for i in range(len(C)):
    row_min = C[i].min()  # Trouve le minimum de la ligne
    C[i] -= row_min       # Soustrait le minimum de tous les éléments de la ligne

# Étape 2 : réduction de colonnes
# Pour chaque colonne de C, on soustrait le minimum de cette colonne à tous les éléments de la colonne.
for j in range(len(C[0])):
    col_min = C[:, j].min()  # Trouve le minimum de la colonne
    C[:, j] -= col_min       # Soustrait le minimum de tous les éléments de la colonne

# Fonction pour trouver la couverture minimale des zéros
# Cette fonction identifie les lignes et colonnes à couvrir pour contenir tous les zéros de la matrice.
def couverture_zeros(mat):
    # Initialisation des couvertures de lignes et colonnes
    lignes_couvertes = [False] * len(mat)
    colonnes_couvertes = [False] * len(mat[0])
    
    # Parcours de chaque ligne pour identifier les zéros
    for i in range(len(mat)):
        if 0 in mat[i]:  # Si un zéro est trouvé dans la ligne
            lignes_couvertes[i] = True
            for j in range(len(mat[i])):
                if mat[i][j] == 0:
                    colonnes_couvertes[j] = True  # Marque la colonne si elle contient un zéro
    
    return lignes_couvertes, colonnes_couvertes

# Fonction pour ajuster la matrice en fonction des lignes et colonnes couvertes
# Cette fonction ajuste les valeurs de la matrice pour améliorer la couverture des zéros.
def ajuster_matrice(mat, lignes_couvertes, colonnes_couvertes):
    # Sélectionne les éléments non couverts et trouve le minimum parmi eux
    uncovered_elements = [mat[i][j] for i in range(len(mat)) for j in range(len(mat[0]))
                          if not lignes_couvertes[i] and not colonnes_couvertes[j]]
    min_uncovered = min(uncovered_elements) if uncovered_elements else 0
    
    # Ajustement de la matrice : soustrait le minimum des éléments non couverts et ajoute aux éléments couverts deux fois
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            if not lignes_couvertes[i] and not colonnes_couvertes[j]:
                mat[i][j] -= min_uncovered  # Réduit les éléments non couverts
            if lignes_couvertes[i] and colonnes_couvertes[j]:
                mat[i][j] += min_uncovered  # Augmente les éléments couverts deux fois

# Boucle pour ajuster la matrice jusqu'à obtenir la solution optimale
while True:
    lignes_couvertes, colonnes_couvertes = couverture_zeros(C)
    
    # Vérifie si la couverture minimale est suffisante
    if sum(lignes_couvertes) + sum(colonnes_couvertes) >= len(C):
        break  # Si oui, sort de la boucle
    
    # Ajuste la matrice en fonction de la couverture actuelle des lignes et colonnes
    ajuster_matrice(C, lignes_couvertes, colonnes_couvertes)

# Assignation finale en cherchant les zéros dans la matrice ajustée
affectation = []
assigned_commerces = set()  # Ensemble pour suivre les commerces déjà assignés
assigned_emplacements = set()  # Ensemble pour suivre les emplacements déjà assignés

for i in range(len(C)):
    for j in range(len(C[0])):
        # Si un zéro est trouvé et que ni le commerce ni l'emplacement n'ont été assignés
        if C[i][j] == 0 and i not in assigned_commerces and j not in assigned_emplacements:
            affectation.append((i, j))  # Enregistre l'assignation (commerce, emplacement)
            assigned_commerces.add(i)  # Marque le commerce comme assigné
            assigned_emplacements.add(j)  # Marque l'emplacement comme assigné

# Affichage de la solution d'assignation optimale
print("Assignation optimale des commerces aux emplacements :")
for commerce, emplacement in affectation:
    print(f"Commerce c{commerce} -> Emplacement e{emplacement}")

# Calcul du coût total minimal pour l'assignation
cout_total = sum(F[commerce][autre_commerce] * D[emplacement][autre_emplacement]
                 for commerce, emplacement in affectation
                 for autre_commerce, autre_emplacement in affectation)

print("\nCoût total minimal :", cout_total)
