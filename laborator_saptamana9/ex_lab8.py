import pymc as pm
import arviz as az
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 3, figsize=(15, 8))

for r, theta in enumerate([0.2, 0.5]):
    for c, Y in enumerate([0, 5, 10]):
        with pm.Model() as model:
            n = pm.Poisson("n", mu=10)
            y = pm.Binomial("y", n=n, p=theta, observed=Y)
            trace = pm.sample(5000, chains=4, random_seed=1)
        n_s = trace.posterior["n"].values.flatten()
        az.plot_posterior(n_s, ax=axs[r, c])
        axs[r, c].set_title("Y=" + str(Y) + ", theta=" + str(theta))

plt.tight_layout()
plt.savefig("ex_lab8_posterior.png")
plt.show()
