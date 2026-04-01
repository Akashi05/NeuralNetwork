# Traitement des Données (Échecs)

Les réseaux de neurones ne comprennent que les nombres. Comment transformer un plateau d'échecs en nombres ?

## Le Format FEN
L'entrée brute est au format **Forsyth-Edwards Notation (FEN)**.
Exemple : `rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`

## Encodage (Preprocessing)

Nous transformons cette chaîne en un vecteur de taille fixe (généralement 64 ou plus). Une méthode simple consiste à associer une valeur à chaque pièce :

| Pièce | Valeur |
| :--- | :--- |
| Pion Blanc | 1 |
| Cavalier Blanc | 3 |
| Roi Noir | -6 |
| Case Vide | 0 |
| ... | ... |

Le réseau reçoit donc une liste de 64 nombres flottants normalisés.

## Output (One-Hot Encoding)
La sortie attendue n'est pas un texte, mais un vecteur de probabilités de taille 3 :

*   **Checkmate** : `[1, 0, 0]`
*   **Check** : `[0, 1, 0]`
*   **Nothing** : `[0, 0, 1]`

C'est ce format que la fonction `Softmax` tente de reproduire en sortie.
