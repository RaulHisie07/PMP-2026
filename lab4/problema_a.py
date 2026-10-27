import pyagrum as gum
import matplotlib.pyplot as plt
import networkx as nx

G = nx.Graph()

G.add_edges_from(
    [
    ("A1", "A2"),

    ("A1", "A3"),

    ("A2", "A4"),

    ("A2", "A5"),

    ("A3", "A4"),

    ("A4", "A5")
    ]
)

nx.draw(G, with_labels=True, node_color="lightblue")
plt.show()

print("Clicile maximale : ", list(nx.find_cliques(G)))