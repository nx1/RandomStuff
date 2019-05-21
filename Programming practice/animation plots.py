# -*- coding: utf-8 -*-
"""
Created on Sun May  5 23:50:22 2019

@author: norma
"""

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

#Set up the figure, axis, plot element wish wish to animat

fig = plt.figure()
ax = plt.axes(xlim=(0, 10), ylim = (-4, 4))
line, = ax.plot([], [], lw = 2)

#initialization function, plot the background of each frame
def init():
    line.set_data([], [])
    return line,

#animation fucntion. This is called sequentially

def animate(t):
    k = 0.25
    w = 0.5
    x = np.linspace(0,30, 5000)
    y = np.sin(k*x - w*t)
    line.set_data(x,y)
    return line,

#Call the animator.
#blit = True means only re-draw the parts that have changed.


anim = animation.FuncAnimation(fig, animate, init_func = init,
                           frames = 500, interval = 20, blit = True)


plt.show()