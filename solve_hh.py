from scipy.integrate import odeint
import numpy as np
import pylab as pl

def HH(y, t, I0, t_in, t_end):
    gna = 120.0
    gk = 36.0
    gl = 0.3
    Vna = 115.0
    Vk = -12.0
    Vl = 10.6
    Cm = 1.0
    dydt = np.zeros_like(y)
    V = y[0]
    n = y[1]
    m = y[2]
    h = y[3]
    Iap = 0.0
    if t_in < t < t_end:
        Iap = I0
    alpha_m = 0.1 * (25 - V) / (np.exp((25 - V) / 10) - 1)
    beta_m = 4 * np.exp(-V / 18)
    alpha_h = 0.07 * np.exp(-V / 20)
    beta_h = 1 / (1 + np.exp((30 -V) / 10))
    alpha_n = 0.01 * (10 - V) / (np.exp((10 - V) / 10) - 1)
    beta_n = 0.125 * np.exp(-V / 80)
    term1 = gna * m**3 * h * (V - Vna)
    term2 = gk * n**4 * (V - Vk)
    term3 = gl * (V - Vl)
    dydt[0] = -(term1 + term2 + term3 + Iap)/ Cm
    dydt[1] = alpha_n * (1 - n) - beta_n * n
    dydt[2] = alpha_m * (1 - m) - beta_m * m
    dydt[3] = alpha_h * (1 - h) - beta_h * h
    return dydt


func = lambda y, t: HH(y, t, -5, 2, 4)
y0 = np.array([0.000, 0.3177, 0.0530, 0.5959])
time = np.linspace(0, 20, 1000)
y = odeint(func, y0, time)
pl.figure(1)
pl.plot(time, y[:, 0])

func = lambda y, t: HH(y + np.array([6, 0, 0, 0]), t, -5, 2, 4)
y0 = np.array([0.000, 0.3177, 0.0530, 0.5959])
y = odeint(func, y0, time)
pl.plot(time, y[:, 0])


pl.xlabel('t')
pl.ylabel('V')
pl.grid(True)

pl.show()
