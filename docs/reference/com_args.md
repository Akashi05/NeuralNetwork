# Command Line Interface (CLI)

Documentation des exécutables fournis avec My_Torch.

## `my_torch_generator`
Outil de création de réseaux neuronaux vierges.

**Usage :**
`./my_torch_generator [CONFIG_FILE] [NB_NETWORKS]`

| Argument | Description |
| :--- | :--- |
| `CONFIG_FILE` | Chemin vers le fichier JSON décrivant l'architecture. |
| `NB_NETWORKS` | Nombre de fichiers `.nn` à générer (ex: 10 pour tester 10 init différentes). |

---

## `my_torch_analyzer`
Le programme principal pour l'entraînement et la prédiction.

**Usage :**
`./my_torch_analyzer [OPTIONS] LOADFILE DATAFILE`

| Argument | Description |
| :--- | :--- |
| `LOADFILE` | Chemin vers un fichier réseau (`.nn`) existant. |
| `DATAFILE` | Fichier contenant les données (FEN + Labels pour train, FEN pour predict). |

**Options :**

| Option | Description |
| :--- | :--- |
| `--train` | Active le mode entraînement (Backpropagation activée). |
| `--predict` | Active le mode inférence (Pas de modification des poids). |
| `--save FILE` | (Mode Train uniquement) Sauvegarde le réseau entraîné dans `FILE`. |
