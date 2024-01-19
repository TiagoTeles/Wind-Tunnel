import numpy as np
import matplotlib.pyplot as plt

# Plot cost function
time = np.linspace(0, 4000, 400)
gci = np.linspace(0, 0.1, 100)
TIME, GCI = np.meshgrid(time, gci)

cost = TIME/3600 + GCI*(100/2.5)

plt.contourf(TIME, 100*GCI, cost)
plt.colorbar(label='Cost Function')

# Plot Richardson extrapolation
n_cells = -0.0808*time**2 + 1074.2*time + 119993
r = np.power(n_cells/986863, 1/3)
error = 0.0194339453468639 / np.power(r, 4.78713054229863)

plt.plot(time, 100*error, c='tab:orange', label='Extrapolated GCI')

plt.scatter(time[160], 100*error[160], c='tab:green', marker='o',  label='Optimal Case')
plt.scatter(time[26], 100*error[26], c='tab:red', marker='x', label='Simulated Cases')
plt.scatter(time[86], 100*error[86], c='tab:red', marker='x')
plt.scatter(time[277], 100*error[277], c='tab:red', marker='x')

# Plot valid TIME an GCI
plt.axvspan(3600, 4000, color='black', alpha=0.2, lw=1)
plt.axhspan(5, 10, color='black', alpha=0.2, lw=1)

plt.xlabel('Time, [s]')
plt.ylabel('Grid Convergence Index, [%]')

plt.xlim((0, 4000))
plt.ylim((0, 10))

plt.legend(loc='upper right')
plt.show()
