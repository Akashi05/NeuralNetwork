import numpy as np

class MSE:
    """
    Calcule l'erreur moyenne au carré.
    Plus ce chiffre est proche de 0, meilleur est le réseau.
    """
    def loss(self, y_true, y_pred):
        return np.mean(np.power(y_true - y_pred, 2))

    """
    Calcule la dérivée de l'erreur.
    C'est le point de départ de la Backpropagation.
    Cela indique : "Tu étais trop haut ou trop bas ?"
    """
    def derivative(self, y_true, y_pred):
        return 2 * (y_pred - y_true) / y_true.size

class CategoricalCrossEntropy:
    def loss(self, y_true, y_pred):
        # On ajoute une minuscule valeur (1e-9) pour éviter de faire log(0) qui planterait le programme
        epsilon = 1e-9
        y_pred_clipped = np.clip(y_pred, epsilon, 1 - epsilon)
        # Formule : - Somme(y_true * log(y_pred))
        return -np.mean(np.sum(y_true * np.log(y_pred_clipped), axis=1))

    def derivative(self, y_true, y_pred):
        # La dérivée combinée de (Softmax + CrossEntropy) est simplement : (Prédiction - Cible)
        # C'est aussi simple que la MSE !
        return (y_pred - y_true) / y_true.shape[0]