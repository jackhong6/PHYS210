# PHYS 210: Project 4 – Resonance
# Jack Hong, 30935134
# November 15, 2016

# Simulation of a damped and forced single pendulum.
# No arguments needed to run script. Must run with Python 3.
# Generates the following:
#  1. Plot of maximum amplitude vs force frequency (resonance.pdf)
#  2. Animation of the pendulum with w=w0 (pendulum.mp4)
#  3. Plots of theta(t) and d(theta)/dt as a function of time for
#     w = w0, w << w0, and w >> w0 (phase_space.pdf)

# Some code adapted from:
# http://matplotlib.org/1.5.3/examples/animation/double_pendulum_animated.html

import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as mpl

# Constants ==================================================================
g = 9.8     # acceleration due to gravity (m/s^2)
m = 1       # mass attached to rod (kg)
L = 1       # length of the rod (m)
F = 0.2     # forced force amplitude (N)
b = 0.15    # damping coefficient
I = m*L**2  # moment of inertia (kg*m^2)
w0 = np.sqrt(g/L)  # resonance frequency (s^-1)
# ============================================================================

# Plot and animation parameters ==============================================
dt = 0.05
t = np.arange(0.0, 45, dt)  # time steps
th1 = 0.0  # initial angle in radians
a1 = 0.0   # initial angular velocity in radian per second
init_state = [th1, a1]  # [theta, dth_dt]

wmin = w0-2
wmax = w0+2
dw = 0.1
ws = np.arange(wmin, wmax, dw)  # forcing frequencies (< w0)

savefig = False
showplt = True
# ============================================================================


def deriv(state, t, w):
    """Return [dtheta_dt, d2theta_dt2].
    For use with odeint.
    """
    global g, m, L, F, b, I
    theta = state[0]
    dth_dt = state[1]
    return [dth_dt,
            -b/I*dth_dt - m*g*L/I*np.sin(theta)+F/I*np.cos(w*t)*np.cos(theta)]


# 1. Plot of maximum amplitude vs force frequency (resonance.pdf)
max_thetas = np.zeros_like(ws)

for k in range(len(ws)):
    max_thetas[k] = max(odeint(deriv, init_state, t, args=(ws[k], ))[:, 0])

plt.figure(1)
plt.plot(ws, max_thetas)
plt.title('Maximum Amplitude vs Force Frequency')
plt.xlabel('Force Frequency (s^-1)')
plt.ylabel('Maximum Amplitude (radians)')

if savefig:
    plt.savefig('resonance.pdf')


# 2. Animation of the pendulum with w=w0 (pendulum.mp4)
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(111, autoscale_on=False,
                       xlim=(-1.5, 1.5), ylim=(-1.5, 0))
line, = ax2.plot([], [], 'o-', lw=2)
time_template = 'time = %.1fs'
time_text = ax2.text(0.05, 0.9, '', transform=ax2.transAxes)

yM = odeint(deriv, init_state, t, args=(w0,))
xs = L * np.sin(yM[:, 0])
ys = -L * np.cos(yM[:, 0])


def init():
    line.set_data([], [])
    time_text.set_text('')
    return line, time_text


def updatefig(i):
    thisx = [0, xs[i]]
    thisy = [0, ys[i]]

    line.set_data(thisx, thisy)
    time_text.set_text(time_template % (i*dt))
    return line, time_text


ani = animation.FuncAnimation(fig2, updatefig, range(len(xs)), interval=50,
                              init_func=init)

if savefig:
    ani.save('resonance.mp4')

# Plots of theta(t) and d(theta)/dt as a function of time for
#     w = w0, w << w0, and w >> w0 (phase_space.pdf)
yM_wmin = odeint(deriv, init_state, t, args=(wmin,))
yM_wmax = odeint(deriv, init_state, t, args=(wmax,))

fig3 = plt.figure(3)
mpl.rcParams['xtick.labelsize'] = 9
mpl.rcParams['ytick.labelsize'] = 9

plt.subplot(2, 3, 1)
plt.plot(t, yM_wmin[:, 0])
plt.title(r'$\omega \ll \omega_0$')
plt.xlabel('Time (s)')
plt.ylabel(r'$\theta(t)\ (radians)$')

plt.subplot(2, 3, 4)
plt.plot(t, yM_wmin[:, 1])
plt.title(r'$\omega \ll \omega_0$')
plt.xlabel('Time (s)')
plt.ylabel(r'$\frac{d\theta}{dt}$ $(s^{-1})$')

plt.subplot(2, 3, 2)
plt.plot(t, yM[:, 0], color='r')
plt.title(r'$\omega=\omega_0$')
plt.xlabel('Time (s)')
plt.ylabel(r'$\theta(t)\ (radians)$')

plt.subplot(2, 3, 5)
plt.plot(t, yM[:, 1], color='r')
plt.title(r'$\omega=\omega_0$')
plt.xlabel('Time (s)')
plt.ylabel(r'$\frac{d\theta}{dt}$ $(s^{-1})$')

plt.subplot(2, 3, 3)
plt.plot(t, yM_wmax[:, 0], color='g')
plt.title(r'$\omega \gg \omega_0$')
plt.xlabel('Time (s)')
plt.ylabel(r'$\theta(t)\ (radians)$')

plt.subplot(2, 3, 6)
plt.plot(t, yM_wmax[:, 1], color='g')
plt.title(r'$\omega \gg \omega_0$')
plt.xlabel('Time (s)')
plt.ylabel(r'$\frac{d\theta}{dt}$ $(s^{-1})$')

fig3.set_tight_layout(True)

if savefig:
    plt.savefig('phase_space.pdf')

if showplt:
    plt.show()
