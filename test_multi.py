import numpy as np
from my_torch.network import Network
from my_torch.layers import Layer
from my_torch.activations import Tanh, Softmax # <-- On importe Softmax
from my_torch.loss import CategoricalCrossEntropy # <-- On importe la nouvelle Loss

def main():
    print("=== TEST MULTI-CLASSES (Rouge/Vert/Bleu) ===")

    # DONNÉES (3 exemples)
    # Exemple 1 : [-1, -1] -> Doit être Classe 0 (Rouge)
    # Exemple 2 : [0, 2]   -> Doit être Classe 1 (Vert)
    # Exemple 3 : [2, 2]   -> Doit être Classe 2 (Bleu)
    
    x_train = np.array([
        [[-1, -1]], 
        [[0, 2]], 
        [[2, 2]]
    ])

    # Encodage "One-Hot" (Un seul 1, le reste des 0)
    y_train = np.array([
        [[1, 0, 0]], 
        [[0, 1, 0]], 
        [[0, 0, 1]]
    ])

    # ARCHITECTURE
    net = Network()
    net.add(Layer(2, 5))    # Couche cachée
    net.add(Tanh())
    net.add(Layer(5, 3))    # 3 Neurones en sortie (car 3 classes !)
    net.add(Softmax())      # Activation Softmax pour avoir des %

    # CONFIGURATION
    # Attention : On utilise CategoricalCrossEntropy ici !
    net.use_loss(CategoricalCrossEntropy())

    # ENTRAÎNEMENT
    print("Entraînement en cours...")
    net.train(x_train, y_train, epochs=1000, learning_rate=0.1)

    # VÉRIFICATION
    print("\n--- RÉSULTATS ---")
    classes = ["Rouge", "Vert", "Bleu"]
    for x, y in zip(x_train, y_train):
        output = net.predict(x)
        # np.argmax nous donne l'index du plus grand nombre (ex: [0.1, 0.8, 0.1] -> index 1)
        pred_index = np.argmax(output)
        true_index = np.argmax(y)
        
        print(f"Entrée {x[0]} :")
        print(f"   Probas : {output[0]}") # Affiche les % bruts
        print(f"   Prédiction : {classes[pred_index]} (Vrai : {classes[true_index]})")
        print("-" * 20)

if __name__ == "__main__":
    main()