from utils import load_data

# On essaie de charger un de tes fichiers (assure-toi que le fichier existe)
inputs, outputs = load_data("dataset/check/10_pieces.txt")

if len(inputs) > 0:
    print("\n--- TEST DU PREMIER PLATEAU ---")
    print("Vecteur d'entrée (taille) :", inputs[0].shape)
    print("Aperçu des 10 premières cases :", inputs[0].flatten()[:10])
    print("Vecteur de sortie (Target) :", outputs[0].flatten())
    print("C'est bien un vecteur colonne ? ", inputs[0].shape == (64, 1))