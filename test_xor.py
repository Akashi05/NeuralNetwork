import numpy as np

# On importe tes modules
from my_torch.network import Network
from my_torch.layers import Layer
from my_torch.activations import Tanh, Sigmoid
from my_torch.loss import MSE

def main():
    print("=== TEST DU RÉSEAU DE NEURONES (XOR) ===")

    # 1. PRÉPARATION DES DONNÉES
    # X = Les entrées (4 exemples de 2 bits)
    # Forme : (4 exemples, 1 ligne, 2 colonnes)
    x_train = np.array([
        [[0, 0]], 
        [[0, 1]], 
        [[1, 0]], 
        [[1, 1]]
    ])

    # Y = Les réponses attendues
    # Forme : (4 exemples, 1 ligne, 1 colonne)
    y_train = np.array([
        [[0]], 
        [[1]], 
        [[1]], 
        [[0]]
    ])

    # 2. CONSTRUCTION DE L'ARCHITECTURE
    net = Network()

    # Couche Cachée : 2 entrées (x1, x2) -> 3 neurones
    net.add(Layer(2, 3))
    net.add(Tanh())  # Non-linéarité

    # Couche de Sortie : 3 neurones -> 1 sortie (y)
    net.add(Layer(3, 1))
    net.add(Sigmoid())  # Non-linéarité (sortie entre -1 et 1)

    # 3. CONFIGURATION
    net.use_loss(MSE())

    # 4. ENTRAÎNEMENT
    # On lance 1000 cycles d'apprentissage avec un Learning Rate de 0.1
    print("\n--- Début de l'entraînement ---")
    net.train(x_train, y_train, epochs=1000, learning_rate=0.1)

    # 5. VÉRIFICATION
    print("\n--- Résultats Final ---")
    print("Attendu -> Prédit")
    for x, y in zip(x_train, y_train):
        output = net.predict(x)
        # On affiche joliment le résultat
        input_str = str(x[0])
        target_str = str(y[0][0])
        pred_val = output[0][0]
        print(f"Entrée {input_str} : Cible [{target_str}] -> IA [{pred_val:.5f}]")

if __name__ == "__main__":
    main()