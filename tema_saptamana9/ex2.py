import pymc as pm
import arviz as az
import numpy as np
import matplotlib.pyplot as plt

A = np.array([3.2, 4.1, 2.8, 5.0, 3.7, 4.5, 3.0, 3.9])
B = np.array([2.1, 2.8, 3.4, 2.5, 3.0, 2.2, 3.6, 2.7])

# a) model PyMC
with pm.Model() as model:
    lamA = pm.Gamma("lamA", alpha=2, beta=4)
    lamB = pm.Gamma("lamB", alpha=2, beta=4)
    xA = pm.Exponential("xA", lam=lamA, observed=A)
    xB = pm.Exponential("xB", lam=lamB, observed=B)
    trace = pm.sample(5000, chains=4, random_seed=1)

lamA_s = trace.posterior["lamA"].values.flatten()
lamB_s = trace.posterior["lamB"].values.flatten()

# b) timpi medii
medA = 1 / lamA_s
medB = 1 / lamB_s

plt.hist(medA, bins=60, density=True, alpha=0.5, label="1/lamA")
plt.hist(medB, bins=60, density=True, alpha=0.5, label="1/lamB")
plt.legend()
plt.title("Posterior timpi medii")
plt.savefig("ex2_timpi_medii.png")
plt.close()

print("HDI 95% 1/lamA:", az.hdi(medA, hdi_prob=0.95))
print("HDI 95% 1/lamB:", az.hdi(medB, hdi_prob=0.95))

# c) P(B mai rapid in medie)
print("P(1/lamB < 1/lamA) =", (medB < medA).mean())

# d) predictiv: pacient nou
xA_new = np.random.exponential(1 / lamA_s)
xB_new = np.random.exponential(1 / lamB_s)
print("P(xB_nou < xA_nou) =", (xB_new < xA_new).mean())
