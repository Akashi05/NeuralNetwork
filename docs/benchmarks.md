# Benchmarks & Performance

Cette section présente les résultats expérimentaux obtenus avec **My_Torch**. Les tests ont été réalisés pour valider la convergence du réseau, l'efficacité des optimisations et la précision sur la détection des états d'échecs.
Chaque graphique est généré par un script de test indépendant (`generate_tri_bench.py`) qui isole une fonctionnalité critique du projet.

---

## 1. Validation de la Logique (Non-Linéarité)

Ce test valide la capacité fondamentale du réseau à résoudre des problèmes non-linéaires. Un réseau sans couche cachée ou sans fonction d'activation échouerait ici (erreur bloquée à 0.5).

### 🧪 Protocole
*   **Données** : Table de vérité XOR (4 exemples : `0,0->0`, `0,1->1`...).
*   **Architecture** : `[2 entrées] -> [10 Tanh] -> [1 Tanh]`.
*   **Optimiseur** : SGD (Learning Rate = `0.1`).

![Benchmark XOR](/bench_1_xor.png)

### 📊 Analyse de la courbe
*   **La Chute Verticale (Époque 0-10)** : On observe une chute brutale de l'erreur. C'est le moment où le réseau trouve l'hyperplan qui sépare les 0 des 1.
*   **Le Plateau (Époque 20+)** : L'erreur devient quasi-nulle ($< 10^{-3}$). Cela prouve que la **Rétropropagation** fonctionne parfaitement à travers les couches cachées et les fonctions `Tanh`.

---

## 2. Validation de la Charge (Input 64)

Le projet final nécessite de traiter un échiquier de 64 cases. Ce test vérifie que le moteur supporte une haute dimensionnalité sans instabilité numérique (explosion de gradient).

### 🧪 Protocole
*   **Données** : 50 vecteurs aléatoires de taille **64** (simulant un échiquier bruité).
*   **Tâche** : Le réseau doit apprendre à prédire la sortie en se basant uniquement sur la 1ère case, en ignorant les 63 autres (bruit).
*   **Architecture** : `[64 entrées] -> [32 Tanh] -> [1 Linear]`.
*   **Optimiseur** : SGD (Learning Rate = `0.01`). Notez le LR plus faible pour éviter les divergences dues au grand nombre de poids.

![Benchmark 64 Inputs](/bench_2_dim.png)

### 📊 Analyse de la courbe
*   **La Forme Exponentielle** : Contrairement au XOR, la courbe est douce. Le réseau doit "éteindre" l'influence des 63 entrées inutiles (poids tendant vers 0) et renforcer la 1ère.
*   **Stabilité** : Malgré les 2000+ paramètres à ajuster, la courbe ne présente pas de pics (spikes). Cela valide notre implémentation du **Produit Matriciel** (`np.dot`) et la gestion des dimensions.

---

## 3. Validation de la Classification (3 Sorties)

Le défi final est de distinguer 3 états exclusifs : *Check*, *Checkmate*, *Nothing*. Ce test valide l'utilisation de `Softmax` pour générer des probabilités.

### 🧪 Protocole
*   **Données** : 30 vecteurs classés en 3 catégories (A, B, C) selon une règle mathématique (somme des éléments).
*   **Sortie Attendue** : Encodage One-Hot (ex: Classe A = `[1, 0, 0]`).
*   **Architecture** : `[10 entrées] -> [10 Tanh] -> [3 Softmax]`.
*   **Loss** : MSE sur les vecteurs de probabilités.

![Benchmark Multi-Class](/bench_3_multi.png)

### 📊 Analyse de la courbe
*   **Convergence plus lente** : La courbe met environ 100 époques à atteindre un niveau bas. C'est normal : le `Softmax` crée une compétition entre les neurones de sortie (si l'un monte, les autres doivent descendre).
*   **Asymptote** : L'erreur tend vers 0 sans jamais l'atteindre totalement, car `Softmax` ne sort jamais exactement 0 ou 1 (mais plutôt 0.0001 et 0.9999). Le comportement est conforme à la théorie.
