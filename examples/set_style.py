import matplotlib.pyplot as plt
import numpy as np

import plottools as pt
pt.set_publication_rc()


# bar plot
plt.figure()
x = np.arange(6)
cat = ['cat1','cat2','cat3','cat4']

p = []
yy = np.zeros_like(x)
for c in cat:
	y = np.random.random_integers(1,high=10,size=x.shape)
	pl = plt.bar(x, y, 0.8, bottom=yy, color=pt.lightcolor.next() )
	p.append(pl[0])
	yy = yy+y
    
plt.xticks(x+0.4,x)
plt.xlim([x[0]-0.2, x[-1]+0.8+0.2])

plt.ylabel('y-label')
plt.legend(p,cat,framealpha=0.7)
pt.set_style('verticalgridonly')

plt.savefig('verticalgridonly_style.pdf')

# show plots
plt.show()