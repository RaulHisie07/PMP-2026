import random

N = 100000
numar_bile_rosii = 0

for i in range(N):
    urna = ['R'] * 3 + ['A'] * 4 + ['N'] * 2

    zar = random.randint(1,6)

    if zar in [2,3,5]:
     urna.append('N')
    elif zar == 6:
        urna.append('R')
    else:
        urna.append('A')

    bila_extrasa = random.choice(urna)

    if bila_extrasa == 'R':
        numar_bile_rosii += 1
    
probabilitate_simulata = numar_bile_rosii / N 

probabilitate_teoretica = (
    (3 / 6) * (3 / 10) +
    (1 / 6) * (4 / 10) +
    (2 / 6) * (3 / 10)
)
print("Probabilitatea simulata:", probabilitate_simulata)

print("Probabilitatea teoretica:", probabilitate_teoretica)

print("Diferenta:", abs(probabilitate_simulata - probabilitate_teoretica))