# Configuration Avancée du Réseau

Le générateur `my_torch_generator` utilise un fichier JSON strict pour définir la topologie du réseau.

## Structure JSON

Le fichier doit contenir un objet racine avec `input_size` et une liste `layers`.

```json
{
  "input_size": 64,  // Obligatoire: Taille du vecteur d'entrée
  "layers": [
    {
      "type": "linear",
      "output_size": 128
    },
    {
      "type": "relu"
    },
    {
      "type": "dropout",
      "probability": 0.5  // Garde 50% des neurones
    },
    {
      "type": "linear",
      "output_size": 3
    },
    {
      "type": "softmax"
    }
  ]
}
```

## Types de Couches Supportés

| Type | Paramètres Requis | Description |
| :--- | :--- | :--- |
| `linear` | `output_size` (int) | Couche dense entièrement connectée. |
| `dropout` | `probability` (float) | Couche de régularisation. `0.5` est recommandé. |
| `sigmoid` | *Aucun* | Activation Sigmoïde (sortie 0-1). |
| `tanh` | *Aucun* | Activation Tangente Hyperbolique (sortie -1 à 1). |
| `relu` | *Aucun* | Activation Rectifiée (sortie 0 à inf). |
| `softmax` | *Aucun* | Normalisation de probabilité (somme = 1). |

::: warning Cohérence des dimensions
Assurez-vous que la dernière couche `linear` a un `output_size` correspondant à vos classes cibles (ex: 3 pour les échecs : Mat, Échec, Rien).
:::