import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Import data
data = pd.read_csv('data/residuals.csv',  usecols=['Time', 'Ux', 'Uy', 'Uz', 'p'])

plt.semilogy(data['Time'], data['Ux'], label=r'$u$ Residual')
plt.semilogy(data['Time'], data['Uy'], label=r'$v$ Residual')
plt.semilogy(data['Time'], data['Uz'], label=r'$w$ Residual')
plt.semilogy(data['Time'],  data['p'], label=r'$p$ Residual')

plt.xlabel('Iteration, [-]')
plt.ylabel('Residual, [-]')
plt.legend()
plt.grid()
plt.show()