import os
import random

# Configuration
OUTPUT_FILE = "mega_dataset.txt"

CATEGORIES = {
    "Check": [
        "dataset/check/10_pieces.txt",
        "dataset/check/20_pieces.txt",
        "dataset/check/many_pieces.txt",
    ],
    "Checkmate": [
        "dataset/checkmate/10_pieces.txt",
        "dataset/checkmate/20_pieces.txt",
        "dataset/checkmate/many_pieces.txt",
    ],
    "Nothing": [
        "dataset/nothing/10_pieces.txt",
        "dataset/nothing/20_pieces.txt",
        "dataset/nothing/many_pieces.txt",
    ]
}

def create_dataset():
    print(f"Création d'un MEGA dataset équilibré (Oversampling)...")
    
    data_by_category = {}
    max_count = 0
    
    # 1. Lecture de toutes les données
    for category, files in CATEGORIES.items():
        lines = []
        for filepath in files:
            if not os.path.exists(filepath):
                print(f"Attention: Fichier {filepath} manquant.")
                continue
            print(f"Lecture de {filepath}...")
            with open(filepath, 'r') as f:
                lines.extend(f.readlines())
        
        data_by_category[category] = lines
        count = len(lines)
        print(f" -> Total {category}: {count} lignes.")
        if count > max_count:
            max_count = count
            
    print(f"Objectif par catégorie : {max_count} lignes.")
    
    final_lines = []
    
    # 2. Oversampling pour atteindre max_count
    for category, lines in data_by_category.items():
        current_count = len(lines)
        if current_count == 0:
            continue
            
        # On prend tout ce qu'on a déjà
        final_lines.extend(lines)
        
        # On complète avec des doublons aléatoires
        needed = max_count - current_count
        if needed > 0:
            print(f"  -> Oversampling {category}: Ajout de {needed} doublons.")
            extras = random.choices(lines, k=needed)
            final_lines.extend(extras)
            
    print(f"Mélange final de {len(final_lines)} lignes...")
    random.shuffle(final_lines)
    
    print(f"Ecriture dans {OUTPUT_FILE}...")
    with open(OUTPUT_FILE, 'w') as f:
        f.writelines(final_lines)
        
    print("Terminé !")

if __name__ == "__main__":
    create_dataset()
