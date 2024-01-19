import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import data
profile_20 = pd.read_csv('data/velocity-N10.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])
profile_21 = pd.read_csv('data/velocity-N09.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])
profile_22 = pd.read_csv('data/velocity-N08.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])
profile_23 = pd.read_csv('data/velocity-N07.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])
profile_24 = pd.read_csv('data/velocity-N06.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])
profile_25 = pd.read_csv('data/velocity-N05.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])

# Calculate derived quantities
profile_20['z'] = profile_20['arc_length'] - 2.0
profile_21['z'] = profile_21['arc_length'] - 2.0
profile_22['z'] = profile_22['arc_length'] - 2.0
profile_23['z'] = profile_23['arc_length'] - 2.0
profile_24['z'] = profile_24['arc_length'] - 2.0
profile_25['z'] = profile_25['arc_length'] - 2.0

profile_20['U'] = np.sqrt(profile_20['U:0']**2 + profile_20['U:1']**2 + profile_20['U:2']**2)
profile_21['U'] = np.sqrt(profile_21['U:0']**2 + profile_21['U:1']**2 + profile_21['U:2']**2)
profile_22['U'] = np.sqrt(profile_22['U:0']**2 + profile_22['U:1']**2 + profile_22['U:2']**2)
profile_23['U'] = np.sqrt(profile_23['U:0']**2 + profile_23['U:1']**2 + profile_23['U:2']**2)
profile_24['U'] = np.sqrt(profile_24['U:0']**2 + profile_24['U:1']**2 + profile_24['U:2']**2)
profile_25['U'] = np.sqrt(profile_25['U:0']**2 + profile_25['U:1']**2 + profile_25['U:2']**2)

# Plot velocity profile
plt.plot(profile_20['U'], profile_20['z'], label=r'$x=-2.0 \; m$')
plt.plot(profile_21['U'], profile_21['z'], label=r'$x=-2.1 \; m$')
plt.plot(profile_22['U'], profile_22['z'], label=r'$x=-2.2 \; m$')
plt.plot(profile_23['U'], profile_23['z'], label=r'$x=-2.3 \; m$')
plt.plot(profile_24['U'], profile_24['z'], label=r'$x=-2.4 \; m$')
plt.plot(profile_25['U'], profile_25['z'], label=r'$x=-2.5 \; m$')

plt.xlabel('Velocity, [m/s]')
plt.ylabel('Z Coordinate, [m]')
plt.legend(loc='upper right')
plt.grid()
plt.show()