# PHYS 210: Project 3
# Jack Hong, 30935134
# November 6, 2016

# Animation of forest fire model. mp4 already saved in folder.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import colors

f = 0.001   # probability that tree ignites spontaneously
p = 0.01  # probability that an empty space fills with a tree
nframes = 301
init_prob = 0.55
L = 100  # length of one side

# numpy array to keep track of the state of each grid point
# 0 = empty; 1 = tree; 2 = burning
# initially populate with trees with probability init_prob per cell
states = np.array(np.random.random((L, L)) < init_prob).astype('float')

fig = plt.figure()
# color map: empty=white, tree=green, burning=red
cmap = colors.ListedColormap(['white', 'green', 'red'])
im = plt.imshow(states, interpolation='nearest', cmap=cmap, vmin=0, vmax=2)
plt.title('Forest Fire Simulation with f={:g} and p={:g}'.format(f, p))


def updatefig(*args):
    global states

    empty = np.where(states == 0)
    tree = np.where(states == 1)
    burning = np.where(states == 2)

    # tree ignites with probability f even if no neighbour is burning
    states[tree] = (np.random.random(len(tree[1])) < f) + 1

    # tree will burn if at least one neighbour is burning
    states[((np.roll(states, 1, 0) == 2) | (np.roll(states, 1, 1) == 2) |
           (np.roll(states, -1, 0) == 2) | (np.roll(states, -1, 1) == 2)) |
           (np.roll(np.roll(states, -1, 0), -1, 1) == 2) |
           (np.roll(np.roll(states, 1, 0), -1, 1) == 2) |
           (np.roll(np.roll(states, -1, 0), 1, 1) == 2) |
           (np.roll(np.roll(states, 1, 0), 1, 1) == 2) &
           (states == 1)] = 2

    # burning cell turns into empty cell
    states[burning] = 0

    # empty space fills with tree with probability p
    states[empty] = np.random.random(len(empty[1])) < p

    im.set_data(states)
    return im,


ani = animation.FuncAnimation(fig, updatefig,
                              frames=nframes, interval=150, blit=False)

plt.show()
# ani.save('forestfire.mp4')
