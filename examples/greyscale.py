import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

import plottools as pt
from plottools.linearize_greyscale import to_greyscale

# get the greyscale values of all colors
n = len(pt.color.default.cycle)

colors = []
names = []
greyscales = []
for i in range(n):
    names.append( pt.color.default.cycle[i] )
    colors.append( pt.color.default[i] )
    greyscales.append(  np.mean(to_greyscale(pt.color.default[i])) )
    
colors = np.array(colors)
names = np.array(names)
greyscales = np.array(greyscales)


index = np.argsort( greyscales )

# create a figure with the colors sorted by greyscale
fig = plt.figure()
ax = fig.add_subplot(111)
for i,ind in enumerate(index):
    ax.add_patch(  patches.Rectangle( (i, 0), 1.0, 5.0, facecolor=colors[ind,:], edgecolor='none') )

plt.xlim([0,n])
plt.ylim([0,5])

# create a figure with the colors sorted by greyscale as lines
fig = plt.figure()
ax = fig.add_subplot(111)
for i,ind in enumerate(index):
    plt.plot( [0.0,5.0],[i+0.5,i+0.5], linewidth=2, color=colors[ind,:], label=names[ind] )

plt.legend()   
plt.xlim([0,5])    
plt.ylim([0,n])


# plot the greyscale values in order
plt.figure()
plt.plot(np.arange(n),greyscales[index],'o',color=pt.color.default['k'])
for i,ind in enumerate(index):
    plt.text(i+0.12,greyscales[ind],names[ind])

plt.xlim([0,n])
plt.ylim([0.0,0.9])

plt.show()


