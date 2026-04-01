import numpy as np

class Linear:
    def __init__(self, input_size, output_size):
        # Initialisation de He
        self.weights = np.random.randn(input_size, output_size) * np.sqrt(2. / input_size)
        self.bias = np.zeros((1, output_size))
        
        # Stockage pour le backward
        self.input = None
        self.grad_weights = None
        self.grad_bias = None

    def forward(self, input_data, training=False):
        # training=False est là juste pour la compatibilité, on ne s'en sert pas ici
        self.input = input_data
        return np.dot(input_data, self.weights) + self.bias

    def backward(self, output_gradient):
        # Calcul des gradients pour l'optimizer
        self.grad_weights = np.dot(self.input.T, output_gradient)
        self.grad_bias = np.sum(output_gradient, axis=0, keepdims=True)
        # Calcul de l'erreur à propager vers le bas
        input_gradient = np.dot(output_gradient, self.weights.T)
        return input_gradient

class Dropout:
    def __init__(self, probability=0.5):
        self.probability = probability
        self.mask = None

    def forward(self, input_data, training=False):
        if training:
            # On génère un masque aléatoire
            self.mask = np.random.binomial(1, self.probability, size=input_data.shape) / self.probability
            return input_data * self.mask
        else:
            return input_data

    def backward(self, output_gradient):
        return output_gradient * self.mask

Layer = Linear