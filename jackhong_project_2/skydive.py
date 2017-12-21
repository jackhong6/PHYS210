# PHYS 210 - Project 2: skydive.py
# Jack Hong, 30935134
# November 1, 2016

# Python 3 script that returns (and prints) the max velocity, time of max
# velocity, final velocity on the ground, and total duration of a simulation of
# Felix Baumgartner's jump in 2012.
# Also plot the velocity and the altitude of the jump as a function of time.

# Just run from command line (python3 skydive.py). No arguments required.

import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Constant Definitions --------------------------------------------------------
m = 118     # Mass of sky diver and equipment in kg
g = 9.8     # Acceleration due to gravity in m/s^2

dt = 1e-3   # time step
vi = 0      # Initial velocity
zi = 40000  # Initial altitude in m
zt = 2000   # Transition altitude when parachute opens in m

CD1 = 0.2   # Phase 1 drag coefficient
CD2 = 1.5   # Phase 2 drag coefficient

A1 = 0.85   # Phase 1 cross-sectional area of sky diver in m^2


def A2(t):
    """Return jumper area for phase 2 in m^2"""
    return 1 + 50*((1-np.exp(-t/5))/(1+np.exp(-t/5)))


def rho1(z):
    """Phase 1 air density in kg/m^3"""
    return 1.22 * np.exp(-z/10000)


rho2 = 1.22  # Phase 2 air density in kg/m^3
# -----------------------------------------------------------------------------

# Phase 1: --------------------------------------------------------------------


def dydtLF1(yLF, tF):
    """Return [dz/dt, dv/dt] in phase 1. For use with odeint"""
    global m, g, CD1, A1, rho1
    z = yLF[0]  # altitude
    v = yLF[1]  # velocity
    return [-v, g-0.5*rho1(z)*CD1*A1*v**2/m]  # [dz/dt, dv/dt]


ti1 = 0.0       # Phase 1 initial time in seconds
tf1 = 200       # Phase 1 final time in seconds (approx)
tLF1 = np.arange(ti1, tf1, dt)  # Array of time values
yiLF1 = [zi, vi]  # initial values for altitude and velocity
yM1 = odeint(dydtLF1, yiLF1, tLF1)  # array of altitudes and velocity

zLF1 = yM1[:, 0]
select = zLF1 > zt
zLF1 = zLF1[select]
vLF1 = yM1[select, 1]
tLF1 = tLF1[select]
# -----------------------------------------------------------------------------

# Phase 2: --------------------------------------------------------------------


def dydtLF2(yLF, tF):
    """Return [dz/dt, dv/dt] in phase 2. For use with odeint."""
    global m, g, CD2, A2, rho2, ti2
    z = yLF[0]
    v = yLF[1]
    return [-v, g-0.5*rho2*CD2*A2(tF-ti2)*v**2/m]  # [dz/dt, dv/dt]


zi2 = zLF1[-1]  # Phase 2 initial altitude (= last element from zLF1)
vi2 = vLF1[-1]  # Phase 2 initial velocity (= last element from vLF1)
ti2 = tLF1[-1]  # Phase 2 initial time (= last element from tLF1)
tf2 = 600       # Phase 2 final time (approx)
tLF2 = np.arange(ti2, tf2, dt)
yiLF2 = [zi2, vi2]
yM2 = odeint(dydtLF2, yiLF2, tLF2)

zLF2 = yM2[:, 0]
select = zLF2 >= 0
zLF2 = zLF2[select]
vLF2 = yM2[select, 1]
tLF2 = tLF2[select]
# -----------------------------------------------------------------------------


def main():
    """Return (and print) the max velocity, time of max velocity, final velocity
    on the ground, and total duration of the jump. Also plot the velocity and
    the altitude as a function of time.
    """
    max_v = np.amax(vLF1) * 3.6  # in km/h
    tmax_v = tLF1[np.argmax(vLF1)]  # in seconds
    final_v = vLF2[-1]  # in m/s
    total_time = tLF2[-1]  # in seconds

    print('The maximum velocity is {:f} km/h'.format(max_v))
    print('The time when max velocity is reached is {:f} s'.format(tmax_v))
    print('The final velocity on the ground is {:f} m/s'.format(final_v))
    print('The total duration of the jump is {:f} s'.format(total_time))

    plt.subplot(2, 1, 1)
    plt.plot(tLF1, zLF1, label='Phase 1')
    plt.plot(tLF2, zLF2, label='Phase 2', color='red', linewidth=2.0)
    plt.title('Simulation of Felix Baumgartner\'s 2012 Jump')
    plt.ylabel('Altitude (m)')
    plt.grid('on')
    plt.legend()

    plt.subplot(2, 1, 2)
    plt.plot(tLF1, vLF1, label='Phase 1')
    plt.plot(tLF2, vLF2, label='Phase 2', color='red', linewidth=2.0)
    plt.ylabel('Velocity (m/s) [Down]')
    plt.xlabel('Time (s)')
    plt.grid('on')
    plt.legend()

    plt.savefig('skydive.pdf')
    plt.show()

    return (max_v, tmax_v, final_v, total_time)

if __name__ == "__main__":
    main()
