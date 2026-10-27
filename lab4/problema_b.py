import itertools
import math

beta = 1 

edges = [(0,1), (0,2), (1,3),
         (1,4), (2,3), (3,4)]

configurations = list(itertools.product([0,1], repeat=5))

weights = []

for a in configurations:
    s = sum(a[i] * a[j] for i,j in edges)
    weights.append(math.exp(beta * s))

Z = sum(weights)

probabilities = [w / Z for w in weights]

max_prob = max(probabilities)

for a, p in zip(configurations, probabilities):
    if abs(p - max_prob) < 1e-12:
        print("Configuratie maxima:", a)
        print("Probabilitate:", p)