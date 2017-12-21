# PHYS 210: Project 6
# Jack Hong, 30935134
# December 1, 2016

# Animation of the solar system with the Sun and all 8 planets.
# Run "python solarsystem.py -h" for usage guide, all arguments are optional.

# Distances and planet radii are not drawn to the same scale.
# Planet radii are proportional to each other, but not to the Sun.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from scipy.integrate import odeint
import sys
import getopt

# Masses of the sun and the planets in units of Earth masses.
#    [ Sun,  Mercury, Venus,  Earth, Mars,  Jupiter, Saturn, Uranus, Neptune]
m = [332946, 0.0553, 0.8150, 1.000, 0.1074, 317.8, 95.16, 14.50, 17.20]
m = np.array(m)

G = 4*np.pi**2/m[0]  # au^3 yr^-2 mEarth^-1

nsteps = 1000
tf = 50  # Earth years
tspan = np.linspace(0, tf, nsteps)

# Initial states for each body.
#    [ x, y, dx/dt, dy/dt ] in units of au and au/yr
init_states = [0.000, 0, 0, 0,                    # Sun [0, 1, 2, 3]
               0.387, 0, 0, 2*np.pi*0.387/0.241,  # Mercury [4, 5, 6, 7]
               0.723, 0, 0, 2*np.pi*0.723/0.615,  # Venus [8, 9, 10, 11]
               1.000, 0, 0, 2*np.pi*1.000/1.000,  # Earth [12, 13, 14, 15]
               1.524, 0, 0, 2*np.pi*1.524/1.881,  # Mars [16, 17, 18, 19]
               5.203, 0, 0, 2*np.pi*5.203/11.86,  # Jupiter [20, 21, 22, 23]
               9.537, 0, 0, 2*np.pi*9.537/29.45,  # Saturn [24, 25, 26, 27]
               19.19, 0, 0, 2*np.pi*19.19/84.02,  # Uranus [28, 29, 30, 31]
               30.07, 0, 0, 2*np.pi*30.07/165]  # Neptune [32, 33, 34, 35]
init_states = np.array(init_states)


def get_accelerations(states):
    """Return the x and y accelerations for the Sun and all the planets"""

    def get_accel_helper(n):
        """Return the x and y acceleration for the nth planet from the Sun."""
        global G
        mi = m[[k for k in range(9) if k != n]]
        xi = states[[k for k in range(36) if k % 4 == 0 and k != 4*n]]
        yi = states[[k for k in range(36) if (k-1) % 4 == 0 and k != 4*n+1]]
        xx = states[4*n]
        yy = states[4*n+1]
        ri = np.vstack((xi-xx, yi-yy))
        wi = G*mi/np.sqrt((xi-xx)**2+(yi-yy)**2)**3

        return np.sum(np.vstack((wi, wi)) * ri, axis=1)

    accels = np.zeros(18)
    for n in range(9):
        a = get_accel_helper(n)
        accels[2*n] = a[0]
        accels[2*n+1] = a[1]

    return accels


def get_derivs(states, t):
    """Return [dx/dt, dy/dt, d2x/dt2, d2y/dt2, ...] for the Sun and planets."""
    vels = states[[k for k in range(36) if (k-2) % 4 == 0 or (k-3) % 4 == 0]]
    vels = np.reshape(vels, (9, 2))
    accels = np.reshape(get_accelerations(states), (9, 2))
    derivs = np.concatenate((vels, accels), axis=1)
    return np.reshape(derivs, -1)


states = np.reshape(odeint(get_derivs, init_states, tspan), (nsteps, 36))


def animate(zoom_flag):
    pos = states[:, [k for k in range(36) if k % 4 == 0 or (k-1) % 4 == 0]]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)
    ax.set_axis_bgcolor('black')
    ax.set_autoscale_on(False)

    if zoom_flag:
        s = 2
    else:
        s = 35

    ax.set_xlim([-s, s])
    ax.set_ylim([-s, s])
    ax.set_xlabel('au')
    ax.set_ylabel('au')
    ims = []

    # Radii of the Sun and planets in units of Earth radius. (Sun not to scale)
    # Also not to scale with distances.
    radii = np.array([2, 0.383, 0.95, 1, 0.532, 10.97, 9.14, 3.98, 4.18])
    if zoom_flag:
        radii = radii * 10

    colors = ['y', 'gray', 'orange', 'b', 'r', 'r', 'orange', 'b', 'b']

    for n in range(nsteps):
        xs = pos[n, [k for k in range(18) if k % 2 == 0]]
        ys = pos[n, [k for k in range(18) if k % 2 != 0]]
        txt = ax.text(0.03, 0.95,
                      'time = {:.2f} days'.format((n+1)*tf/nsteps*365.25),
                      transform=ax.transAxes, color='white')
        img = ax.scatter(xs, ys, s=np.pi*radii**2, c=colors, edgecolor='')
        ims.append([img, txt])

    imani = animation.ArtistAnimation(fig, ims, interval=10, repeat=True)

    plt.show()
    # imani.save('solarsystem_bonus.mp4')


def retrograde():
    earth_coords = states[:, [12, 13]]
    sun_coords = states[:, [0, 1]]
    mars_coords = states[:, [16, 17]]

    r_es = earth_coords-sun_coords
    r_em = mars_coords-earth_coords
    r_es_len = np.linalg.norm(r_es, axis=1)
    r_em_len = np.linalg.norm(r_em, axis=1)
    thetas = []
    for n in range(nsteps):
        thetas.append(np.arccos(np.inner(r_es[n, :], r_em[n, :]) /
                      (r_es_len[n]*r_em_len[n])))

    plt.plot(tspan, thetas)
    plt.title('Earth''s retrograde motion as seen from Mars')
    plt.xlabel('Time (years)')
    plt.ylabel('Theta (radians)')
    # plt.savefig('retrograde.pdf')


def main(argv):
    help_str = 'usage: solarsystem.py -z <zoomflag> -p <plotflag>'
    try:
        opts, args = getopt.getopt(argv, 'hz:p:a:',
                                   ['zoom=', 'plot=', 'animate='])
    except getopt.GetoptError:
        print(help_str)
        sys.exit(2)

    zoomflag = False
    plotflag = False
    aniflag = True
    for opt, arg in opts:
        if opt == '-h':
            print(help_str)
            sys.exit()
        elif opt in ('-z', '--zoom'):
            zoomflag = int(arg)
        elif opt in ('-p', '--plot'):
            plotflag = int(arg)
        elif opt in ('a', '--animate'):
            aniflag = int(arg)

    if plotflag:
        retrograde()
    if aniflag:
        animate(zoomflag)


if __name__ == "__main__":
    main(sys.argv[1:])
