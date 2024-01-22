import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import CFD Data
data_cfd = pd.read_csv('data/pressure.csv', usecols=['U:0', 'U:1', 'U:2', 'p', 'vtkValidPointMask', 'arc_length'])[375:625]
data_cfd['x'] = data_cfd['arc_length'] - 4.0
data_cfd['p'] = (101325 + 1.225*data_cfd['p']) / 100

# Import Experimental Data
data_poly = pd.read_csv('results/polynomial.csv', usecols=['X', 'Y', 'Z', 'alpha', 'beta', 'p_static', 'velocity'])
data_poly['X'] /= 1000
data_poly['Y'] /= 1000
data_poly['Z'] /= 1000
data_poly['p_static'] = (data_poly['p_static'] + 101325 - 99081) / 100

data_interp = pd.read_csv('results/interpolation.csv', usecols=['X', 'Y', 'Z', 'alpha', 'beta', 'p_static', 'velocity'])
data_interp['X'] /= 1000
data_interp['Y'] /= 1000
data_interp['Z'] /= 1000
data_interp['p_static'] = (data_interp['p_static'] + 101325 - 99081) / 100

# Plot Probe Locations
plt.scatter(data_poly['Y'][15:24], data_poly['Z'][15:24], label=r'$q_{avg}$')
plt.scatter(data_poly['Y'][24:34], data_poly['Z'][24:34], marker='x', label='Height')
plt.scatter(data_poly['Y'][34:44], data_poly['Z'][34:44], marker='x', label='Width')
plt.xlabel('Y Coordinate, [m]')
plt.ylabel('Z Coordinate, [m]')
plt.legend()
plt.grid()
plt.show()

# Plot Static Pressure
plt.plot(data_cfd['x'], data_cfd['p'], label='OpenFOAM')
plt.plot(data_poly['X'][0:15], data_poly['p_static'][0:15], label='Polynomial Fit')
plt.plot(data_interp['X'][0:15], data_interp['p_static'][0:15], label='Direct Interpolation')
plt.xlabel('Streamsiwe Coordinate, [m]')
plt.ylabel('Static Pressure, [hPa]')
plt.legend()
plt.grid()
plt.show()

# Determine Section Size
if True:
    data_exp = data_poly
else:
    data_exp = data_interp

# First Section
section_02_avg = np.mean(data_exp['velocity'][15:24])
section_02_NZ = data_exp.loc[24:28, :].sort_values('velocity')
section_02_PZ = data_exp.loc[29:33, :].sort_values('velocity')
section_02_NY = data_exp.loc[34:38, :].sort_values('velocity')
section_02_PY = data_exp.loc[39:43, :].sort_values('velocity')

z_min_02 = np.interp(np.sqrt(0.96)*section_02_avg, section_02_NZ['velocity'], section_02_NZ['Z'])
z_max_02 = np.interp(np.sqrt(0.96)*section_02_avg, section_02_PZ['velocity'], section_02_PZ['Z'])
y_min_02 = np.interp(np.sqrt(0.96)*section_02_avg, section_02_NY['velocity'], section_02_NY['Y'])
y_max_02 = np.interp(np.sqrt(0.96)*section_02_avg, section_02_PY['velocity'], section_02_PY['Y'])

print('Section 0.2 Height: ' + str(z_max_02-z_min_02) + ' [m]')
print('Section 0.2 Width: ' + str(y_max_02-y_min_02) + ' [m]\n')

# Second Section
section_10_avg = np.mean(data_exp['velocity'][44:53])
section_10_NZ = data_exp.loc[53:57, :].sort_values('velocity')
section_10_PZ = data_exp.loc[58:62, :].sort_values('velocity')
section_10_NY = data_exp.loc[63:67, :].sort_values('velocity')
section_10_PY = data_exp.loc[68:72, :].sort_values('velocity')

z_min_10 = np.interp(np.sqrt(0.96)*section_10_avg, section_10_NZ['velocity'], section_10_NZ['Z'])
z_max_10 = np.interp(np.sqrt(0.96)*section_10_avg, section_10_PZ['velocity'], section_10_PZ['Z'])
y_min_10 = np.interp(np.sqrt(0.96)*section_10_avg, section_10_NY['velocity'], section_10_NY['Y'])
y_max_10 = np.interp(np.sqrt(0.96)*section_10_avg, section_10_PY['velocity'], section_10_PY['Y'])

print('Section 2.0 Height: ' + str(z_max_10-z_min_10) + ' [m]')
print('Section 2.0 Width: ' + str(y_max_10-y_min_10) + ' [m]\n')

# Third Section
section_16_avg = np.mean(data_exp['velocity'][77])
section_16_NZ = data_exp.loc[82:89, :].sort_values('velocity')
section_16_PZ = data_exp.loc[89:96, :].sort_values('velocity')
section_16_NY = data_exp.loc[96:103, :].sort_values('velocity')
section_16_PY = data_exp.loc[103:110, :].sort_values('velocity')

z_min_16 = np.interp(np.sqrt(0.96)*section_16_avg, section_16_NZ['velocity'], section_16_NZ['Z'])
z_max_16 = np.interp(np.sqrt(0.96)*section_16_avg, section_16_PZ['velocity'], section_16_PZ['Z'])
y_min_16 = np.interp(np.sqrt(0.96)*section_16_avg, section_16_NY['velocity'], section_16_NY['Y'])
y_max_16 = np.interp(np.sqrt(0.96)*section_16_avg, section_16_PY['velocity'], section_16_PY['Y'])

print('Section 2.0 Height: ' + str(z_max_16-z_min_16) + ' [m]')
print('Section 2.0 Width: ' + str(y_max_16-y_min_16) + ' [m]')
