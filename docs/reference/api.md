# API Python Reference

Si vous souhaitez utiliser `my_torch` comme une librairie dans vos propres scripts Python.

## `Network`
La classe principale gérant le graphe de calcul.

```python
from my_torch.network import Network

net = Network()
net.add(Linear(64, 32))
net.save("model.nn")
```

### Méthodes
*   `add(layer)` : Ajoute une couche à la fin de la pile.
*   `forward(input, training=False)` : Pousse les données à travers le réseau.
*   `train(x, y, epochs, lr)` : Lance la boucle d'apprentissage SGD.
*   `save(path)` / `load(path)` : Sérialisation Pickle.

## `Linear`
Couche dense connectée.
```python
Linear(input_size: int, output_size: int)
```
Utilise l'initialisation de He par défaut.