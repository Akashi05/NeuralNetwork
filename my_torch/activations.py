import numpy as np

class Tanh:
    """
    Passe l'information vers l'avant.
    Transforme l'entrée pour qu'elle soit entre -1 et 1.
    """
    def forward (self, input_data):
        self.input = input_data
        return np.tanh(input_data)

    """
    Passe l'information vers l'arrière.
    Calcule la dérivée de Tanh : 1 - tanh(x)^2
    """
    def backward(self, output_gradient):
        # Formule mathématique de la dérivée de tanh
        derivative = 1 - np.power(np.tanh(self.input), 2)
        return np.multiply(output_gradient, derivative)

class Sigmoid:
    def forward(self, input_data):
        self.input = input_data
        self.input = np.clip(self.input, -500, 500)
        self.output = 1 / (1 + np.exp(-self.input))
        return self.output

    def backward(self, output_gradient):
        s = self.output
        derivative = s * (1 - s)
        return np.multiply(output_gradient, derivative)

class Softmax:
    def forward(self, input_data):
        # On fait une "petite triche" pour la stabilité numérique :
        # On soustrait le max pour éviter d'avoir des exponentielles géantes qui font exploser le PC.
        tmp = np.exp(input_data - np.max(input_data, axis=1, keepdims=True))
        self.output = tmp / np.sum(tmp, axis=1, keepdims=True)
        return self.output

    def backward(self, output_gradient):
        return output_gradient

class ReLU:
    def forward(self, input_data):
        self.input = input_data
        return np.maximum(0, input_data)

    def backward(self, output_gradient):
        return output_gradient * (self.input > 0)