#In this script below, I've used an external program that allows for the graphical placement of data points across an X and Y axis.

import matplotlib.pyplot as plt
import numpy as np
from matplotlib.cm import get_cmap
from matplotlib.colors import Normalize

#Here I'll first generate the first cubic numerals
x_small = np.arange(1, 6)
y_small = x_small ** 3

x_large = np.arange(1, 5001)
y_large = x_large ** 3

#Here I'll add a colormap
norm_small = Normalize(vmin=min(y_small), vmax=max(y_small))
norm_large = Normalize(vmin=min(y_large), vmax=max(y_large))


cmap = get_cmap('viridis')

colors_small = cmap(norm_small(y_small))
colors_large = cmap(norm_large(y_large))

# Here I'll now being plotting
fig, axs = plt.subplots(2, 1, figsize=(10, 12))

# Plot first 5 cubes
axs[0].scatter(x_small, y_small, c=colors_small, s=100)
axs[0].set_title('First 5 Cubic Numbers')
axs[0].set_xlabel('Number')
axs[0].set_ylabel('Cube')
axs[0].grid(True)

# Plot first 5000 cubes
scatter = axs[1].scatter(x_large, y_large, c=colors_large, s=1)
axs[1].set_title('First 5000 Cubic Numbers')
axs[1].set_xlabel('Number')
axs[1].set_ylabel('Cube')
axs[1].grid(True)

# Finally I'll be adding the colorbar for the large plot
fig.colorbar(scatter, ax=axs[1], label='Cube Value')

plt.tight_layout()
plt.show()
