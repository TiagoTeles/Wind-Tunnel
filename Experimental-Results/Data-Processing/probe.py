import numpy as np
import pandas as pd
import scipy as sp

def get_polynomial_coeffs(cal):

    c_alpha = cal['c_alpha']
    c_beta  = cal['c_beta']

    # Calibartion Matrix (4th Order Polynomial)
    C = np.empty((c_alpha.shape[0], 15))

    # 0th Order Terms
    C[:, 0] = 1.0

    # 1st Order Terms
    C[:, 1] = c_alpha
    C[:, 2] = c_beta

    # 2nd Order Terms
    C[:, 3] = c_alpha**2
    C[:, 4] = c_alpha * c_beta
    C[:, 5] = c_beta**2

    # 3rd Order Terms
    C[:, 6] = c_alpha**3
    C[:, 7] = c_alpha**2 * c_beta
    C[:, 8] = c_alpha * c_beta**2
    C[:, 9] = c_beta**3

    # 4th Order Terms
    C[:, 10] = c_alpha**4
    C[:, 11] = c_alpha**3 * c_beta
    C[:, 12] = c_alpha**2 * c_beta**2
    C[:, 13] = c_alpha * c_beta**3
    C[:, 14] = c_beta**4

    # Polynomial Coefficients (Least Squares)
    alpha_coeffs = np.linalg.inv(C.T @ C) @ C.T @ cal['alpha']
    beta_coeffs  = np.linalg.inv(C.T @ C) @ C.T @ cal['beta']
    c_din_coeffs = np.linalg.inv(C.T @ C) @ C.T @ cal['c_din']
    c_tot_coeffs = np.linalg.inv(C.T @ C) @ C.T @ cal['c_tot']

    return alpha_coeffs, beta_coeffs, c_din_coeffs, c_tot_coeffs


def sample_polynomial(p, coeffs):

    # Intermediate Coefficients
    c_alpha_a = (p['S4'] - p['S1']) / (p['S7'] - np.mean(p.loc[:, 'S1':'S6'], axis=1))
    c_alpha_b = (p['S3'] - p['S6']) / (p['S7'] - np.mean(p.loc[:, 'S1':'S6'], axis=1))
    c_alpha_c = (p['S2'] - p['S5']) / (p['S7'] - np.mean(p.loc[:, 'S1':'S6'], axis=1))

    # Angular Coefficients
    c_alpha = (1/3) * (2*c_alpha_a + c_alpha_b - c_alpha_c)
    c_beta  = (1/np.sqrt(3)) * (c_alpha_b + c_alpha_c)

    # Sample Polynomial
    value = coeffs[0]

    value += coeffs[1] * c_alpha \
           + coeffs[2] * c_beta

    value += coeffs[3] * c_alpha**2 \
           + coeffs[4] * c_alpha * c_beta \
           + coeffs[5] * c_beta**2

    value += coeffs[6] * c_alpha**3 \
           + coeffs[7] * c_alpha**2 * c_beta \
           + coeffs[8] * c_alpha * c_beta**2 \
           + coeffs[9] * c_beta**3

    value += coeffs[10] * c_alpha**4 \
           + coeffs[11] * c_alpha**3 * c_beta \
           + coeffs[12] * c_alpha**2 * c_beta**2 \
           + coeffs[13] * c_alpha * c_beta**3 \
           + coeffs[14] * c_beta**4

    return value


def interpolate(p, cal):
    
    # Intermediate Coefficients
    c_alpha_a = (p['S4'] - p['S1']) / (p['S7'] - np.mean(p.loc[:, 'S1':'S6'], axis=1))
    c_alpha_b = (p['S3'] - p['S6']) / (p['S7'] - np.mean(p.loc[:, 'S1':'S6'], axis=1))
    c_alpha_c = (p['S2'] - p['S5']) / (p['S7'] - np.mean(p.loc[:, 'S1':'S6'], axis=1))

    # Angular Coefficients
    c_alpha = (1/3) * (2*c_alpha_a + c_alpha_b - c_alpha_c)
    c_beta  = (1/np.sqrt(3)) * (c_alpha_b + c_alpha_c)

    # Interpolated Angles
    alpha = sp.interpolate.griddata((cal['c_alpha'], cal['c_beta']), cal['alpha'], (c_alpha, c_beta))
    beta = sp.interpolate.griddata((cal['c_alpha'], cal['c_beta']), cal['beta'], (c_alpha, c_beta))

    # Interpolated Pressure
    c_din = sp.interpolate.griddata((cal['c_alpha'], cal['c_beta']), cal['c_din'], (c_alpha, c_beta))
    c_tot = sp.interpolate.griddata((cal['c_alpha'], cal['c_beta']), cal['c_tot'], (c_alpha, c_beta))

    return alpha, beta, c_din, c_tot


if __name__ == '__main__':

    # Load Data
    calibration = pd.read_csv('data/calibration.csv', usecols=['alpha', 'beta', 'c_din', 'c_tot', 'c_alpha', 'c_beta'])
    offset = pd.read_csv('data/reference.csv', usecols=['X', 'Y', 'Z', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7'])
    data = pd.read_csv('data/data.csv', usecols=['X', 'Y', 'Z', 'S1', 'S2', 'S3', 'S4', 'S5', 'S6', 'S7'])

    # Correct Units (hPa -> Pa)
    offset.loc[:, 'S1':'S7'] *= 100
    data.loc[:, 'S1':'S7'] *= 100

    # Correct S1 Values (Faulty Probe)
    offset['S1'] = (offset['S2'] + offset['S6']) / 2
    data['S1'] = (data['S2'] + data['S6']) / 2

    # Apply Offset
    data.loc[:, 'S1':'S7'] = (data.loc[:, 'S1':'S7'] - offset.loc[0, 'S1':'S7']) + np.mean(offset.loc[0, 'S1':'S7'])

    # Calculate Velocity
    if False:
        # Calculate Polynomial Coefficients
        alpha_coeffs, beta_coeffs, c_din_coeffs, c_tot_coeffs = get_polynomial_coeffs(calibration)

        # Sample Polynomials
        alpha = sample_polynomial(data, alpha_coeffs)
        beta  = sample_polynomial(data, beta_coeffs)
        c_din = sample_polynomial(data, c_din_coeffs)
        c_tot = sample_polynomial(data, c_tot_coeffs)

    else:
        # Direct Interpolation
        alpha, beta, c_din, c_tot = interpolate(data, calibration)

    # Calculate Properties
    p_total = data['S7'] - c_tot * (data['S7'] - np.mean(data.loc[:, 'S1':'S6'], axis=1))
    p_static = p_total - (data['S7'] - np.mean(data.loc[:, 'S1':'S6'], axis=1)) / c_din
    velocity = np.sqrt(2 * (p_total-p_static) / 1.225)

    # Store Results
    results = pd.DataFrame()
    results['X'] = data['X']
    results['Y'] = data['Y']
    results['Z'] = data['Z']
    results['alpha'] = alpha
    results['beta'] = beta
    results['p_static'] = p_static
    results['velocity'] = velocity

