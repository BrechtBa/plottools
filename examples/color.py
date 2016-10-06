import matplotlib.pyplot as plt
import numpy as np

import plottools as pt


# line plot with thick lines
plt.figure()
x = np.linspace(0,2*np.pi,100)

pt.color.default.set_as_default()
n = len(pt.color.default.cycle)

for i in range(n):
    plt.plot(x,np.sin(x-i*2*np.pi/n),label=pt.color.default.cycle[i],linewidth=2)

plt.legend()


# lines light and dark
plt.figure()
x = np.linspace(0,2*np.pi,100)
for i,key in enumerate( pt.color.default.keys() ):
    plt.plot(x,np.sin(x- i*2*2*np.pi/12),color=pt.color.default[key],label=key)
    plt.plot(x,np.sin(x- i*2*2*np.pi/12)-0.1,color=pt.color.default.light[key])
    plt.plot(x,np.sin(x- i*2*2*np.pi/12)+0.1,color=pt.color.default.dark[key])
plt.legend()



# bar plot
pt.color.default.reset_index()
plt.figure()
x = np.arange(6)
cat = ['cat{}'.format(i+1) for i in range(n)]

p = []
yy = np.zeros_like(x)
for c in cat:
    y = np.random.random_integers(1,high=10,size=x.shape)
    pl = plt.bar(x, y, 0.8, bottom=yy , color=pt.color.default.next())
    p.append(pl[0])
    yy = yy+y
    
plt.legend(p,cat)

# show plots
plt.show()
