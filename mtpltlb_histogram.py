#%%
import matplotlib.pyplot as plt
import numpy as np

x = np.random.normal(170, 10, 250)

plt.hist(x)
plt.show()
# %%
#we used NumPy to randomly generate an array with 250 values, where the values will concentrate around 170, and the standard deviation is 10.