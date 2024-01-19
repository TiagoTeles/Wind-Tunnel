import matplotlib.pyplot as plt
import numpy as np

# Import data
section_02 = np.array([
    [1.8406, 1.1870, 0.6896],
    [1.3586, 1.2079, 0.7231],
    [1.0000, 1.2341, 0.7308],
    [0.0000, np.nan, 0.7330]
    ])

section_10 = np.array([
    [1.8406, 1.1313, 0.6447],
    [1.3586, 1.1630, 0.6797],
    [1.0000, 1.1782, 0.6878],
    [0.0000, 1.1921, 0.6902]
    ])

section_16 = np.array([
    [1.8406, 1.1019, 0.6224],
    [1.3586, 1.1167, 0.6297],
    [1.0000, 1.1272, 0.6326],
    [0.0000, 1.1520, 0.6345]
    ])


# Section 02 Width
plt.plot(section_02[0:3, 0], section_02[0:3, 1], marker='o', ls='--', label='Calculated Value')

plt.xlabel('Normalised Grid Spacing, [-]')
plt.ylabel('Width, [m]')

plt.legend()
plt.grid()
plt.show()

# Section 02 Height
plt.plot(section_02[0:3, 0], section_02[0:3, 2], marker='o', ls='--', label='Calculated Value')
plt.scatter(section_02[3, 0], section_02[3, 2], color='tab:orange', label='Extrapolated Value')
plt.errorbar(section_02[3, 0], section_02[3, 2], 0.391*section_02[3, 2]/100, capsize=2)

plt.xlabel('Normalised Grid Spacing, [-]')
plt.ylabel('Height, [m]')

plt.legend()
plt.grid()
plt.show()

# Section 10 Width
plt.plot(section_10[0:3, 0], section_10[0:3, 1], marker='o', ls='--', label='Calculated Value')
plt.scatter(section_10[3, 0], section_10[3, 1], color='tab:orange', label='Extrapolated Value')
plt.errorbar(section_10[3, 0], section_10[3, 1], 1.480*section_10[3, 1]/100, capsize=2)

plt.xlabel('Normalised Grid Spacing, [-]')
plt.ylabel('Width, [m]')

plt.legend()
plt.grid()
plt.show()

# Section 10 Height
plt.plot(section_10[0:3, 0], section_10[0:3, 2], marker='o', ls='--', label='Calculated Value')
plt.scatter(section_10[3, 0], section_10[3, 2], color='tab:orange', label='Extrapolated Value')
plt.errorbar(section_10[3, 0], section_10[3, 2], 0.446*section_10[3, 2]/100, capsize=2)

plt.xlabel('Normalised Grid Spacing, [-]')
plt.ylabel('Width, [m]')

plt.legend()
plt.grid()
plt.show()

# Section 16 Width
plt.plot(section_16[0:3, 0], section_16[0:3, 1], marker='o', ls='--', label='Calculated Value')
plt.scatter(section_16[3, 0], section_16[3, 1], color='tab:orange', label='Extrapolated Value')
plt.errorbar(section_16[3, 0], section_16[3, 1], 2.762*section_16[3, 1]/100, capsize=2)

plt.xlabel('Normalised Grid Spacing, [-]')
plt.ylabel('Width, [m]')

plt.legend()
plt.grid()
plt.show()

# Section 16 Height
plt.plot(section_16[0:3, 0], section_16[0:3, 2], marker='o', ls='--', label='Calculated Value')
plt.scatter(section_16[3, 0], section_16[3, 2], color='tab:orange', label='Extrapolated Value')
plt.errorbar(section_16[3, 0], section_16[3, 2], 0.373*section_16[3, 2]/100, capsize=2)

plt.xlabel('Normalised Grid Spacing, [-]')
plt.ylabel('Width, [m]')

plt.legend()
plt.grid()
plt.show()