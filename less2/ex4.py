import math
import pylab
from matplotlib import mlab

def x(t, a):
    return math.sin(t+a)
def y(t):
    return math.cos(2*t)

tmin = -20.0
tmax = 20.0
dt = 0.01

tlist = mlab.frange (tmin, tmax, dt)
ylist = [math.cos(2*t) for t in tlist]
pylab.ion()

for a in range (50):
    xlist = [math.sin(t+a) for t in tlist]
    pylab.clf()
    pylab.plot(xlist, ylist)
    pylab.draw()
    pylab.pause(0.3)

pylab.close()