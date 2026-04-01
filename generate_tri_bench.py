#!/usr/bin/env python3
import matplotlib.pyplot as plt
import numpy as np
import os

from my_torch.network import Network
from my_torch.layers import Linear
from my_torch.activations import Tanh, Sigmoid, Softmax
from my_torch.loss import MSE
from my_torch.optimizer import SGD

def save_plot(history, title, filename, color):
    plt.figure(figsize=(10, 6))
    plt.plot(history, color=color, linewidth=2.5)
    plt.title(title, fontsize=14, fontweight='bold')
    plt.xlabel('Époques (Itérations)')
    plt.ylabel('Erreur (Loss)')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.fill_between(range(len(history)), history, color=color, alpha=0.1)
    
    path = f'docs/public/{filename}'
    plt.savefig(path)
    plt.close()
    print(f"✅ Graphique généré : {path}")

# --- TEST 1 : LOGIQUE (XOR) ---
def bench_xor():
    print("🔹 1/3 : Benchmark Logique (XOR)...")
    X = np.array([[0,0], [0,1], [1,0], [1,1]])
    Y = np.array([[0], [1], [1], [0]])

    net = Network()
    net.add(Linear(2, 10))
    net.add(Tanh())
    net.add(Linear(10, 1))
    net.add(Tanh())
    net.use_loss(MSE())
    net.use_optimizer(SGD(learning_rate=0.1))

    hist = net.train(X, Y, epochs=300, learning_rate=0.1)
    save_plot(hist, 'Test 1 : Logique Non-Linéaire (XOR)', 'bench_1_xor.png', '#646cff') # Bleu

# --- TEST 2 : HAUTE DIMENSION (Simu Échecs) ---
def bench_high_dim():
    print("🔹 2/3 : Benchmark Haute Dimension (64 Entrées)...")
    # Simulation : 64 entrées aléatoires
    X = np.random.rand(50, 64) 
    # Cible : Juste apprendre à reproduire la première case (tâche simple mais bruyante)
    Y = X[:, 0].reshape(-1, 1)

    net = Network()
    net.add(Linear(64, 32))
    net.add(Tanh())
    net.add(Linear(32, 1))
    net.use_loss(MSE())
    net.use_optimizer(SGD(learning_rate=0.01))

    hist = net.train(X, Y, epochs=200, learning_rate=0.01)
    save_plot(hist, 'Test 2 : Stabilité sur vecteur 64 (Échiquier)', 'bench_2_dim.png', '#3eaf7c') # Vert

# --- TEST 3 : MULTI-CLASSES (3 Sorties) ---
def bench_multiclass():
    print("🔹 3/3 : Benchmark Multi-Sorties (Check/Mate/Nothing)...")
    # Simulation de 3 classes (One-Hot Encoding)
    # 0 -> [1,0,0], 1 -> [0,1,0], 2 -> [0,0,1]
    X = np.random.rand(30, 10) # 10 entrées
    Y = np.zeros((30, 3))      # 3 sorties !
    
    # Règle arbitraire pour créer des classes
    for i in range(30):
        val = np.sum(X[i])
        if val < 3: Y[i] = [1, 0, 0]   # Classe A
        elif val < 5: Y[i] = [0, 1, 0] # Classe B
        else: Y[i] = [0, 0, 1]         # Classe C

    net = Network()
    net.add(Linear(10, 10))
    net.add(Tanh())
    net.add(Linear(10, 3))    # 3 Neurones de sortie
    net.add(Softmax())        # Activation pour probabilités
    net.use_loss(MSE())
    net.use_optimizer(SGD(learning_rate=0.05))

    hist = net.train(X, Y, epochs=400, learning_rate=0.05)
    save_plot(hist, 'Test 3 : Classification Multi-Classes (3 Sorties)', 'bench_3_multi.png', '#ff5252') # Rouge

if __name__ == "__main__":
    os.makedirs('docs/public', exist_ok=True)
    bench_xor()
    bench_high_dim()
    bench_multiclass()
    