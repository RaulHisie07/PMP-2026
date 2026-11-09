import numpy as np
import arviz as az
import matplotlib.pyplot as plt

alpha = 181
beta = 11

np.random.seed(42)
valori = np.random.gamma(alpha, 1 / beta, 100000)

az.plot_posterior(valori, hdi_prob=0.94, point_estimate="mode")

hdi = az.hdi(valori, hdi_prob=0.94)

print("Interval HDI 94%:", hdi)

mod = (alpha - 1) / beta

print("Cea mai probabila valoare:", mod)

plt.show()