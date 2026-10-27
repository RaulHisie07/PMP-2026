import numpy as np
import matplotlib.pyplot as plt
import networkx as nx
from hmmlearn.hmm import CategoricalHMM


stari = ["Dificil", "Mediu", "Usor"]

model = CategoricalHMM(n_components=3, init_params="")


model.startprob_ = np.array([1 / 3, 1 / 3, 1 / 3])


model.transmat_ = np.array([
    [0,   0.5,  0.5],
    [0.5, 0.25, 0.25],
    [0.5, 0.25, 0.25]
])


model.emissionprob_ = np.array([
    [0.10, 0.20, 0.40, 0.30],
    [0.15, 0.25, 0.50, 0.10],
    [0.20, 0.30, 0.40, 0.10]
])

# a
graf = nx.DiGraph()
graf.add_nodes_from(stari)
etichete = {}

for i in range(3):
    for j in range(3):
        if model.transmat_[i, j] > 0:
            graf.add_edge(stari[i], stari[j])
            etichete[(stari[i], stari[j])] = model.transmat_[i, j]

pozitii = {"Dificil": (0, 1), "Mediu": (-1, 0), "Usor": (1, 0)}

plt.figure(figsize=(8, 6))
nx.draw(
    graf, pozitii, with_labels=True,
    node_size=2400, node_color="lightblue",
    arrowsize=20, connectionstyle="arc3,rad=0.2"
)
nx.draw_networkx_edge_labels(
    graf, pozitii, edge_labels=etichete,
    connectionstyle="arc3,rad=0.2"
)
plt.title("Tranzitiile dintre dificultati")
plt.show()

# b)

observatii = np.array([
    [0], [0], [2], [1], [1], [2],
    [1], [1], [3], [1], [1], [2]
])


log_prob, secventa = model.decode(observatii, algorithm="viterbi")

print("Dificultatile estimate:")
for dificultate in secventa:
    print(stari[dificultate], end=" ")
print()


probabilitate_comuna = np.exp(log_prob)


probabilitate_conditionata = np.exp(
    log_prob - model.score(observatii)
)

print("Probabilitatea comuna:", probabilitate_comuna)
print("Probabilitatea conditionata:", probabilitate_conditionata)