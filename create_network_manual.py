#!/usr/bin/env python3
from my_torch.network import Network
from my_torch.layers import Layer
from my_torch.activations import Tanh, Softmax, Sigmoid, ReLU
from my_torch.loss import CategoricalCrossEntropy

def create_chess_network():
    net = Network()
    
    # Couche d'entrée : 65 neurones (64 cases + 1 trait)
    # Couche cachée 1 : 128 neurones
    net.add(Layer(65, 128))
    net.add(ReLU())
    
    # Couche cachée 2 : 64 neurones
    net.add(Layer(128, 64))
    net.add(ReLU())
    
    # Couche de sortie : 3 neurones (Checkmate, Check, Nothing)
    net.add(Layer(64, 3))
    net.add(Softmax())
    
    # On utilise la CrossEntropy pour la classification
    net.use_loss(CategoricalCrossEntropy())
    
    return net

if __name__ == "__main__":
    net = create_chess_network()
    net.save("my_torch_network.nn")
    print("Réseau 'my_torch_network.nn' créé avec succès (65 inputs -> 128 -> 64 -> 3 outputs).")
