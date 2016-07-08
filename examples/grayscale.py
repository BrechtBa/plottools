import matplotlib.pyplot as plt
import matplotlib.patches as patches
import numpy as np

import plottools as pt


# get the grayscale values of all colors
n = len(pt.color.cycle)

colors = []
names = []
grayscales = []
for i in range(n):
    names.append( pt.color.cycle[i] )
    colors.append( pt.color[i] )
    grayscales.append(  0.21*pt.color[i][0] + 0.72*pt.color[i][1] + 0.07*pt.color[i][2] )
    
colors = np.array(colors)
names = np.array(names)
grayscales = np.array(grayscales)


index = np.argsort( grayscales )

# create a figure with the colors sorted by grayscale
fig = plt.figure()
ax = fig.add_subplot(111)
for i,ind in enumerate(index):
    ax.add_patch(  patches.Rectangle( (i, 0), 1.0, 5.0, facecolor=colors[ind,:], edgecolor='none') )

plt.xlim([0,n])
plt.ylim([0,5])


# plot the grayscale values in order
plt.figure()
plt.plot(np.arange(n),grayscales[index],'o',color=pt.color['k'])
for i,ind in enumerate(index):
    plt.text(i+0.12,grayscales[ind],names[ind])

plt.xlim([0,n])
plt.ylim([0.0,0.9])

plt.show()


