class SGD:
    """
    Stochastic Gradient Descent (Descente de Gradient Stochastique).
    C'est l'algo qui met à jour les poids pour descendre la montagne d'erreur.
    """
    def __init__(self, learning_rate=0.1):
        self.lr = learning_rate

    """
    Applique la correction : W = W - (lr * gradient)
    """
    def update(self, layer):
        # On vérifie si la couche a des poids (ex: Layer a des poids, mais Tanh non)
        if hasattr(layer, 'weights'):
            layer.weights -= self.lr * layer.grad_weights
            layer.bias -= self.lr * layer.grad_bias