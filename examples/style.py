import matplotlib.pyplot as plt
import matplotlib as mpl
import numpy as np

import plottools as pt
pt.set_publication_rc()


# bar chart
plt.figure()
pt.color.reset_index()
x = np.arange(6)
cat = ['cat1','cat2','cat3','cat4']

p = []
yy = np.zeros_like(x)
for c in cat:
	y = np.random.random_integers(1,high=10,size=x.shape)
	plt.bar(x, y, 0.8, bottom=yy, color=pt.color.next(),label=c )
	yy += y
    
plt.xticks(x+0.4,x)
plt.xlim([x[0]-0.2, x[-1]+0.8+0.2])

plt.ylabel('y-label')
plt.legend(framealpha=0.7)
pt.style.set(['horizontalgrid','noxticks'])

plt.savefig('style_horizontalgridwithoutticks.pdf')



# line chart
plt.figure()
pt.color.reset_index()
x = np.arange(20)
cat = ['cat1','cat2','cat3','cat4']

for c in cat:
	y = np.cumsum( np.random.random_integers(-3,high=5,size=x.shape) )
	plt.plot(x, y, color=pt.color.next(), label=c )

plt.ylabel('y-label')
plt.xlabel('x-label')
plt.legend(framealpha=0.7,loc='upper left')
pt.style.set(['horizontalgrid'])

plt.savefig('style_horizontalgrid.pdf')




# show plots
plt.show()