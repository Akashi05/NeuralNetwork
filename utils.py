import numpy as np

def parse_an_fen(fen_as_strings):
    """
    Transforme une chaine FEN en vecteur numpy.
    """
    parts = fen_as_strings.split(' ')
    echiquier_part = parts[0]

    # Pions=1, Cheval/Fou=3, Tour=5, Reine=9, Roi=10
    # Blancs = Positif, Noirs = Négatif
    piece_values = {
        'P': 1, 'N': 3, 'B': 3, 'R': 5, 'Q': 9, 'K': 10,  # Blancs
        'p': -1, 'n': -3, 'b': -3, 'r': -5, 'q': -9, 'k': -10, # Noirs
    }
    echiquier_vector = []
    for every_char in echiquier_part:
        if every_char == "/":
            continue
        elif every_char.isdigit():
            nb_empty_squares = int(every_char)
            for _ in range(nb_empty_squares):
                echiquier_vector.append(0)
        else:
            echiquier_vector.append(piece_values[every_char])
    
    # Ajout du trait (qui doit jouer) : 1 pour Blancs, -1 pour Noirs
    if len(parts) > 1 and parts[1] == 'b':
        echiquier_vector.append(-1)
    else:
        echiquier_vector.append(1)

    if len(echiquier_vector) != 65:
        print(f"Attention: FEN invalide (taille {len(echiquier_vector)}) -> {fen_as_strings}")
        return np.zeros((1, 65))
    
    # Normalisation : On divise par 10 pour avoir des valeurs entre -1 et 1
    return np.array(echiquier_vector).reshape((1, 65)) / 10.0

def encode_result(result_string):
    """
    Encode le résultat d'une partie d'échecs en valeur numérique.
    Sortie attendue : Vecteur de taille 3
    [1, 0, 0] = Checkmate
    [0, 1, 0] = Check
    [0, 0, 1] = Nothing
    """
    if "Checkmate" in result_string:
        return np.array([[1, 0, 0]])
    elif "Check" in result_string:
        return np.array([[0, 1, 0]])
    else:
        return np.array([[0, 0, 1]])


def load_data(file_path):
    """
    Charge les données d'entraînement depuis un fichier .txt
    """
    inputs = []
    outputs = []

    # print(f"Chargement des données depuis {file_path}...")
    
    try:
        with open(file_path, 'r') as f:
            lines = f.readlines()
        for line in lines:
            line = line.strip()
            if not line:
                continue
            input_vector = parse_an_fen(line)
            # On essaie de lire le résultat, mais ce n'est pas grave s'il n'y est pas (mode prédiction)
            output_vector = encode_result(line)
            inputs.append(input_vector)
            outputs.append(output_vector)
        # print(f"Données chargées: {len(inputs)} plateaux.")
        return inputs, outputs
    except FileNotFoundError:
        print(f"Erreur: Fichier {file_path} non trouvé.")
        return [], []
                