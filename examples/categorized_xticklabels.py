import matplotlib.pyplot as plt
import numpy as np
import plottools as pt


pt.set_publication_rc()


# generate data
C,B,A = np.meshgrid([10,20],[0.4,0.6,0.8],[1,2,3],indexing='ij')
xticklabels = [ A.reshape((-1,)), B.reshape((-1,)), C.reshape((-1,)) ]
values = [np.random.random(len(t)) for t in xticklabels]
xticks = np.arange(len(values[0]))

xticklabelnames = ['coord','$B_\mathrm{value}$','CCC']
labels = ['set1','set2','set3']
fmt = ['${:.2f}$','${}$ m','$10^{{{:.0f}}}$']
rotation = [70,0,0]


# create the figure
plt.figure()
bottom = np.zeros_like(values[0])
for val,lab in zip(values,labels):
    plt.bar(xticks+0.1,val,0.8,bottom=bottom,label=lab,color=pt.color.next(),edgecolor='none')
    bottom += val
    
plt.legend(framealpha=0.7,loc='upper right')
plt.ylabel('y-label')

# set the figure style
pt.set_style('horizontalgridwithoutticks')   
    
# add categories on the x-axis
pt.categorized_xticklabels(xticks+0.5,xticklabels,xticklabelnames=xticklabelnames,fmt=fmt,rotation=rotation)
plt.tight_layout()
plt.savefig('categorized_xticklabels.pdf')
plt.show()