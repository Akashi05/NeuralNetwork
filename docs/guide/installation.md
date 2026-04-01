# Installation

## Prérequis
*   **Python** : Version 3.8 ou supérieure.
*   **Pip** : Gestionnaire de paquets Python.
*   **Git** : Pour cloner le projet.

## Procédure

1.  **Cloner le dépôt**
    ```bash
    git clone https://github.com/votre-repo/my_torch.git
    cd my_torch
    ```

2.  **Créer un environnement virtuel (Recommandé)**
    Cela évite de polluer votre système global.
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Sur Linux/Mac
    # venv\Scripts\activate   # Sur Windows
    ```

3.  **Installer les dépendances**
    La seule dépendance externe autorisée et requise est NumPy.
    ```bash
    pip install numpy
    ```

4.  **Vérification**
    Lancez le générateur d'aide pour vérifier que tout fonctionne.
    ```bash
    ./my_torch_generator --help
    ```