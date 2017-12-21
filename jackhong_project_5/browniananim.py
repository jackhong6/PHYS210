# PHYS 210: Project 5 – Brownian motion
# Jack Hong, 30935134
# November 20, 2016

# Animation of brownian motion of a single grain.
# No arguments needed to run script.


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

m = 1
M = m * 20
r = 0.03

nmolecules = 400
nframe = 5000
xmin, xmax, ymin, ymax = 0, 1, 0, 1
fig, ax = plt.subplots()
plt.xlim(xmin, xmax)
plt.ylim(ymin, ymax)
dt = 0.001

x = np.random.random(nmolecules)
y = np.random.random(nmolecules)
vx = np.random.randn(nmolecules)
vy = np.random.randn(nmolecules)

xg = 0.5
yg = 0.5
vxg = 0
vyg = 0

im = ax.scatter(x, y)
img = ax.scatter(xg, yg, c='r', s=300)


def updatefig(num):
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

    xg = xg + dt*vxg
    yg = yg + dt*vyg

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

    data = np.stack((x, y), axis=-1)
    im.set_offsets(data)
    img.set_offsets((xg, yg))

ani = animation.FuncAnimation(fig, updatefig, nframe, interval=1, repeat=False)
# ani.save('browniananim.mp4')
plt.show()
