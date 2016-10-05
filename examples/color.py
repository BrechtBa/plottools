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


# some lines
plt.figure()
x = np.linspace(0,2*np.pi,100)
plt.plot(x,np.sin(x- 0*2*np.pi/12),color=pt.color.default['k'],label='k')
plt.plot(x,np.sin(x- 2*2*np.pi/12),color=pt.color.default['b'],label='b')
plt.plot(x,np.sin(x- 4*2*np.pi/12),color=pt.color.default['r'],label='r')
plt.plot(x,np.sin(x- 6*2*np.pi/12),color=pt.color.default['y'],label='y')
plt.plot(x,np.sin(x- 8*2*np.pi/12),color=pt.color.default['o'],label='o')
plt.plot(x,np.sin(x-10*2*np.pi/12),color=pt.color.default['g'],label='g')

plt.plot(x,np.sin(x- 0*2*np.pi/12)-0.1,color=pt.color.defaultlight['k'],label='kl')
plt.plot(x,np.sin(x- 2*2*np.pi/12)-0.1,color=pt.color.defaultlight['b'],label='bl')
plt.plot(x,np.sin(x- 4*2*np.pi/12)-0.1,color=pt.color.defaultlight['r'],label='rl')
plt.plot(x,np.sin(x- 6*2*np.pi/12)-0.1,color=pt.color.defaultlight['y'],label='yl')
plt.plot(x,np.sin(x- 8*2*np.pi/12)-0.1,color=pt.color.defaultlight['o'],label='ol')
plt.plot(x,np.sin(x-10*2*np.pi/12)-0.1,color=pt.color.defaultlight['g'],label='gl')
plt.legend()



# bar plot
pt.color.defaultlight.reset_index()
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
