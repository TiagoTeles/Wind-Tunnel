import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import data
profile_02 = pd.read_csv('data/velocity-02.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])
profile_10 = pd.read_csv('data/velocity-10.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])
profile_16 = pd.read_csv('data/velocity-16.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])

# Calculate derived quantities
profile_02['z'] = profile_02['arc_length'] - 1.0
profile_10['z'] = profile_10['arc_length'] - 1.0
profile_16['z'] = profile_16['arc_length'] - 1.0

profile_02['U'] = np.sqrt(profile_02['U:0']**2 + profile_02['U:1']**2 + profile_02['U:2']**2)
profile_10['U'] = np.sqrt(profile_10['U:0']**2 + profile_10['U:1']**2 + profile_10['U:2']**2)
profile_16['U'] = np.sqrt(profile_16['U:0']**2 + profile_16['U:1']**2 + profile_16['U:2']**2)

# Plot velocity profile
plt.plot(profile_02['U'], profile_02['z'], label=r'$x=-0.8 \; m$')
plt.plot(profile_10['U'], profile_02['z'], label=r'$x= 0.0 \; m$')
plt.plot(profile_16['U'], profile_02['z'], label=r'$x= 0.6 \; m$')

plt.axvline(30, c='tab:red', ls='--', label='Target Velocity')

plt.axhspan(-1, -0.4, color='black', alpha=0.2, lw=0)
plt.axhspan( 1,  0.4, color='black', alpha=0.2, lw=0)

plt.xlabel('Velocity, [m/s]')
plt.ylabel('Z Coordinate, [m]')
plt.legend(loc='upper right')
plt.grid()
plt.show()