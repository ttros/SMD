import matplotlib.pyplot as plt
import numpy as np

rng = np.random.default_rng(5)
chi = rng.chisquare(5,500)

plt.hist(chi,30)
plt.errorbar()
plt.savefig('chi/1.pdf')
