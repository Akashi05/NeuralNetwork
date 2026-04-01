# NeuralNetwork — my_torch

Un framework de réseau de neurones fait maison en Python, inspiré de PyTorch, avec une application de classification de positions d'échecs.

## Table des matières

- [Présentation](#présentation)
- [Structure du projet](#structure-du-projet)
- [Installation](#installation)
- [La bibliothèque `my_torch`](#la-bibliothèque-my_torch)
- [Outils en ligne de commande](#outils-en-ligne-de-commande)
  - [my\_torch\_generator](#my_torch_generator)
  - [my\_torch\_analyzer](#my_torch_analyzer)
- [Format de configuration JSON](#format-de-configuration-json)
- [Tests](#tests)

---

## Présentation

Ce projet implémente un réseau de neurones entièrement from scratch avec NumPy. Il est composé de :

- **`my_torch`** : la bibliothèque principale (couches, activations, fonctions de perte, optimiseur)
- **`my_torch_generator`** : génère et sauvegarde des réseaux à partir d'un fichier de configuration JSON
- **`my_torch_analyzer`** : entraîne ou utilise un réseau pour classifier des positions d'échecs (Échec et mat / Échec / Rien)

---

## Structure du projet

```
.
├── my_torch/               # Bibliothèque principale
│   ├── network.py          # Classe Network (forward, backward, train, save, load)
│   ├── layers.py           # Couches Linear et Dropout
│   ├── activations.py      # Fonctions d'activation : Tanh, Sigmoid, Softmax, ReLU
│   ├── loss.py             # Fonctions de perte : MSE, CategoricalCrossEntropy
│   └── optimizer.py        # Optimiseur SGD
├── my_torch_analyzer       # CLI : entraînement / prédiction sur positions d'échecs
├── my_torch_generator      # CLI : génération de réseaux depuis un fichier JSON
├── utils.py                # Parsing FEN et encodage des résultats
├── network_config.json     # Exemple de configuration réseau (échecs)
├── config.json             # Exemple de configuration simple (XOR)
├── test_xor.py             # Test du réseau sur le problème XOR
├── test_multi.py           # Test multiclasse
├── test_parsing.py         # Test du parsing FEN
└── docs/                   # Documentation VitePress
```

---

## Installation

**Prérequis :** Python 3.8+ et NumPy.

```bash
pip install numpy
```

Pour la documentation (optionnel) :

```bash
npm install
npm run docs:dev
```

---

## La bibliothèque `my_torch`

### Construire un réseau

```python
from my_torch.network import Network
from my_torch.layers import Linear
from my_torch.activations import ReLU, Softmax
from my_torch.loss import CategoricalCrossEntropy

net = Network()
net.add(Linear(65, 128))
net.add(ReLU())
net.add(Linear(128, 3))
net.add(Softmax())

net.use_loss(CategoricalCrossEntropy())
```

### Entraîner

```python
net.train(x_train, y_train, epochs=30, learning_rate=0.005)
```

### Prédire

```python
output = net.predict(input_vector)
```

### Sauvegarder / Charger

```python
net.save("mon_reseau.nn")
net = Network.load("mon_reseau.nn")
```

### Couches disponibles

| Classe     | Description                              |
|------------|------------------------------------------|
| `Linear`   | Couche entièrement connectée (He init)   |
| `Dropout`  | Régularisation par désactivation aléatoire |

### Activations disponibles

| Classe    | Plage de sortie |
|-----------|-----------------|
| `Tanh`    | [-1, 1]         |
| `Sigmoid` | [0, 1]          |
| `ReLU`    | [0, +∞)         |
| `Softmax` | [0, 1] (somme = 1) |

### Fonctions de perte

| Classe                    | Usage typique              |
|---------------------------|----------------------------|
| `MSE`                     | Régression                 |
| `CategoricalCrossEntropy` | Classification multiclasse |

---

## Outils en ligne de commande

### my_torch_generator

Génère un ou plusieurs réseaux initialisés à partir d'un fichier de configuration JSON et les sauvegarde au format `.nn`.

```bash
./my_torch_generator <config.json> <nb_reseaux>
```

**Exemple :**

```bash
./my_torch_generator network_config.json 3
# Crée : network_config_1.nn, network_config_2.nn, network_config_3.nn
```

---

### my_torch_analyzer

Entraîne un réseau ou effectue des prédictions sur des plateaux d'échecs au format FEN.

```bash
./my_torch_analyzer <reseau.nn> <dataset.txt> --train [--save sortie.nn]
./my_torch_analyzer <reseau.nn> <dataset.txt> --predict
```

**Entraînement :**

```bash
./my_torch_analyzer mon_reseau.nn train_data.txt --train --save mon_reseau_v2.nn
```

**Prédiction :**

```bash
./my_torch_analyzer mon_reseau.nn test_data.txt --predict
```

Chaque ligne du fichier de données est une position FEN. La sortie en mode `--predict` est l'une des trois classes :

- `Checkmate` — Échec et mat
- `Check` — Échec
- `Nothing` — Rien de particulier

---

## Format de configuration JSON

```json
{
    "input_size": 65,
    "layers": [
        { "type": "linear", "output_size": 128 },
        { "type": "relu" },
        { "type": "dropout", "probability": 0.9 },
        { "type": "linear", "output_size": 64 },
        { "type": "relu" },
        { "type": "linear", "output_size": 3 },
        { "type": "softmax" }
    ]
}
```

**Types de couches supportés :** `linear`, `dropout`, `tanh`, `sigmoid`, `relu`, `softmax`

---

## Tests

```bash
# Test du problème XOR
python test_xor.py

# Test multiclasse
python test_multi.py

# Test du parsing FEN
python test_parsing.py
```
