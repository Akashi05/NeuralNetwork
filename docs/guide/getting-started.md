# Premiers Pas

Ce guide vous accompagne pour réaliser votre première prédiction en moins de 2 minutes.

## 1. Générer le Cerveau 🧠
Nous allons créer un réseau neuronal simple défini dans `config.json`.

```bash
# Crée 1 réseau nommé 'basic_network_1.nn'
./my_torch_generator config.json 1
```

## 2. Entraîner le Modèle 🏋️
Nous allons apprendre au réseau à reconnaître le XOR (exemple simple) ou des échecs.
Supposons un fichier `dataset.txt` contenant vos données.

```bash
# Entraîne le réseau et sauvegarde le résultat dans 'trained.nn'
./my_torch_analyzer --train --save trained.nn basic_network_1.nn dataset.txt
```

*Vous verrez l'erreur (Loss) diminuer progressivement dans le terminal.*

## 3. Faire une Prédiction 🔮
Utilisez votre nouveau cerveau intelligent sur de nouvelles données.

```bash
./my_torch_analyzer --predict trained.nn chessboards_test.txt
```

Le programme affichera :
```text
Checkmate
Nothing
Check
...
```
