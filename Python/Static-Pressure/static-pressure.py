import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import data
data = pd.read_csv('data/pressure.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])

# Calculate derived quantities
data['x'] = data['arc_length'] - 4.0
data['p'] = (101325 + 1.225*data['p']) / 100
data['U'] = np.sqrt(data['U:0']**2 + data['U:1']**2 + data['U:2']**2)
data['q'] = 0.5 * 1.225 * data['U']**2

# Define wind tunnel sections
nozzle = data[:][0:375]
test_section = data[:][375:625]
collector = data[:][625:715]
diffuser = data[:][715:1000]

# Plot streamwise pressure variation
plt.plot(nozzle['x'], nozzle['p'], label='Nozzle')
plt.plot(test_section['arc_length'] - 4.0, test_section['p'], label='Test Section')
plt.plot(collector['arc_length'] - 4.0, collector['p'], label='Collector')
plt.plot(diffuser['arc_length'] - 4.0, diffuser['p'], label='Diffuser')

plt.axvspan(-4, -1, color='black', alpha=0.2, lw=0)
plt.axvspan( 1,  4, color='black', alpha=0.2, lw=0)

plt.xlabel('Streamsiwe Coordinate, [m]')
plt.ylabel('Static Pressure, [hPa]')
plt.legend()
plt.grid()
plt.show()

# Plot streamwise pressure variation at test section
plt.plot(test_section['x'], test_section['p'], label='Static Pressure')
plt.axhline(np.mean(test_section['p']), c='tab:orange', ls='--', label='Mean')
plt.axhline(np.max(test_section['p']), c='tab:green', ls=':', label='Maximum')
plt.axhline(np.min(test_section['p']), c='tab:red', ls=':', label='Minimum')

plt.xlabel('Streamsiwe Coordinate, [m]')
plt.ylabel('Static Pressure, [hPa]')
plt.legend(loc='upper left')
plt.grid()
plt.show()