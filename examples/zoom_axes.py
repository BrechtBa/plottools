import matplotlib.pyplot as plt
import numpy as np
import plottools as pt


pt.set_publication_rc()


# small figure, box on the left
plt.figure(figsize=(8/2.54,6/2.54))
plt.plot([0,2],[1,2])
plt.plot([0,2],[2,1])
plt.xlabel('xlabel')
plt.ylabel('ylabel')
fig = plt.gcf()
ax = plt.gca()

ax1 = pt.zoom_axes(fig,ax,[0.1,0.3],[1.0,1.2],[1.0,1.9],[1.5,2.0])
plt.plot([0,2],[1,2])
plt.plot([0,2],[2,1])




# axes all around the box
def draw_testlines():
    t = np.linspace(0,30,500)
    plt.plot(np.cos(2*np.pi*t/6),np.sin(2*np.pi*t/5))

    
plt.figure(figsize=(16/2.54,12/2.54))
draw_testlines()
plt.xlabel('xlabel')
plt.ylabel('ylabel')
plt.xlim([-2.2,2.2])
plt.ylim([-2.2,2.2])

fig = plt.gcf()
ax = plt.gca()


count = 0
for dy in [0.8,0,-0.8]:
    for dx in [-0.8,0,0.8]:
        count+=1
        
        if not (dx==0 and dy==0):
        
            #plt.subplot(3,3,count)
            #plt.figure(figsize=(8/2.54,6/2.54))
            s = 2
            ax1 = pt.zoom_axes(fig,ax,[-0.2+dx,0.2+dx],[-0.2+dy,0.2+dy],[-0.4+s*dx,0.4+s*dx],[-0.4+s*dy,0.4+s*dy])
            draw_testlines()
           


# show plots
plt.show()