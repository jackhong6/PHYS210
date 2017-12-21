# PHYS 210: Project 5 – Brownian motion
# Jack Hong, 30935134
# November 20, 2016

# Simulation of brownian motion of a single grain.
# No arguments needed to run script.

import numpy as np
import matplotlib.pyplot as plt

m = 1
M = m * 20
r = 0.03
xg = 0.5
yg = 0.5
vxg = 0
vyg = 0

nmolecules = 4000
nsteps = 15000
xmin, xmax, ymin, ymax = 0, 1, 0, 1
fig, ax = plt.subplots()
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
dt = 0.001

x = np.random.random(nmolecules)
y = np.random.random(nmolecules)
vx = np.random.randn(nmolecules)
vy = np.random.randn(nmolecules)

xgs = np.zeros(nsteps)
ygs = np.zeros(nsteps)


def step():
    global x, y, vx, vy, xg, yg, vxg, vyg

    # handle collisions with the grain
    lcollide = np.where((np.sqrt((x-xg)**2+(y-yg)**2) <= r) & (x < xg))
    rcollide = np.where((np.sqrt((x-xg)**2+(y-yg)**2) <= r) & (x >= xg))

    ltheta = np.arctan2(yg-y[lcollide], xg-x[lcollide])
    rtheta = np.arctan2(yg-y[rcollide], xg-x[rcollide])-np.pi

    vx[lcollide] = -vx[lcollide]
    vx[rcollide] = -vx[rcollide]

    ldvxgs = np.cos(ltheta)*vx[lcollide]
    ldvygs = np.sin(ltheta)*vx[lcollide]
    rdvxgs = np.cos(rtheta)*vx[rcollide]
    rdvygs = np.sin(rtheta)*vx[rcollide]

    vx[lcollide] = np.cos(ltheta)*vx[lcollide]-np.sin(ltheta)*vy[lcollide]
    vy[lcollide] = np.sin(ltheta)*vx[lcollide]+np.cos(ltheta)*vy[lcollide]
    vx[rcollide] = np.cos(rtheta)*vx[rcollide]-np.sin(rtheta)*vy[rcollide]
    vy[rcollide] = np.sin(rtheta)*vx[rcollide]+np.cos(rtheta)*vy[rcollide]

    vxg = vxg-2*(m/M)*(np.sum(ldvxgs) + np.sum(rdvxgs))
    vyg = vyg-2*(m/M)*(np.sum(ldvygs) + np.sum(rdvygs))

    x[lcollide] = xg - r*np.cos(ltheta)
    y[lcollide] = yg - r*np.sin(ltheta)
    x[rcollide] = xg - r*np.cos(rtheta+np.pi)
    y[rcollide] = yg - r*np.sin(rtheta+np.pi)

    # update coordinates of grain
    if xg < xmin or xg > xmax:
        vxg = -vxg
    if yg < ymin or yg > ymax:
        vyg = -vyg

    xg_old = xg
    yg_old = yg
    xg = xg + dt*vxg
    yg = yg + dt*vyg
    r2 = (xg-xg_old)**2 + (yg-yg_old)**2

    # handle molecules hitting the edges of the box
    xout = np.where((x < xmin) | (x > xmax))
    yout = np.where((y < ymin) | (y > ymax))
    vx[xout] = -vx[xout]
    vy[yout] = -vy[yout]

    # update coordinates of molecules
    dx = dt*vx
    dy = dt*vy
    x = x+dx
    y = y+dy

    return (xg, yg, r2)

for k in range(nsteps):
    grain_coords = step()
    xgs[k] = grain_coords[0]
    ygs[k] = grain_coords[1]

plt.figure(1)
plt.plot(xgs, ygs)
plt.title('Full Trajectory of the Grain Over 15000 Time Steps')
# plt.savefig('brownianpath.pdf')

r2s = np.zeros(nsteps)
for m in range(20):
    ssf = 0
    for k in range(nsteps):
        grain_coords = step()
        ssf = ssf+grain_coords[2]
        r2s[k] = r2s[k] + ssf
r2s = r2s/20

plt.figure(2)
t = np.arange(0, nsteps)
plt.plot(t, r2s)
slope, intercept = np.polyfit(t, r2s, 1)
plt.text(9000, 1, 'Slope = '+str(slope))
plt.title('Distance Squared as a Function\
 of Time Averaged Over 20 Simulations')
plt.xlabel(r'Time (s)')
plt.ylabel(r'$<r^2>$')
# plt.savefig('brownianscatter.pdf')
plt.show()
