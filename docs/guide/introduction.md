# Présentation du Projet (Non-Tech)

**My_Torch** n'est pas un simple jeu d'échecs. C'est une plongée au cœur de la mécanique de l'Intelligence Artificielle.

## 🎯 L'Objectif
L'intelligence artificielle (IA) est souvent vue comme une "boîte noire" magique. Notre mission était de casser cette boîte et de reconstruire le moteur nous-mêmes.
Concrètement, nous avons créé un programme capable de **regarder un échiquier** et de dire instantanément si le Roi est en danger (Échec), si la partie est finie (Mat) ou si tout va bien.

## 💡 L'Analogie : L'Enfant et l'Échiquier
Pour comprendre comment fonctionne notre programme, imaginez un enfant qui n'a jamais joué aux échecs.

1.  **Le Cerveau Vide (Initialisation)** :
    Au départ, l'enfant (notre programme) ne connaît rien. Il a des neurones, mais ils ne sont pas connectés. Si on lui montre un échiquier, il répond au hasard.

2.  **L'École (L'Entraînement)** :
    Nous montrons à l'enfant des milliers de photos de parties d'échecs. Pour chaque photo, nous lui disons : *"Regarde, ici c'est Échec et Mat"* ou *"Ici, il ne se passe rien"*.

3.  **L'Apprentissage (La Rétropropagation)** :
    Au début, l'enfant se trompe souvent. Mais à chaque erreur, nous le corrigeons. Son cerveau s'ajuste petit à petit : *"Ah, quand la Tour est en face du Roi, c'est dangereux !"*. C'est ce qu'on appelle l'ajustement des **Poids**.

4.  **L'Examen (La Prédiction)** :
    Une fois l'entraînement fini, nous montrons à l'enfant une situation qu'il n'a jamais vue. Grâce à son expérience, il peut nous donner la bonne réponse.

## 🚀 Pourquoi "From Scratch" ?
Dans l'industrie, les développeurs utilisent des outils tout faits (comme TensorFlow ou PyTorch). C'est comme acheter une voiture chez le concessionnaire.
**My_Torch**, c'est fabriquer la voiture soi-même, en usinant chaque pièce du moteur. Cela nous permet de comprendre mathématiquement pourquoi l'IA fonctionne (ou ne fonctionne pas).