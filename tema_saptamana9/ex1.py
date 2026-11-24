import pymc as pm
import arviz as az
import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

M = 20
n = 15
y = 4

# a) model PyMC
with pm.Model() as model:
    N = pm.DiscreteUniform("N", lower=20, upper=200)
    obs = pm.HyperGeometric("obs", N=N, k=M, n=n, observed=y)
    trace = pm.sample(5000, chains=4, random_seed=1)

N_s = trace.posterior["N"].values.flatten()

plt.hist(N_s, bins=60, density=True)
plt.title("Posterior N")
plt.xlabel("N")
plt.savefig("ex1_posterior_N.png")
plt.close()

# b) media, mediana, HDI
print("media", N_s.mean())
print("mediana", np.median(N_s))
print("HDI 95%", az.hdi(N_s, hdi_prob=0.95))
print("estimare clasica M*n/Y =", M * n / y)

# c) P(N>100)
print("P(N>100) =", (N_s > 100).mean())

# d) predictiv: nr marcate la o noua capturare de 15
y_new = stats.hypergeom.rvs(N_s, M, n)   # scipy: (total, marcate, extrase)
vals, counts = np.unique(y_new, return_counts=True)
print("predictiv:", dict(zip(vals, counts / len(y_new))))

plt.bar(vals, counts / len(y_new))
plt.title("Predictiv a posteriori: nr marcate din 15")
plt.xlabel("y nou")
plt.savefig("ex1_predictiv.png")
plt.close()

# verificare exacta (fara MCMC)
Ns = np.arange(20, 201)
lik = stats.hypergeom.pmf(y, Ns, M, n)
post = lik / lik.sum()
print("exact: media", (Ns * post).sum())
print("exact: P(N>100)", post[Ns > 100].sum())
