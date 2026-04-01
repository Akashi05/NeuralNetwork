import pickle
import numpy as np

class Network:
    def __init__(self):
        self.layers = []
        self.loss_function = None
        self.optimizer = None

    def add(self, layer):
        """Ajoute une couche au réseau"""
        self.layers.append(layer)

    def use_loss(self, loss_function):
        self.loss_function = loss_function

    def use_optimizer(self, optimizer):
        """On attache le mécanicien au réseau"""
        self.optimizer = optimizer

    def forward(self, input_data, training=False):
        """
        training : Si True, active le Dropout.
        """
        sample = input_data
        for layer in self.layers:
            # On vérifie si la couche accepte l'argument 'training' (comme Dropout)
            if hasattr(layer, 'forward') and 'training' in layer.forward.__code__.co_varnames:
                sample = layer.forward(sample, training=training)
            else:
                sample = layer.forward(sample)
        return sample

    def predict(self, input_data):
        return self.forward(input_data)

    def train(self, x_train, y_train, epochs, learning_rate):
        if self.optimizer is None:
            from my_torch.optimizer import SGD
            self.optimizer = SGD(learning_rate)
        else:
            self.optimizer.lr = learning_rate
        
        loss_history = []
        for i in range(epochs):
            error = 0
            for x, y in zip(x_train, y_train):
                # On force x et y à devenir des matrices (1, N) au lieu de vecteurs plats (N,)
                x = np.reshape(x, (1, -1))
                y = np.reshape(y, (1, -1))
                output = self.forward(x, training=True)
                error += self.loss_function.loss(y, output)

                # 2. Backward (Calcul des gradients uniquement)
                grad = self.loss_function.derivative(y, output)
                for layer in reversed(self.layers):
                    # Attention : activation layers (Tanh) n'ont pas besoin de learning_rate
                    # On passe juste le gradient
                    grad = layer.backward(grad)
                # 3. Optimization (Mise à jour des poids)
                # On demande au mécano de passer sur chaque couche
                for layer in self.layers:
                    self.optimizer.update(layer)
            error /= len(x_train)
            loss_history.append(error)
            print(f"Époque {i+1}/{epochs}, Erreur : {error}")
        return loss_history

    def save(self, filename):
        """Sauvegarde le réseau dans un fichier"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)
        print(f"Réseau sauvegardé dans {filename}")

    @staticmethod
    def load(filename):
        """Charge un réseau depuis un fichier"""
        with open(filename, 'rb') as f:
            return pickle.load(f)