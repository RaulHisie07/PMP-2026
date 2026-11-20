import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import beta

t=np.linspace(0, 1, 1000)

prior = beta.pdf(t,2,8)
posterior = beta.pdf(t,7,23)

plt.plot(t,prior,label="A priori: beta(2,8)")
plt.plot(t,posterior,label="a posteriori: beta(7,23)")

plt.xlabel("teta")
plt.ylabel("Densitatea de probabilitate")
plt.legend()
plt.grid()
plt.show()