import pymc as pm
import arviz as az
import numpy as np
import matplotlib.pyplot as plt

y = np.array([3, 4, 2, 5, 3, 4, 3, 2, 4, 3, 4, 5, 5, 6, 5, 7, 6, 8, 7, 9,
              8, 10, 9, 8, 11, 9, 10, 8, 9, 10])
t = np.arange(1, 31)

# a) model PyMC
with pm.Model() as model:
    lam1 = pm.Exponential("lam1", 0.2)
    lam2 = pm.Exponential("lam2", 0.2)
    tau = pm.Uniform("tau", 1, 30)
    k = pm.Exponential("k", 1)
    lam_t = lam1 + (lam2 - lam1) * pm.math.sigmoid(k * (t - tau))
    obs = pm.Poisson("obs", mu=lam_t, observed=y)
    trace = pm.sample(5000, tune=2000, chains=4, target_accept=0.95, random_seed=1)

l1 = trace.posterior["lam1"].values.flatten()
l2 = trace.posterior["lam2"].values.flatten()
tau_s = trace.posterior["tau"].values.flatten()
k_s = trace.posterior["k"].values.flatten()

# b) tau si k
plt.hist(tau_s, bins=60, density=True)
plt.title("Posterior tau")
plt.savefig("ex3_tau.png")
plt.close()

plt.hist(k_s, bins=60, density=True)
plt.title("Posterior k")
plt.savefig("ex3_k.png")
plt.close()

print("HDI 95% tau:", az.hdi(tau_s, hdi_prob=0.95))
print("HDI 95% k:", az.hdi(k_s, hdi_prob=0.95))

# c) P(lam2 > lam1) si evolutia lambda_t
print("P(lam2 > lam1) =", (l2 > l1).mean())

# lambda_t pentru fiecare esantion: matrice (esantioane, 30 zile)
lam_all = l1[:, None] + (l2[:, None] - l1[:, None]) / (1 + np.exp(-k_s[:, None] * (t[None, :] - tau_s[:, None])))
lam_mean = lam_all.mean(axis=0)

plt.plot(t, y, "o", label="date")
plt.plot(t, lam_mean, label="lambda_t estimat")
plt.legend()
plt.xlabel("ziua")
plt.savefig("ex3_lambda_t.png")
plt.close()

# d) predictiv
y_pred = np.random.poisson(lam_all)
pred_mean = y_pred.mean(axis=0)
pred_low = np.percentile(y_pred, 2.5, axis=0)
pred_high = np.percentile(y_pred, 97.5, axis=0)

plt.plot(t, y, "o", label="date")
plt.plot(t, pred_mean, label="media predictiva")
plt.fill_between(t, pred_low, pred_high, alpha=0.3, label="interval 95%")
plt.legend()
plt.xlabel("ziua")
plt.savefig("ex3_predictiv.png")
plt.close()

print("zile cu y in intervalul 95%:", ((y >= pred_low) & (y <= pred_high)).sum(), "din 30")
