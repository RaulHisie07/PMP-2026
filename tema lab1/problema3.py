import numpy as np
import matplotlib.pyplot as plt

numar_clienti = 10000
valori_X = []

for i in range(numar_clienti):
    numar_repartizare = np.random.randint(1,14)

    if numar_repartizare <= 3:
        viteza_servire = 3
    elif numar_repartizare <= 9:
        viteza_servire = 6
    else:
        viteza_servire = 4
    timp_servire = np.random.exponential(scale=1 / viteza_servire)
    valori_X.append(timp_servire)

media_X = np.mean(valori_X)
deviatia_X = np.std(valori_X)

print("Media lui X:", media_X)
print("Deviatia standard a lui X:", deviatia_X)
print("Media in minute:", media_X * 60)

plt.hist(
    valori_X,
    bins=50,
    density=True,
    edgecolor="black"
)

plt.xlabel("Timpul de servire (ore)")
plt.ylabel("Densitatea")
plt.title("Densitatea aproximativa a lui X")
plt.show()