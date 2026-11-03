# D = dificil, M = mediu, U = usor
stari = ['D', 'M', 'U']
note = ['FB', 'FB', 'S', 'B', 'B', 'S', 'B', 'B', 'NS', 'B', 'B', 'S']
pi = [1/3, 1/3, 1/3]
A = [[0, 0.5, 0.5], [0.5, 0.25, 0.25], [0.5, 0.25, 0.25]]
B = [[0.1, 0.2, 0.4, 0.3], [0.15, 0.25, 0.5, 0.1], [0.2, 0.3, 0.4, 0.1]]
index_note = {'FB': 0, 'B': 1, 'S': 2, 'NS': 3}

print('Sume randuri A:', [sum(rand) for rand in A])
print('Sume randuri B:', [sum(rand) for rand in B])

scoruri = []
precedente = []
primul = index_note[note[0]]
scoruri.append([pi[j] * B[j][primul] for j in range(3)])
precedente.append([-1, -1, -1])

for t in range(1, len(note)):
    scor_nou = []
    predecesori_noi = []
    for j in range(3):
        valori = [scoruri[t-1][i] * A[i][j] for i in range(3)]
        cel_mai_bun = valori.index(max(valori))
        scor_nou.append(max(valori) * B[j][index_note[note[t]]])
        predecesori_noi.append(cel_mai_bun)
    scoruri.append(scor_nou)
    precedente.append(predecesori_noi)

print('delta 1:', scoruri[0])
print('delta 2:', scoruri[1])
ultima = scoruri[-1].index(max(scoruri[-1]))
probabilitate = scoruri[-1][ultima]
traseu = [ultima]
for t in range(len(note)-1, 0, -1):
    ultima = precedente[t][ultima]
    traseu.insert(0, ultima)

print('Traseu:', [stari[i] for i in traseu])
print('Probabilitate comuna:', probabilitate)
print('Interpretare: Viterbi alege traseul complet cu probabilitatea comuna maxima, nu fiecare stare separat.')
