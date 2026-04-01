# Fondements Mathématiques

Ce projet n'utilise aucune boîte noire. Toutes les opérations sont des implémentations directes de l'algèbre linéaire.

## 1. La Couche Dense (Linear)

C'est le cœur du calcul. Pour une entrée $X$ de dimension $(B, N_{in})$, la sortie $Y$ est calculée ainsi :

$$ Y = X \cdot W + B $$

*   $W$ : Matrice des poids de dimension $(N_{in}, N_{out})$.
*   $B$ : Vecteur de biais de dimension $(1, N_{out})$.

## 2. Fonctions d'Activation

Les activations introduisent la non-linéarité nécessaire pour résoudre des problèmes complexes comme les échecs.

### Sigmoid
Utilisée pour les probabilités binaires.
$$ \sigma(x) = \frac{1}{1 + e^{-x}} $$
*Dérivée :* $\sigma'(x) = \sigma(x) \cdot (1 - \sigma(x))$

### ReLU (Rectified Linear Unit)
Utilisée dans les couches cachées pour accélérer la convergence (pas de problème de "vanishing gradient").
$$ f(x) = \max(0, x) $$
*Dérivée :* $1$ si $x > 0$, sinon $0$.

### Softmax
Utilisée en couche de sortie pour la classification multi-classes (Checkmate vs Check vs Nothing).
$$ \sigma(z)_i = \frac{e^{z_i}}{\sum_{j=1}^K e^{z_j}} $$

## 3. Fonction de Coût (Loss)

Pour évaluer la performance, nous utilisons l'erreur quadratique moyenne (MSE) ou la Cross-Entropy.

$$ MSE = \frac{1}{n} \sum_{i=1}^{n} (Y_{pred} - Y_{true})^2 $$
