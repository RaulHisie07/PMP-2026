import numpy as np
from hmmlearn.hmm import CategoricalHMM
model = CategoricalHMM(n_components=4, init_params="")

model.startprob_ = np.array([0.25, 0.25, 0.25, 0.25])

model.transmat_ = np.array([
    [0,   0.5, 0,   0.5],
    [0.5, 0,   0.5, 0],
    [0,   0.5, 0,   0.5],
    [0.5, 0,   0.5, 0]
])
model.emissionprob_ = np.array([
    [0.7, 0.2, 0.1],
    [0.2, 0.6, 0.2],
    [0.1, 0.3, 0.6],
    [0.5, 0.2, 0.3]
])
obs = np.array([[0], [1], [2], [2], [0]])

log_prob, camere = model.decode(obs, algorithm="viterbi")

print("Camere:", camere + 1)
print("Probabilitatea comuna:", round(np.exp(log_prob), 12))